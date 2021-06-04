text = input().split()

print('\n'.join([word for word in text if len(word) % 2 == 0]), end=' ')
