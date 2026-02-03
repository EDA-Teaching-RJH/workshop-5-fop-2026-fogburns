def camel_snake(camel):
    snake = ""
    for c in camel:
        if c.isupper():
            snake+= "_" + c.lower()
        else:
            snake += c
    return snake.lstrip("_")

def main():
    camel_case = input("Input name of a variable in camel case >> ")
    snake_case = camel_snake(camel_case)
    print(snake_case)
main()