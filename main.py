import turtle,pandas
screen=turtle.Screen()
screen.bgpic("map.gif")
screen.setup(width=800,height=400)
screen.title("octucode Map Game")
data=pandas.read_csv("coordinates.csv")
countries=data.country.to_list()
guessed=[]
while len(guessed)<22:
    answer=screen.textinput("Guess a country!","Type a country name and hit enter!")
    if answer:
        answer=answer.strip().title()
    if answer in countries:
        guessed.append(answer)

        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        country_x=data[data.country==answer]["x"].item()
        country_y=data[data.country==answer]["y"].item()
        t.goto(country_x,country_y)
        t.fillcolor("red")
        t.begin_fill()
        t.circle(16)
        t.end_fill()
        t.write(answer,font=("ariel",15))
turtle.mainloop()



