*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${x}	10
${y}	10
# @{NUMBERS}		1  2  3  4  5  a

*** Test Cases ***
SO SANH HAI BIEN 1
    #SO SANH HAI BIEN 1
    should Be Equal		${x}	${y}

SO SANH HAI BIEN 2
    Should Be NOT Equal		${x}	${y}

# Điều kiện
IF ${x} == ${y}
    Log		${x} == ${y}
    Log      Bằng nhau
ELSE IF ${x} != ${y}
    Log		Khác nhau 
END

    #Vòng lặp
    FOR    ${i}	IN RANGE	10
        Log		${i}
    END
Vong lap
    @{NUMBERS}= 	Create List	1	2	3	4	5
    FOR	${number}	IN     @{NUMBERS}
        Log To Console		${number}
    END

Click Element Button
    TRY
        Click Element		//button[@id='submit']
    EXCEPT
        Log To Console		"không tìm thấy nút bấm"
    END

*** Keywords ***
So Sanh Hai Bien
    [Documentation]		Kiểm tra hai biến có bằng nhau hay không
    [Arguments]		${x}	${y}
    should Be Equal		${x}	${y}
    Should Be Not Equal		${x}	${y}
    Should Be Equal As Strings		${x}	${y}
    Should Be Equal As Numbers		${x}	${y}