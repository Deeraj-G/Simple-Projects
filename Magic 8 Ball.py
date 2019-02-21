import random
from time import sleep

response = ["Yes", "No", "Maybe", "Only if you believe in God", "To die", "In two years", "At the age of 50"]

def bulk():
    question = input("Ask me any question: ")
    print("Processing...")
    sleep(2.5)
    print(random.choice(response))
bulk()

sleep(1)

restart = input("Would you like to ask another question? ")
if restart == "yes" or restart == "Yes":
    bulk()
if restart == "no" or restart == "No":
    print("Ok")

