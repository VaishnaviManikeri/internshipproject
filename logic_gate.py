#we use operator to take decision based on multiple conditions there are 3 logical operator and,or,not
#and gate 
time=20
speed=120
if time < 25 and speed > 110: 
    print("yes we go")

#or gate
x = 5
y = 150
if x > 3 or y < 20:
    print("nice")

#not gate
x=20
result=x<25
condition=not result
print(condition)

#if a player take more than 5m to complete the race display msg speed up using not
time_of_player=7
if not time_of_player<5:
    print("speed up")

