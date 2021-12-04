from sys import argv
script, user_name=argv
prompt1='>---'

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes=input (prompt1)

print(f"Where do you live {user_name}?")
lives=input(prompt1)

print("What kinf of computer do you have?")
computer=input(prompt1)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
