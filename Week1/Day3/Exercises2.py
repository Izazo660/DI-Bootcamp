#Exercise 1: What Are You Learning?

student_grades = {
    "Alice" : [88, 92, 100],
    "Bob" : [75, 78, 80],
    "Charlie" : [92, 90, 85],
    "Dana" : [83, 88, 92],
    "Eli" : [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}
total_averages_sum = 0

for name, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    student_averages[name] = round(avg, 2)
    total_averages_sum += avg
    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    else:
        letter = "F"
    student_letter_grades[name] = letter

class_average = round(total_averages_sum / len(student_grades), 2)

print("STUDENT GRADE SUMMARY REPORT")
for name in student_grades:
    print(f"Student: {name} | Average : {student_averages[name]} | Grade : {student_letter_grades[name]}")

print("-" * 36)
print(f"Class Average : {class_average}")




#Exercise 2 : Advanced Data Manipulation and Analysis

sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

for transaction in sales_data:
    transaction["total_price"] = transaction["price"] * transaction["quantity"]


product_sales = {}
for transaction in sales_data:
    product = transaction["product"]
    revenue = transaction["total_price"]
    if product in product_sales:
        product_sales[product] += revenue
    else:
        product_sales[product] = revenue


customer_spending = {}
for transaction in sales_data:
    cust_id = transaction["customer_id"]
    revenue = transaction["total_price"]
    if cust_id in customer_spending:
        customer_spending[cust_id] += revenue
    else:
        customer_spending[cust_id] = revenue


high_value_transactions = [t for t in sales_data if t["total_price"] > 500]
high_value_transactions.sort(key=lambda x: x["total_price"], reverse=True)


purchase_counts = {}
for transaction in sales_data:
    cust_id = transaction["customer_id"]
    purchase_counts[cust_id] = purchase_counts.get(cust_id, 0) + 1

loyal_customers = [cust_id for cust_id, count in purchase_counts.items() if count > 1]


product_quantities = {}
product_counts = {}

for transaction in sales_data:
    product = transaction["product"]
    product_quantities[product] = product_quantities.get(product, 0) + transaction["quantity"]
    product_counts[product] = product_counts.get(product, 0) + 1

product_averages = {}
for product in product_sales:
    product_averages[product] = round(product_sales[product] / product_counts[product], 2)

most_popular_product = max(product_quantities, key=product_quantities.get)


print("RETAIL DATA ANALYSIS REPORT")
print("\n[Task 1] Total Revenue per Product Category :")
print(product_sales)

print("\n[Task 2] Customer Spending Profiles:")
print(customer_spending)

print("\n[Task 4] Sorted High-Value Transactions (> $500):")
for t in high_value_transactions:
    print(f"Customer {t['customer_id']} bought {t['product']} for ${t['total_price']}")

print("\n[Task 5] Loyal Customers (ID):")
print(loyal_customers)

print("\n[Bonus] Average Transaction Value per Product:")
print(product_averages)

print(f"\n[Bonus] Most Popular Product (by Quantity Sold): {most_popular_product} ({product_quantities[most_popular_product]} units)")

print("\n" + "="*50)
print("MARKETING STRATEGY INSIGHTS")
print("="*50)
print(f"1. Cross-Selling & Loyalty: Customers {loyal_customers} have shown regular interest.")
print("   -> Strategy: Send targeted email rewards or subscription plans to keep them hooked.")
print(f"2. Product Power: '{most_popular_product}' is driving volume, but Laptops generate massive revenue.")
print("   -> Strategy: Use bundling (e.g., buy a Laptop, get Headphones 20% off) to increase")
print("      the average order value of high-revenue product lines.")