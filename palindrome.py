def palindrome(n):
    return (n[::-1] == n)
    
print(f"palindrome : {palindrome(input("enter a string : "))}")
