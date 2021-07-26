n = input("Enter the number and see if it is palindrome: ")
if n == n[::-1]:
    print("This number is palindrome")
else:
    print("This number is not palindrome")