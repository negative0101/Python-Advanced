def palindrome(word,index):
    rev_index = len(word) - index -1
    if index >= rev_index:
        return f'{word} is a palindrome'
    if not word[index] == word[rev_index]:
        return f'{word} is not a palindrome'
    return palindrome(word,index+1)