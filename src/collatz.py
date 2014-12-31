## Calculate how many steps it takes to reach 1 using
## the Collatz Conjecture from a user-determined number
__author__ = "sor"
__date__ = "$Dec 30, 2014 11:37:21 PM$"

def collatz():
    num = int(raw_input("Enter a number to begin: "))
    count = 0
    while num != 1:
        if num % 2 == 0:
            num -= num/2
            count+=1
        else:
            num = num*3 + 1
            count+=1
    return count

if __name__ == "__main__":
    print collatz()