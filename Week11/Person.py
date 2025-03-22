class Person:
    def __init__(self, name, age, height):
        print(f"Constructing person with params - name: {name}, age: {age}, height: {height}")
        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop = "I'm public"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __del__(self):
        print(f"{self.__name} was sent to the garbage bin automatically :(")
