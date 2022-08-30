def fizzBuzz(n: int):

    answer = []

    for i in range(1,n+1):
        if i%15 == 0:
            answer.append("FizzBuzz")
        elif i%3 ==0:
            answer.append("Fizz")
        elif i%5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))


    return answer

#another way
#return ['FizzBuzz' if i%15 == 0 else 'Buzz' if i%5 == 0 else 'Fizz' if i%3 == 0 else str(i) for i in range(1,n+1)]

#main
N = int(input("Enter the n : "))
print(fizzBuzz(N))