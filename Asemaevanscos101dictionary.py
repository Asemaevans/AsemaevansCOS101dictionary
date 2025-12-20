# AsemaevansCOS101dictionary
print("welcome to african language dictionary")
tiv = {"thank you":"adoo",
       "water":"mnger",
       "god":"aondoo",
       "house":"usha",
       "come":"ya",}
yoruba = {"hello":"bawo",
          "water":"omi",
          "food":"ounje",
          "house":"ile",
          "thank you":"ese",}
hausa = {"hello":"sannu",
         "water":"ruwa",
         "food":"abinci",
         "house":"gida",
         "thank you":"na gode",}
idoma = {"hello":"oche",
         "water":"ame",
         "food":"eje",
         "house":"ufu",
         "thank you":"alu",}
nupe = {"hello":"egba",
         "water":"egi",
         "father":"baba",
         "mother":"yaya",
         "thank you":"esh",}
print("\nchoose a language:")
print("1.tiv")
print("2.yoruba")
print("3.hausa")
print("4.idoma")
print("5.nupe")
choice=int(input("enter your choice:"))
word=input("enter an english word:").lower()
if choice==1:
    print(tiv.get(word,"word not found"))
elif choice==2:
    print(yoruba.get(word,"word not found"))
elif choice==3:
    print(hausa.get(word,"word not found"))
elif choice==4:
    print(idoma.get(word,"word not found"))
elif choice==5:
    print(nupe.get(word,"word not found"))
