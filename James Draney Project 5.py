#Project Number 5
#James Draney
#jamesdraney99@gmail.com
#Lets get it
#Sentence Program
#yktv


import math
import string

def main():


    sentence=(input("Write a Sentence "))
    print("Number of Characters: ", len(sentence))
    words=len(sentence.split())
    print("Number of Words: " ,words)
    count=0
    numwords=1
    for i in range (len(sentence)):
        if sentence[count]==" ":
            count=count+1
            
        
   
    
    x=len(sentence.replace(" ", ""))/words
        
    print("Average Word Length ",(x))

main()


#divide number of letters by number of words
#convert letters in wor into numeric values
#divide those values by wor
