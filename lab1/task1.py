def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    string = input("Enter a string: ")
    if is_palindrome(string):
        print("True.")
    else:
        print("False.")
        