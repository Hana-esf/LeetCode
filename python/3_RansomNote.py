from unittest import result


from collections import OrderedDict

def canConstruct(ransomNote: str, magazine: str) -> bool:

    result_ran = {}
    for keys in ransomNote:
        result_ran[keys] = result_ran.get(keys, 0) + 1
    result_ran = OrderedDict(sorted(result_ran.items()))

    result_mag = {}  
    for keys in magazine:
        result_mag[keys] = result_mag.get(keys, 0) + 1
    result_mag = OrderedDict(sorted(result_mag.items()))

    print(result_ran)
    print(result_mag)
    for i in result_ran:
        if i not in result_mag or result_ran[i] > result_mag[i]:
            return False
    return True




#explanation : 
#the unique chars and frequency of each char in both strings should be the same
#main
ransom = input('Enter ransom : ')
mag = input('Enter mag : ')
print(canConstruct(ransom,mag))
