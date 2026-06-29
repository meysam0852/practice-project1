from __future__ import annotations
import json


class Product:
    """Represent a product in the store."""

    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} (Stock: {self.stock})"


class Store:
    """Manage store products."""

    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, name: str, price: float, stock: int):
        """Add a new product or update an existing product."""
        existing_product = self.find_product(name)

        if existing_product:
            existing_product.price = price
            existing_product.stock += stock
            print(f"✅ Product updated: {existing_product}")
        else:
            product = Product(name, price, stock)
            self.products.append(product)
            print(f"✅ Product added: {product}")

    def list_products(self):
        """Print all available products."""
        if not self.products:
            print("❌ No products available.")
            return

        print("Available products:")
        for index, product in enumerate(self.products, start=1):
            print(f"[{index}] {product}")

    def find_product(self, name: str):
        """Find a product by name."""
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None


class CartItem:
    """Represent one product item inside the shopping cart."""

    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def subtotal(self):
        """Calculate subtotal price for this cart item."""
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"- {self.product.name} x{self.quantity} - ${self.subtotal():.2f}"


class Cart:
    """Manage shopping cart operations."""

    def __init__(self):
        self.items: list[CartItem] = []

    def add_to_cart(self, product: Product, quantity: int):
        """Add a product to the cart if enough stock exists."""
        if quantity <= 0:
            print("❌ Quantity must be greater than zero.")
            return

        if quantity > product.stock:
            print("❌ Not enough stock available.")
            return

        cart_item = self.find_cart_item(product.name)

        if cart_item:
            cart_item.quantity += quantity
        else:
            self.items.append(CartItem(product, quantity))

        product.stock -= quantity
        print(f"✅ Added {quantity} x {product.name} to cart.")

    def remove_from_cart(self, product_name: str):
        """Remove a product from the cart and restore its stock."""
        cart_item = self.find_cart_item(product_name)

        if not cart_item:
            print("❌ Product not found in cart.")
            return

        cart_item.product.stock += cart_item.quantity
        self.items.remove(cart_item)
        print(f"🗑️ Removed {product_name} from cart.")

    def view_cart(self):
        """Print cart items and total price."""
        if not self.items:
            print("🛒 Your cart is empty.")
            return

        print("🛒 Your cart:")
        for item in self.items:
            print(item)

        print(f"💰 Total: ${self.total_price():.2f}")

    def total_price(self) -> float:
        """Calculate total cart price."""
        total = 0.0

        for item in self.items:
            total += item.subtotal()

        return total

    def checkout(self):
        """Show final invoice and clear the cart."""
        if not self.items:
            print("❌ Your cart is empty. Add items before checkout.")
            return

        print("🧾 Final Checkout:")
        for item in self.items:
            print(item)

        print(f"💳 Total amount due: ${self.total_price():.2f}")
        print("🎉 Thank you for shopping with us!")

        self.items.clear()

    def find_cart_item(self, product_name: str):
        """Find a cart item by product name."""
        for item in self.items:
            if item.product.name.lower() == product_name.lower():
                return item
        return None


def read_positive_float(message: str):
    """Read a positive float number from user input."""
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("❌ Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid number.")


def read_positive_int(message: str):
    """Read a positive integer number from user input."""
    while True:
        try:
            value = int(input(message))
            if value <= 0:
                print("❌ Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("❌ Please enter a valid integer.")


def manager_login():
    """Check manager username and password."""
    print("--------------------------------")
    print("🔐 Store Manager Login")
    print("--------------------------------")

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("✅ Login successful! Welcome, Manager.")
        return True

    print("❌ Login failed! Please try again or return to main menu.")
    return False


def manager_portal(store: Store):
    """Handle manager actions."""
    if not manager_login():
        return

    print("--------------------------------")
    print("📦 Add Products")
    print("--------------------------------")

    while True:
        name = input("Enter product name (or 'done' to finish): ")

        if name.lower() == "done":
            print("Returning to main menu...")
            break

        price = read_positive_float("Enter product price: ")
        stock = read_positive_int("Enter product stock quantity: ")

        store.add_product(name, price, stock)


def customer_portal(store: Store, cart: Cart):
    """Handle customer actions."""
    while True:
        print("--------------------")
        print("🛍️ CUSTOMER PORTAL")
        print("--------------------")

        store.list_products()

        print("\nWhat would you like to do?")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Return to main menu")

        choice = input("Enter choice: ")

        if choice == "1":
            product_name = input("Enter product name: ")
            product = store.find_product(product_name)

            if not product:
                print("❌ Product not found.")
                continue

            quantity = read_positive_int("Enter quantity: ")
            cart.add_to_cart(product, quantity)

        elif choice == "2":
            product_name = input("Enter product name to remove: ")
            cart.remove_from_cart(product_name)

        elif choice == "3":
            cart.view_cart()

        elif choice == "4":
            cart.checkout()

        elif choice == "5":
            print("Returning to main menu...")
            break

        else:
            print("❌ Invalid choice. Please try again.")


def main():
    """Run the mini store program."""
    store = Store()
    cart = Cart()

    while True:
        print("=================================")
        print("🛍️ MINI STORE MANAGEMENT SYSTEM")
        print("=================================")
        print("👋 Welcome! Please select your role:")
        print("1. Store Manager")
        print("2. Customer")
        print("3. Exit Program")

        choice = input("Enter choice: ")

        if choice == "1":
            manager_portal(store)

        elif choice == "2":
            customer_portal(store, cart)

        elif choice == "3":
            print("👋 Goodbye! See you next time.")
            break

        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()