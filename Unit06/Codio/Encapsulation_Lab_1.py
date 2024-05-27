def main():
    journal = CoffeeJournal('coffee_journal.csv')

    while True:
        print("\nCoffee Journal")
        print("1. Add a new coffee")
        print("2. Display all coffees")
        print("3. Save and quit")

        try:
            choice = input("Enter your choice: ")
        except EOFError:
            print("\nInput not available. Exiting.")
            break

        if choice == '1':
            roaster = input("Enter the roaster: ")
            country = input("Enter the country of origin: ")
            region = input("Enter the region: ")
            stars = input("Enter the number of stars: ")
            journal.add_coffee(roaster, country, region, stars)
        elif choice == '2':
            journal.display_coffee()
        elif choice == '3':
            journal.save_coffee()
            print("Entries saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()