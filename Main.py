import random
import winsound

data=[1,2,3,4,5,6]

probabilities=[0.1,0.2,0.2,0.3,0.05,0.15]

def generate_number(data,probabilities):
    random_number=random.random()
    if (random_number <= probabilities[0]):
        return data[0]

    for i in range (1,len(probabilities)):

        if ( random_number >= sum(probabilities[:i]) and random_number < sum (probabilities[:i+1])):
            return data[i]



size=int(input('Enter the size of new Array : '))
while (size <= 0):
    winsound.Beep(500,1000)
    size = int(input('Re-enter the size of new Array : '))

new_data=[]
for i in range (size):
    new_data.append(generate_number(data,probabilities))

print(new_data)
for i in range(1,7):
    print(i,":",float(new_data.count(i)/size))

