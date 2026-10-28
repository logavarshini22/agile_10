def calculate_total(price, quantity):
    return price * quantity
def calculate_discount(total_bill, discount_percentage):
    return total_bill * (discount_percentage / 100)
def main():
    print("--- Shopping Bill Calculator ---")
    while True:
        try:
            price = float(input("Enter the item price: "))S
            if price < 0:
                print("Price cannot be negative. Please enter a valid price.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numerical value for price.")
    while True:
        try:
            quantity = int(input("Enter the item quantity: "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number for quantity.")
    while True:
        print("\n=== MENU ===")
        print("1. Calculate Total Bill")
        print("2. Add Discount Calculation")
        print("3. Exit Application")
        
        choice = input("Select an option (1-3): ").strip()
        if choice == '1':
            total = calculate_total(price, quantity)
            print(f"\nTotal Bill (Price x Quantity): {total:.2f}")
        elif choice == '2':
            total = calculate_total(price, quantity)
            while True:
                try:
                    discount_pct = float(input("Enter discount percentage (0-100): "))
                    if 0 <= discount_pct <= 100:
                        break
                    print("Discount must be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a numerical value.")
            
            discount_amount = calculate_discount(total, discount_pct)
            final_bill = total - discount_amount
            
            print(f"\n--- Bill Summary ---")
            print(f"Subtotal: {total:.2f}")
            print(f"Discount ({discount_pct}%): -{discount_amount:.2f}")
            print(f"Final Payable Amount: {final_bill:.2f}")
            
        elif choice == '3':
            print("Exiting application. Thank you!")
            break
        else:
            print("Invalid selection. Please choose a valid menu option option (1, 2, or 3).")

if __name__ == "__main__":
    main()

