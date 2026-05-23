def palindrome_checker(word):
    reversed_word = word[::-1]
    
    return word == reversed_word

if __name__=="__main__":
    word = input("Enter a word")
    print(f"{word} is a palindrome.") if palindrome_checker(word) else print(f"{word} is not a palindrome.")