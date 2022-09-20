with open('currency.txt') as f:
    lines= f.readlines()
    
currDict={}
for line in lines:
    parsed= line.split('\t')
    currDict[parsed[0]]=parsed[1]

amount = int(input("Enter the amount in INR: "))
print("Available options for conversion are: \n")
for item in currDict.keys():
    print(item)
currency = input("Please choose one of the above options for conversion: ")
print(f'{amount} INR is equal to {amount*float(currDict[currency])} {currency} ')
