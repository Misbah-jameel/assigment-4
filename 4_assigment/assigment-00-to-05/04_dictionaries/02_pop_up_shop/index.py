def main():
    # Dictionary containing fruit names and their prices
    fruit_prices = {
        "apple": 2.5,
        "durian": 5.0,
        "jackfruit": 7.0,
        "kiwi": 3.0,
        "rambutan": 4.5,
        "mango": 3.5
    }
    
    total_cost = 0  # To store the total cost

    # Loop through each fruit in the dictionary
    for fruit, price in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        total_cost += price * quantity  # Add the cost for the current fruit

    print(f"Your total is ${total_cost:.2f}")

if __name__ == '__main__':
    main()
