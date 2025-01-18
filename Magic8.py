import random
random_number = random.randint(1,3)



#input a name and a question
name = "Joel"
question = "Is it going to rain?"


if random_number == 1:
	answer = "Yes"
elif random_number == 2:
	answer = "No"
elif random_number == 3:
	answer = "Ask again"
else:
	answer = "Error"

print(name, "Asks: ", question)
print(answer)
