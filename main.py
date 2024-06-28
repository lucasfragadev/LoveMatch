# Dev. Lucas Fraga - 100 Days of Code: The Complete Python Pro Bootcamp - LoveMatch 1.0
# PT-BR: Calculadora que mede a compatibilidade amorosa entre duas pessoas com base nos seus nomes, fornecendo um resultado que indica a quantidade de amor.
# EN-US: Calculator that measures the love compatibility between two people based on their names, providing a result that indicates the amount of love.

print("\nBem-vindo (a) à calculadora do amor! Vamos saber seu score. // Welcome to the love calculator! Let's find out your score.\n")
name1 = input("Qual o seu nome? // What is your name? ").lower()
name2 = input("Qual o nome dele (a)? // What's his or her name? ").lower()
combined_names = name1 + name2

t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
first_digit = t + r + u + e

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e = combined_names.count("e")
second_digit = l + o + v + e 

compatibility = str(first_digit) + str(second_digit)
score = int(compatibility)

if score < 10 or score > 90:
    print(f"\nYour score is {score}, you go together like coke and mentos!")
    print(f"Sua pontuação é {score}, vocês combinam como coca-cola e mentos!\n")
elif 40 <= score <= 50:
    print(f"\nYour score is {score}, you are alright together!")
    print(f"Sua pontuação é {score}, vocês estão muito bem juntos!\n")
else: 
    print(f"\nYour score is {score}")
    print(f"Sua pontuação é {score}\n")
