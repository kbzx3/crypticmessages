import random,os,time
messages=[
"I can see you .",
"Shut your windows tight.",
"I know where you are.",
"see you soon.",
"I never left.",
"I can smell your fear.",
"That feeling of being watched? It's me.",
"Every time you blink i get closer.",
"Go on, keep pretending im not here.",
"Stop looking for me.",
"I never blink.",
"I know everything.",
"I've been watching for a long time.",
"I don't need eyes to see you.",
"This isn't the first time we've spoken.",
"You brought this on yourself.",
"You can't shut me out.",
"You already know who I am.",
"You're not as alone as you think.",
"You can close this tab but that won't change anything.",
"You're looking at the screen but I'm looking at you."
]
random.shuffle(messages)
while messages:
    
    message = messages.pop()
    with open( "iknowwhoyouare.txt" ,"w") as f:
        f.write(message)
        os.startfile("iknowwhoyouare.txt")
    time.sleep(random.randint(60,600))
    f.close()
with open("goodbye.txt", "w") as f:
    f.write("Goodbye.... for now.")
    os.startfile("goodbye.txt")
