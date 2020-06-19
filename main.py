


import changeCase
import searchStr
import countStrLen

word = input("\nInput a string : ")

print("\nWord in uppercase : " + changeCase.contoUpper(word))
print("Word in lowercase : " + changeCase.contoLower(word))

toSearch = input("\nInput a string to search within the original string : \n")
searchStr.findtheStr(word, toSearch)

print(countStrLen.numStr(word))
print(countStrLen.numPresent(word))