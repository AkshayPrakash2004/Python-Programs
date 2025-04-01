k=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
   'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encrypt():
    a=input("enter your message")
    b=int(input("enter shift"))
    word=""
    for letter in a:
        pos=k.index(letter)
        npos=pos+b
        c=k[npos]
        word=word+c
    print(word)
def decrypt():
    a=input("enter your message")
    b=int(input("enter shift"))
    word=""
    for letter in a:
        pos=k.index(letter)
        npos=pos-b
        c=k[npos]
        word=word+c
    print(word)
def final():
    print("enter 1 for encrypt and 0 for decrypt")
    f=input()
    match f:
        case "1":
            encrypt()
        case "0":
            decrypt()
final()           




    


    
    
    