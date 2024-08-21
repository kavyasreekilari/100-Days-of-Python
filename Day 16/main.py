# import turtle

# from turtle import Turtle, Screen
# tommy = Turtle() # opens in new screen
# # tommy = turtle.Turtle()
# tommy.shape("turtle")
# tommy.color("green")
# print(tommy)
#
# # screen class in turtle file
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


# OBJECT ORIENTED PROGRAMMING


from prettytable import PrettyTable
table = PrettyTable()   # construct an object named table from PrettyTable class
# print(table)
table.title = "Pokemon Table"
# add columns to the table using add_column() method from PrettyTable
table.add_column("Pokemon Name", ["Pikachu", "Squitle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
# align contents of table to the left usisng align attribute in PrettyTable class
table.align = "l"
print(table)