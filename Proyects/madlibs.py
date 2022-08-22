#string concatenation (how to put strings together)
#suppose we want to create a string that says "subscribe to ____"

youtuber="i dont know" #some string variable

#print("subscribe to "+youtuber)
#print("subscribe to {}".format(youtuber))
print(f"subscribe to {youtuber}") #can be the best form

adj= input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("famous_person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time beacuase\
            i love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
