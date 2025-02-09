import turtle

screen = turtle.Screen()

pen = turtle.Turtle()


for i in range(5):  
    pen.circle(50) 
    pen.penup()  
    pen.forward(100)  
    pen.pendown()  


turtle.done()
