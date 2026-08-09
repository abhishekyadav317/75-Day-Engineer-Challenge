# hashmap pattern or frequency counting 
def is_anagram(s,t):

    if len(s) != len(t):
        return False

    frequency = {}

    for character in s:
        if character in frequency :
            frequency[character] += 1
        else :
            frequency[character] = 1
              

    for character in t :
        if character not in frequency or frequency[character] == 0 :
            return False
        else :
            frequency[character] -= 1
           
    return True

result = is_anagram("anagram" , "nagaaam" )  
print(result)  


