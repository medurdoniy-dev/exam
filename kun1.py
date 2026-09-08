def count_vowels_and_consonants(text):
    vowels = set("aeiouAEIOU")
    result = {"unli": 0, "undosh": 0}
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                result["unli"] += 1
            else:
                result["undosh"] += 1
                
    return result
soz = input ("soz kiriting : ")
print (count_vowels_and_consonants(soz))push