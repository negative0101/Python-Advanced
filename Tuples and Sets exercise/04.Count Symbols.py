text = input()

dictionary= {}
for i in text:
    if i not in dictionary:
        dictionary[i]=0
    dictionary[i] +=1
sorted_dict = sorted(dictionary.items(), key=lambda x: x[0])
for key,value in sorted_dict:
    print(f'{key}: {value} time/s')
#seems more reasonable to solve this problem with a dictionary.