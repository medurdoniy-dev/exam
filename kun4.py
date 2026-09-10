import json 

with open ('students.json' , "r") as file :
    data = json.load(file)
Best=(max(data, key=lambda x: x['grade']))
print ("Eng a'lochi o'quvchi 🤩🤩🤩 " , Best['name'] , Best['grade'])
Poor = (min(data, key=lambda x: x['grade']))
print ("Eng a'lochi o'quvchi 😣😣😣 " , Poor['name'] , Poor['grade'])
average = sum(x['grade'] for x in data) / len(data)
print ("O'rtacha ball 🫡 🫡 🫡 " , round(average))