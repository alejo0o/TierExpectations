class Person:
    def __init__(self, name: str, last_name: str, age: int) -> None:
        self.name = name
        self._last_name = last_name
        self.__age = age

    def __show_full_name(self):
        print("Full name:", self.name + self._last_name)

    def show_age(self):
        print("Age:", self.__age)


if __name__ == "__main__":
    alejo = Person("Alejandro", "Vivanco", 23)
    print(alejo.name)
    #print(alejo.__age) throws AttributeError
    #alejo.__show_full_name() throws error
    alejo.show_age()
