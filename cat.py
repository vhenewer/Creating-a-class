class Cat:
    def __init__(self):
        self.name = None
        self.breed = None
        self.age = None
        self.color = None

    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def display_info(self):
        print(f"\nCat's Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Age: {self.age} years")
        print(f"Color: {self.color}")

    def is_kitten(self):
        if self.age < 1:
            print(f"{self.name} is a kitten!")
        else:
            print(f"{self.name} is not a kitten.")
