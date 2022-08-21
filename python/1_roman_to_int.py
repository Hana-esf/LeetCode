def romanToInt(roman_nom):
    roman_numbers = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}

    integer = roman_numbers[roman_nom[0]]
    print('int : ',integer)
    for i in range(1,len(roman_nom)):
        print(roman_nom[i],' , ',roman_numbers[roman_nom[i]])
        if roman_numbers[roman_nom[i]] > roman_numbers[roman_nom[i-1]]:
            integer = roman_numbers[roman_nom[i]] - integer
        else:
            integer += roman_numbers[roman_nom[i]]

    return integer


#main
roman_str = input('Enter the roman number : ')
print(romanToInt(roman_str))