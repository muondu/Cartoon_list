channels = {
    "Nickolodean" : 1,
    "Boomerang" : 2,
    "Disney XD" : 3,
}
print(channels)
input1 = input("How many times do you want it to print:  ")  
c = int(input1)
constructor = list()

for h in range(c):
    input2 = channels[input("Enter what you want:  ")]
    print("The show is " + str(input2))
    
    
    constructor.append(input2)
    
    like = sum(constructor)
        
        
        
print("Your favorite show is " + str(like))
