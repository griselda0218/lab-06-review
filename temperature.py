tempincelsius = input("Please enter a temperature in celsius")
# print(tempincelsius)
# print(type(tempincelsius))

tempinfahrenheit = float(tempincelsius) * 1.8 + 32
# print(tempinfahrenheit)
# print(type(tempinfahrenheit))

roundedF = round(tempinfahrenheit, 2)

print(tempincelsius + " degree celsius is " + str(roundedF) + " degrees fahrenheit.")
