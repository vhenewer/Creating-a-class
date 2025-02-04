from cat import Cat

def main():
    cats = []

    n = int(input("Enter the number of cats: "))

    for _ in range(n):
        print("\nEnter details for a new cat:")
        name = input("Name: ")
        breed = input("Breed: ")
        age = float(input("Age (in years): "))
        color = input("Color: ")
        cat = Cat(name, breed, age, color)
        cats.append(cat)

    print("\nCats Information:")
    for cat in cats:
        cat.display_info()

    if cats:
        print("\nChecking if the first cat is a kitten...")
        cats[0].is_kitten()

if __name__ == "__main__":
    main()
