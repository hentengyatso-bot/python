#testing git push
class Manager:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def update_profile(self, name=None, email=None, phone=None):
        if name:
            self.name = name
        if email:
            self.email = email
        if phone:
            self.phone = phone
        print("Profile updated successfully!")

    def display_profile(self):
        print(f"Manager Profile:\nName: {self.name}\nEmail: {self.email}\nPhone: {self.phone}\n")

class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def update_customer(self, name=None, phone=None):
        if name:
            self.name = name
        if phone:
            self.phone = phone
        print(f"Customer {self.customer_id} updated successfully!")

    def display_customer(self):
        print(f"Customer ID: {self.customer_id}\nName: {self.name}\nPhone: {self.phone}\n")

class MenuItem:
    def __init__(self, item_id, name, category, price, ingredients):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.price = price
        self.ingredients = ingredients

    def update_item(self, name=None, category=None, price=None, ingredients=None):
        if name:
            self.name = name
        if category:
            self.category = category
        if price:
            self.price = price
        if ingredients:
            self.ingredients = ingredients
        print(f"Menu item {self.item_id} updated successfully!")

    def display_item(self):
        print(f"Item ID: {self.item_id}\nName: {self.name}\nCategory: {self.category}\nPrice: Rs{self.price}\nIngredients: {', '.join(self.ingredients)}\n")

class RestaurantManagementSystem:
    def __init__(self):
        self.customers = {}
        self.menu_items = {}
        self.manager = Manager("Tenzin Gyatso", "tenzingyatso@gmail.com", "9847704292")

    # Managing Customers
    def add_customer(self, customer_id, name, phone):
        customer = Customer(customer_id, name, phone)
        self.customers[customer_id] = customer
        print(f"Customer {customer_id} added successfully!")

    def edit_customer(self, customer_id, name=None, phone=None):
        if customer_id in self.customers:
            self.customers[customer_id].update_customer(name, phone)
        else:
            print(f"Customer {customer_id} not found!")

    def delete_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer {customer_id} deleted successfully!")
        else:
            print(f"Customer {customer_id} not found!")

    # Managing Menu Items
    def add_menu_item(self, item_id, name, category, price, ingredients):
        menu_item = MenuItem(item_id, name, category, price, ingredients)
        self.menu_items[item_id] = menu_item
        print(f"Menu item {item_id} added successfully!")

    def edit_menu_item(self, item_id, name=None, category=None, price=None, ingredients=None):
        if item_id in self.menu_items:
            self.menu_items[item_id].update_item(name, category, price, ingredients)
        else:
            print(f"Menu item {item_id} not found!")

    def delete_menu_item(self, item_id):
        if item_id in self.menu_items:
            del self.menu_items[item_id]
            print(f"Menu item {item_id} deleted successfully!")
        else:
            print(f"Menu item {item_id} not found!")

    # Viewing Ingredients Requested by Chef
    def view_ingredients_list(self):
        print("Ingredients list requested by the chef:")
        for item in self.menu_items.values():
            print(f"Menu Item: {item.name} - Ingredients: {', '.join(item.ingredients)}")

    # Update Manager Profile
    def update_manager_profile(self, name=None, email=None, phone=None):
        self.manager.update_profile(name, email, phone)

    def display_manager_profile(self):
        self.manager.display_profile()


# Simulating the Restaurant Management System
def main():
    system = RestaurantManagementSystem()

    # Manager actions
    system.display_manager_profile()
    system.update_manager_profile(name="Henten Gyatso", email="hentengyatso@gmail.com", phone="9867644125")
    system.display_manager_profile()

    # Managing Customers
    system.add_customer(1, "Hari Bahadur", "985673425")
    system.add_customer(2, "Man Maya", "9856222387")
    system.customers[1].display_customer()
    system.edit_customer(1, name="Ram",)
    system.delete_customer(2)

    # Managing Menu Items
    system.add_menu_item(101, "Jhol Momo", "Main Course", 150, ["Dough", "Tomato Pickle", "Minced meat", "Jhol"])
    system.add_menu_item(102, "Chicken Burger", "Main Course", 250, ["Bread", "Chicken Patty", "Cheese", "Mayonnaise", "Vegetables"])
    system.menu_items[101].display_item()
    system.edit_menu_item(101, price=170)
    system.delete_menu_item(102)

    # Chef's Ingredients List
    system.view_ingredients_list()

if __name__ == "__main__":
    main()
