from flask import Flask, render_template, request
import _sqlite3

#connection to DB
conn = _sqlite3.connect('Inventory.db')

#setup cursor object
cursor = conn.cursor()

def add_inventory(item_count, item_num):
    update_string = str("Update WEB_INVENTORY SET InventoryCount =" + str(item_count)+ " WHERE ITEMNUM = " + str(item_num))
    cursor.execute(update_string)
    conn.commit()



#flask routes setup
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def main():
    return render_template('main.html')



#query = cursor.execute('Select * FROM WEB_INVENTORY WHERE InventoryCount !=0')

#for row in query:
 #   print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])


#add_inventory(987654321, 9001203)
#print("------------------------NEW QUERY------------------")

#query = cursor.execute('Select * FROM WEB_INVENTORY WHERE InventoryCount !=0')
#for row in query:
#    print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])
