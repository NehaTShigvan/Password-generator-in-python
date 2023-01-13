import string
import random

if __name__ == "__main__":
    pLength = int(input("Enter the length of your password: "))
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    # print(s1)
    # print(s2)
    # print(s3)
    # print(s4)
    charList = []
    charList.extend(s1)
    charList.extend(s2)
    charList.extend(s3)
    charList.extend(s4)
    # print(charList)
    # random.shuffle(charList)
    # print("".join(charList[:pLength]))
    print("Your password is: ")
    print("".join(random.sample(charList,pLength)))