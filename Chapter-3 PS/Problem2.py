letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Tafsir").replace("<|Date|>", "Jan 1, 2025")) # replace the placeholders with actual values