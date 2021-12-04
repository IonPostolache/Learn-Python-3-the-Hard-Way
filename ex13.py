from sys import argv
#read the WYSS section for how to run this
script, fi_v, s_v, t_v, f_v= argv
print("The script is called:", script)
print("Your first variable is:", fi_v)
print("Your second variable is:", s_v)
print("Your third variable is:", t_v)
print("Your fourth variable is:", f_v)

#to run this script you need to type: python ex13.py first second third fourth.

arg_no=input("how many argument are used in this exercise?")
print(f"So, {arg_no}  arguments are used in this exercise.")
