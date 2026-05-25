import math

class Pagination:
    # Step 1 and 2: Implement the __init__ Method
    def __init__(self, items=None, page_size=10):
        self.items = items if items is not None else []
        self.page_size = int(page_size)
        self.current_idx = 0 
        self.total_pages = max(1, math.ceil(len(self.items) / self.page_size))

    # Step 3: Implement the get_visible_items() Method
    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # Step 4: Implement Navigation Methods
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page number {page_num} out of range (1 to {self.total_pages}).")
        self.current_idx = page_num - 1
        return self

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    # Step 5 (Bonus): Add a Custom __str__() Method
    def __str__(self):
        visible_items = self.get_visible_items()
        return "\n".join(str(item) for item in visible_items)
    
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print("Initial items:", p.get_visible_items()) 

p.next_page()
print("After next_page():", p.get_visible_items()) 

p.last_page()
print("After last_page():", p.get_visible_items()) 

p.first_page()
print("\n--- String Representation of Page 1 ---")
print(str(p))
print("-" * 40)

chained_result = p.first_page().next_page().next_page().next_page().get_visible_items()
print("Chained method output:", chained_result)

try:
    p.go_to_page(10)
except ValueError as e:
    print(f"\nCaught Expected Error (Page 10): {e}")

try:
    p.go_to_page(0)
except ValueError as e:
    print(f"Caught Expected Error (Page 0): {e}")