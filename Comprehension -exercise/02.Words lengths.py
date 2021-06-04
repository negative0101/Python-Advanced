text = input().split(', ')

print(', '.join([f"{word} -> {len(word)}"for word in text]))