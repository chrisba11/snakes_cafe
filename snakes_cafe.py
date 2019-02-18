menu_sections = {1:'Appetizers', 2:'Entrees', 3:'Desserts', 4:'Drinks'}

menu_items = {
  1:['Nachos', 'Fried Pickles', 'Garlic Fries'],
  2:['Elk Burger', 'Teriyaki Salmon', 'Cobb Salad'],
  3:['Lavendar Ice Cream', 'Bacon Maple Bar', 'Marionberry Pie'],
  4:['Pear Mojito', 'Raspberry Mule', 'Boring Cola', 'Water']
}

customer_order = {
  menu_items[1][0]:0,
  menu_items[1][1]:0,
  menu_items[1][2]:0,
  menu_items[2][0]:0,
  menu_items[2][1]:0,
  menu_items[2][2]:0,
  menu_items[3][0]:0,
  menu_items[3][1]:0,
  menu_items[3][2]:0,
  menu_items[4][0]:0,
  menu_items[4][1]:0,
  menu_items[4][2]:0,
  menu_items[4][3]:0,
}

menu = f"""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************


{menu_sections[1]}
----------
{menu_items[1][0]}
{menu_items[1][1]}
{menu_items[1][2]}


{menu_sections[2]}
----------
{menu_items[2][0]}
{menu_items[2][1]}
{menu_items[2][2]}


{menu_sections[3]}
----------
{menu_items[3][0]}
{menu_items[3][1]}
{menu_items[3][2]}


{menu_sections[4]}
----------
{menu_items[4][0]}
{menu_items[4][1]}
{menu_items[4][2]}
{menu_items[4][3]}
"""

print(menu)

current_order = input("""
******************************************************
**          What would you like to order?           **
**                                                  **
** (type "quit" at any time to complete your order) **
******************************************************

> """)

while current_order != 'quit':
  for i in customer_order:
    if current_order == i:
      customer_order[i] += 1
      if customer_order[i] > 1:
        print(f"""
** {customer_order[i]} orders of {i} have been added to your meal **""")
      else:
        print(f"""
** {customer_order[i]} order of {i} has been added to your meal **""")
  if current_order not in customer_order:
    print(f"""
** {current_order} is not a menu item **""")
  current_order = input("""
> """)
else:
  print("""
** Thank you for your order! **
""")


