def main():
    # Keep product records in memory, keyed by product ID.
    products = {
        1: {"name": "Notebook", "price": 4.5, "quantity": 20},
        2: {"name": "Pen", "price": 1.25, "quantity": 50},
    }
    while True:
        # Present all four product CRUD operations and an exit option.
        print("\nProduct CRUD: 1 Add  2 View  3 Update  4 Delete  5 Exit")
        choice = input("Choose an option: ").strip()
        try:
            if choice == "1":
                product_id = int(input("Product ID: "))
                if product_id in products:
                    print("That product ID already exists.")
                    continue
                name = input("Product name: ").strip()
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                if not name or price < 0 or quantity < 0:
                    print("Enter a name and non-negative price and quantity.")
                    continue
                products[product_id] = {
                    "name": name, "price": price, "quantity": quantity
                }
                print("Product added.")
            elif choice == "2":
                for product_id, product in sorted(products.items()):
                    print(f"{product_id}: {product['name']} — ${product['price']:.2f} ({product['quantity']} in stock)")
                if not products:
                    print("No products found.")
            elif choice == "3":
                product_id = int(input("Product ID to update: "))
                if product_id not in products:
                    print("No product has that ID.")
                    continue
                name = input("New product name: ").strip()
                price = float(input("New price: "))
                quantity = int(input("New quantity: "))
                if not name or price < 0 or quantity < 0:
                    print("Enter a name and non-negative price and quantity.")
                    continue
                products[product_id] = {
                    "name": name, "price": price, "quantity": quantity
                }
                print("Product updated.")
            elif choice == "4":
                product_id = int(input("Product ID to delete: "))
                if products.pop(product_id, None) is None:
                    print("No product has that ID.")
                else:
                    print("Product deleted.")
            elif choice == "5":
                print("Goodbye.")
                break
            else:
                print("Choose a number from 1 to 5.")
        except ValueError as error:
            print(f"Invalid product input: {error}")


if __name__ == "__main__":
    main()
