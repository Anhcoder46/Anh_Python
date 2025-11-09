#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Trích xuất văn bản từ PDF bằng Python
- Hỗ trợ PDF văn bản (pdfplumber, PyPDF2)
- Fallback OCR cho PDF scan (pytesseract + pdf2image)

Cách dùng nhanh:
  python Trich_van_ban_tu_file_PDF.py -i "path/to/file.pdf"
  python Trich_van_ban_tu_file_PDF.py -i "file.pdf" -o "out.txt" --pages "1-3,5" --mode auto

Cài đặt phụ thuộc (khuyến nghị):
  pip install pdfplumber PyPDF2 pytesseract pdf2image pillow

Windows OCR yêu cầu cài thêm:
- Tesseract OCR: https://github.com/UB-Mannheim/tesseract/wiki
  (đường dẫn mặc định: C:\\Program Files\\Tesseract-OCR\\tesseract.exe)
- Poppler for Windows (cho pdf2image): https://github.com/oschwartz10612/poppler-windows/releases/
  (sau khi giải nén, chỉ định --poppler-path tới thư mục bin)
"""

from __future__ import annotations
import argparse
import logging
import os
import re
import sys
from typing import Iterable, List, Optional, Sequence, Tuple

# Thư viện tùy chọn
try:
    import pdfplumber  # type: ignore
except Exception:  # pragma: no cover
    pdfplumber = None  # type: ignore

try:
    import PyPDF2  # type: ignore
except Exception:  # pragma: no cover
    PyPDF2 = None  # type: ignore

try:
    import pytesseract  # type: ignore
except Exception:  # pragma: no cover
    pytesseract = None  # type: ignore

try:
    from pdf2image import convert_from_path  # type: ignore
except Exception:  # pragma: no cover
    convert_from_path = None  # type: ignore


def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%H:%M:%S",
    )


def get_num_pages(pdf_path: str) -> int:
    # Ưu tiên PyPDF2 do mở nhanh lấy số trang
    if PyPDF2 is not None:
        try:
            with open(pdf_path, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                return len(reader.pages)
        except Exception:
            logging.debug("PyPDF2 không lấy được số trang, thử pdfplumber.")
    if pdfplumber is not None:
        try:
            with pdfplumber.open(pdf_path) as pdf:
                return len(pdf.pages)
        except Exception:
            logging.debug("pdfplumber không lấy được số trang.")
    raise RuntimeError("Không thể xác định số trang PDF. Hãy đảm bảo file hợp lệ và đã cài PyPDF2/pdfplumber.")


def parse_page_ranges(pages_expr: str, total_pages: int) -> List[int]:
    """Chuyển biểu thức trang (vd: "1-3,5,7-") thành danh sách index 0-based.
    """
    pages_expr = pages_expr.strip()
    if not pages_expr or pages_expr.lower() in {"all", "*"}:
        return list(range(total_pages))

    result: List[int] = []
    parts = [p.strip() for p in pages_expr.split(",") if p.strip()]
    for part in parts:
        m = re.match(r"^(\d+)?\s*-\s*(\d+)?$", part)
        if m:
            start_s, end_s = m.groups()
            start = int(start_s) if start_s else 1
            end = int(end_s) if end_s else total_pages
            if start < 1:
                start = 1
            if end > total_pages:
                end = total_pages
            if start > end:
                start, end = end, start
            result.extend(range(start - 1, end))
        else:
            if not part.isdigit():
                raise ValueError(f"Biểu thức trang không hợp lệ: '{part}'")
            idx = int(part)
            if not (1 <= idx <= total_pages):
                raise ValueError(f"Trang vượt phạm vi: {idx} (1..{total_pages})")
            result.append(idx - 1)

    # Loại trùng và sắp xếp
    return sorted(set(result))


def extract_text_with_pdfplumber(pdf_path: str, page_indexes: Sequence[int]) -> str:
    if pdfplumber is None:
        raise RuntimeError("Chưa cài pdfplumber. Cài đặt: pip install pdfplumber")
    texts: List[str] = []
    with pdfplumber.open(pdf_path) as pdf:
        for i in page_indexes:
            if i < 0 or i >= len(pdf.pages):
                logging.warning("Bỏ qua trang %s (vượt phạm vi)", i + 1)
                continue
            page = pdf.pages[i]
            txt = page.extract_text() or ""
            texts.append(f"\n=== Trang {i+1} ===\n{txt.strip()}\n")
    return "\n".join(texts).strip()


def extract_text_with_pypdf2(pdf_path: str, page_indexes: Sequence[int]) -> str:
    if PyPDF2 is None:
        raise RuntimeError("Chưa cài PyPDF2. Cài đặt: pip install PyPDF2")
    texts: List[str] = []
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for i in page_indexes:
            if i < 0 or i >= len(reader.pages):
                logging.warning("Bỏ qua trang %s (vượt phạm vi)", i + 1)
                continue
            page = reader.pages[i]
            # extract_text của PyPDF2 có thể kém chính xác hơn pdfplumber
            txt = page.extract_text() or ""
            texts.append(f"\n=== Trang {i+1} ===\n{txt.strip()}\n")
    return "\n".join(texts).strip()


def ocr_pdf(
    pdf_path: str,
    page_indexes: Sequence[int],
    lang: str = "eng",
    dpi: int = 300,
    tesseract_cmd: Optional[str] = None,
    poppler_path: Optional[str] = None,
) -> str:
    if pytesseract is None or convert_from_path is None:
        raise RuntimeError(
            "Chưa cài OCR phụ thuộc. Cài đặt: pip install pytesseract pdf2image pillow\n"
            "Ngoài ra cần cài Tesseract OCR và Poppler (xem hướng dẫn trong phần đầu file)."
        )

    # Thiết lập đường dẫn tesseract nếu cung cấp hoặc dùng mặc định Windows nếu có
    if tesseract_cmd:
        pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
    else:
        default_win_path = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        if os.name == "nt" and os.path.isfile(default_win_path):
            pytesseract.pytesseract.tesseract_cmd = default_win_path

    texts: List[str] = []
    total = len(page_indexes)
    for idx, i in enumerate(page_indexes, start=1):
        logging.info("OCR trang %s/%s (trang gốc: %s)", idx, total, i + 1)
        # pdf2image dùng index trang 1-based
        images = convert_from_path(
            pdf_path,
            dpi=dpi,
            first_page=i + 1,
            last_page=i + 1,
            poppler_path=poppler_path,
        )
        if not images:
            logging.warning("Không render được ảnh từ trang %s", i + 1)
            continue
        # Nếu có nhiều ảnh (hiếm), OCR và nối
        page_texts: List[str] = []
        for im in images:
            txt = pytesseract.image_to_string(im, lang=lang) or ""
            page_texts.append(txt.strip())
        texts.append(f"\n=== Trang {i+1} (OCR) ===\n{'\n\n'.join(page_texts).strip()}\n")
    return "\n".join(texts).strip()


def extract_text(
    pdf_path: str,
    pages_expr: str,
    mode: str = "auto",
    ocr_lang: str = "eng",
    ocr_dpi: int = 300,
    tesseract_cmd: Optional[str] = None,
    poppler_path: Optional[str] = None,
) -> str:
    total_pages = get_num_pages(pdf_path)
    page_indexes = parse_page_ranges(pages_expr, total_pages)
    logging.info("Tổng số trang: %s | Trích: %s", total_pages, ",".join(str(i + 1) for i in page_indexes))

    text = ""
    if mode in ("text", "auto"):
        # Ưu tiên pdfplumber
        try:
            if pdfplumber is not None:
                logging.debug("Thử trích xuất với pdfplumber...")
                text = extract_text_with_pdfplumber(pdf_path, page_indexes)
            elif PyPDF2 is not None:
                logging.debug("pdfplumber không có. Thử PyPDF2...")
                text = extract_text_with_pypdf2(pdf_path, page_indexes)
        except Exception as e:
            logging.warning("Lỗi khi trích xuất văn bản PDF: %s", e)

        if mode == "text":
            return text

    # Fallback OCR nếu auto và văn bản quá ít
    if mode == "auto":
        enough_text = len(text.strip()) >= 50  # ngưỡng đơn giản
        if not enough_text:
            logging.info("Văn bản trích xuất ít, chuyển sang OCR...")
            try:
                text_ocr = ocr_pdf(
                    pdf_path,
                    page_indexes,
                    lang=ocr_lang,
                    dpi=ocr_dpi,
                    tesseract_cmd=tesseract_cmd,
                    poppler_path=poppler_path,
                )
                if len(text_ocr.strip()) > len(text.strip()):
                    text = text_ocr
            except Exception as e:
                logging.error("Không thực hiện được OCR: %s", e)
    elif mode == "ocr":
        text = ocr_pdf(
            pdf_path,
            page_indexes,
            lang=ocr_lang,
            dpi=ocr_dpi,
            tesseract_cmd=tesseract_cmd,
            poppler_path=poppler_path,
        )

    return text


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Trích xuất văn bản từ PDF (hỗ trợ OCR fallback)",
    )
    parser.add_argument(
        "-i", "--input", dest="input_pdf", required=True, help="Đường dẫn file PDF",
    )
    parser.add_argument(
        "-o", "--output", dest="output_txt", default=None, help="Ghi kết quả ra file .txt (mặc định: in ra màn hình và tạo cùng tên .txt cạnh file PDF)",
    )
    parser.add_argument(
        "--pages", dest="pages", default="all", help="Chọn trang, ví dụ: 'all' | '1-3,5,7-'",
    )
    parser.add_argument(
        "--mode", dest="mode", choices=["auto", "text", "ocr"], default="auto", help="Chế độ trích xuất",
    )
    parser.add_argument(
        "--ocr-lang", dest="ocr_lang", default="eng", help="Ngôn ngữ OCR (vd: 'eng', 'vie', 'eng+vie')",
    )
    parser.add_argument(
        "--ocr-dpi", dest="ocr_dpi", type=int, default=300, help="DPI render ảnh cho OCR (mặc định 300)",
    )
    parser.add_argument(
        "--tesseract-cmd", dest="tesseract_cmd", default=None, help="Đường dẫn tesseract.exe nếu cần chỉ định thủ công",
    )
    parser.add_argument(
        "--poppler-path", dest="poppler_path", default=None, help="Đường dẫn thư mục bin của Poppler (Windows)",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Bật log chi tiết",
    )

    args = parser.parse_args(argv)
    setup_logging(args.verbose)

    input_pdf = os.path.abspath(args.input_pdf)
    if not os.path.isfile(input_pdf):
        logging.error("Không tìm thấy file: %s", input_pdf)
        return 2

    try:
        text = extract_text(
            pdf_path=input_pdf,
            pages_expr=args.pages,
            mode=args.mode,
            ocr_lang=args.ocr_lang,
            ocr_dpi=args.ocr_dpi,
            tesseract_cmd=args.tesseract_cmd,
            poppler_path=args.poppler_path,
        )
    except Exception as e:
        logging.exception("Lỗi trích xuất văn bản: %s", e)
        return 1

    # Xuất kết quả
    if args.output_txt:
        out_path = os.path.abspath(args.output_txt)
    else:
        base, _ = os.path.splitext(input_pdf)
        out_path = base + ".txt"

    try:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text or "")
        print(text)  # vẫn in ra màn hình để tiện xem nhanh
        logging.info("Đã ghi văn bản ra: %s", out_path)
    except Exception as e:
        logging.error("Không ghi được file kết quả '%s': %s", out_path, e)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
