from difflib import SequenceMatcher
text1 = "My name is Anh"
text2 = "Hi, my name is Anh"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")


from difflib import SequenceMatcher
text1 = "My name is Anh"
text2 = "Hi, i am a college student"
sequenceScore = SequenceMatcher(None, text1, text2).ratio()
print(f"Both are {sequenceScore * 100} % similar")