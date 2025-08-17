import ollama
import os


model = "llama3.2"

input_file="./data/grocery_list.txt"
output_file="./data/categorized_grocery_list.txt"

if not os.path.exists(input_file):
    print(f"Input file {input_file} does not exist.") 
    exit(1)

with open(input_file, "r") as file:
    grocery_list = file.read().strip()


prompt=f"""
You are a grocery categorizer. Your task is to categorize the following grocery items into appropriate categories.
Here is the grocery list:  
{grocery_list}
Please categorize each item into one of the following categories:
- Fruits        
- Vegetables
- Dairy
- Meat
- Grains
- Snacks
- Beverages
- Frozen Foods
- Condiments
- Bakery
- Canned Goods
- Household Items
- Personal Care
-others
If an item does not fit into any of these categories, label it as "others".
2.sort the items alphabatecally into their respective categories
3.Present the categorized items in a structured format.
"""

try:
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    categorized_list = response["message"]["content"]
    print("Categorized Grocery List:")
    print(categorized_list) 
    
    with open(output_file, "w") as file:
        file.write(categorized_list)
    
    print(f"Categorized grocery list saved to {output_file}")
except Exception as e:
    print(f"An error occurred: {e}")
    exit(1)