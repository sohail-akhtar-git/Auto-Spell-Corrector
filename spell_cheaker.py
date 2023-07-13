from textblob import TextBlob
#Type in the incorrect spelling
a = input("Enter your text : ")
b = TextBlob(a)
#Obtain corrected spelling as an output
print("The best word similar to "+str(a)+" is "+str(b.correct()))