import webbrowser

userRoad = input("What is the name of the road to the place you'd like to locate? ").split(" ")
userCity = input("What is the name of the city in which the place you'd like to locate is? ")
userProvince = input("What is the name of the province in which the place you'd like to locate is? ")

a = ""
for value in userRoad:
    a+=value
    a+="+"
print(a)

webbrowser.open("https://www.google.ca/maps/place" + "/" + a + userCity + "," + "+" +  userProvince) 
