'''
letters = "cdefghijlmnoqstuvxz"
# def reverseHash(hash):
#     print(hash) # write the code here

def hash(str):
    h = 7
    for i in str:
        h = h * 23 + letters.index(i);
        print(h)
    return h

print(hash("justdoit"))


# print(reverseHash(6933552791181934))
'''

letters = "cdefghijlmnoqstuvxz"

def unHash(hashedNum):
    print(hashedNum)
    #TODO coding here


def hash(str):
    h = 7
    for i in str:
        h = h * 23 + letters.index(i)
    return h

print(hash("justdoit"))
print(unHash(6933552791181934))
