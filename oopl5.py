def stringlist(s):
    l=s.split()
    return l
def get_palindrome(lst):
    for i in range(len(lst)):
        txt = lst[i] [::-1]
        if(txt == lst[i]):
            print(lst[i])


sentence="i believe we can buy a racecar"
print("The set of palindromes here are : ")
get_palindrome(stringlist(sentence))

