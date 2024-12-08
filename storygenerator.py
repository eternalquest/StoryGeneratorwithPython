#accesses and reads data from the txt file
with open("story.txt","r") as f:
    story=f.read()
#set named words
words=set()
start_of_word=-1

target_start="<"
target_end=">"
#Reads the data and identifies and stores the words inside set named word
for i,char in enumerate(story):
    if char== target_start:
        start_of_word=i
    
    if char== target_end and start_of_word !=-1:
        word=story[start_of_word:i +1]
        words.add(word)
        start_of_word=-1


answers ={}
#takes input from user and stores it in answers library
for word in words:
    answer = input("enter a word for " + word +":" )
    answers[word]=answer

#replaces with user inputs
for word in words:
   story= story.replace(word,answers[word])

#prints story
print(story)
