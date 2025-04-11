PETURKSBOUIPO_AGE = 16
STANLAU_AGE = 25
MAYENGUA_AGE = 48

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))

    # Define voting rules
    countries = {
        "Peturksbouipo": PETURKSBOUIPO_AGE,
        "Stanlau": STANLAU_AGE,
        "Mayengua": MAYENGUA_AGE
    }

    # Check voting eligibility
    for country, age in countries.items():
        if user_age >= age:
            print(f"You can vote in {country} where the voting age is {age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {age}.")

if __name__ == '__main__':
    main()