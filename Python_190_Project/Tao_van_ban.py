from transformers import pipeline
model = pipeline("text-generation", model = "gpt2")

sentence = model("Hi, My name is Anh, I am here",
                 do_sample = True, top_k = 50,
                 temperature = 0.9, max_new_tokens = 100,
                 truncation = True, num_return_sequences = 2)

for i in sentence:
    print(i["generated_text"])