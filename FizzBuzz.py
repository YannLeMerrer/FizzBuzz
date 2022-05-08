def fizzBuzz(value):

    if int(value)%3 == 0 and int(value)%5 == 0 :
        print("Fizz Buzz")

    elif int(value)%3 == 0 :
        print ("Fizz")

    elif int(value)%5 == 0 :
        print ("Buzz")

    else :
        print(value)

with open('chose.txt', 'r') as fichier:
    contenu = fichier.readlines()
    for line in contenu:
        fizzBuzz(line.rstrip('\n'))
