letter = "Hey my name is {} and I am from {}"
name = "Prabin"
country = "Nepal"
print(letter.format(name, country))#traditional method

print(f"Hey my name is {name} and I am from {country}.")#f-string method
print(f"Hey my name is {{name}} and I am form {{country}}")

price = 10.232333
txt = f"Price is {price:.2f} Dollars"
print(txt)

print(f"{20*2}")
