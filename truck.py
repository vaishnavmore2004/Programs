lt=int(input())
dis=int(input())

hun=(lt/dis)*100
print("Liters per 100 km is:")
print(round(hun,2))

#miles per gallon

miles=dis*0.6214
gallons=lt*0.2642
mpg=miles/gallons
print("Miles per gallon is:")
print(round(mpg,2))