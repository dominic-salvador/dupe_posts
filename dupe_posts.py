# python3.8.x

# write a program to automate 
#  duplicate posting on social media:
#  I love you (1...n)

# program start #

# initialize variables
sentence = input("Sentence to be duplicated:\n-> ")
repetitions = input("For how many repetitions:\n-> ")

# prepare variables
repetitions = int(repetitions) + 1

# print duplicate posts
print("\nBirdbook prompt:")
print(sentence)
for number in range (2,repetitions):
    print(sentence + " (%d)" % number)
