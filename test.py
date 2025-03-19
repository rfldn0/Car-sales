"""
1. Test all programs before implementattion
2.
"""

class MyObject:
    def __init__(self, name):
        self.name = name
        self.items = []  # This is a list inside the object

    def add_item(self, item):
        self.items.append(item)

    def display(self):
        print(f"Object Name: {self.name}")
        print("Items:", self.items)

# Usage
obj = MyObject("Sample Object")
obj.add_item("Item 1")
obj.add_item("Item 2")
obj.display()
