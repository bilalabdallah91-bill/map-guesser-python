import turtle
screen=turtle.Screen()
screen.setup(800,400)
screen.title("Map Game")
screen.bgpic("map.gif")
def my_function(x,y):
    
    country=screen.textinput("guseed coordoni","Enter your country")
    with open("coordinates.csv","a") as file:
        file.write(f"{country} {x},{y}\n")
    print(x,y)
turtle.onscreenclick(my_function)
screen.mainloop()
screen.exitonclick()
