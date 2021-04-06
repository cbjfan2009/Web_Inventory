import _sqlite3

conn = _sqlite3.connect('Inventory.db')

cursor = conn.cursor()

query = cursor.execute('Select * FROM WEB_INVENTORY WHERE InventoryCount !=0')

for row in query:
    print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])
