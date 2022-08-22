def romanToInt(roman_nom):
        roman_numbers = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        integers = [roman_numbers[i] for i in roman_nom]
        result_int = 0
        i = 0
        while i < len(roman_nom):
            if i+1 < len(roman_nom):
                if integers[i] >= integers[i+1]:
                    result_int = result_int + integers[i]
                    i += 1
                else:
                    temp_int = 0
                    temp_int = integers[i+1] - integers[i]
                    print(temp_int)
                    result_int += temp_int
                    i += 2
            else:
                result_int += integers[i]
                i += 1
        return result_int


   


#main
roman_str = input('Enter the roman number : ')
print(romanToInt(roman_str))