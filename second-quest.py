import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.bgcolor("orange")
    screen.title("Koch Сніжинка")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.penup()
    snowflake_turtle.goto(-size / 2, size / 2)
    snowflake_turtle.pendown()
    snowflake_turtle.color("black")
    snowflake_turtle.speed(0)
    snowflake_turtle.width(2)

    for _ in range(3):
        koch_snowflake(snowflake_turtle, order, size)
        snowflake_turtle.right(120)

    screen.mainloop()


if __name__ == "__main__":
    while True:
        user_input = input("Потрібно ввести величину рекурсії: ")

        try:
            recursion_depth = float(user_input)
            draw_koch_snowflake(order=recursion_depth)
            break
        except ValueError:
            print("Error: Please enter a valid number")
