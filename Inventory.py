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


# flask routes setup
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def main():
    with _sqlite3.connect('Inventory.db') as con:
        cur = con.cursor()
        cur.execute('Select * FROM WEB_INVENTORY')
        data = cur.fetchall()
        #for index, tuple in enumerate(data):
        #    element_one = tuple[0]
        #    element_two = tuple[1]
        #    element_three = tuple[2]
        #    element_four = tuple[3]
        #    element_five = tuple[4]
        #    element_six = tuple[5]
        #    element_seven = tuple[6]
        #    print(element_one, element_two, element_three, element_four, element_five, element_six, element_seven)
        # https://stackoverflow.com/a/27036691 good explanation as to why it didn't work
        return render_template('main.html', data=enumerate(data))


#query = cursor.execute('Select * FROM WEB_INVENTORY WHERE InventoryCount !=0')

#for row in query:
 #   print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])


#add_inventory(987654321, 9001203)
#print("------------------------NEW QUERY------------------")

querytest = cursor.execute('Select * FROM WEB_INVENTORY WHERE InventoryCount !=0')
#for row in query:
#    print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])

a = (querytest.fetchall())
for i in a: #gets individual 'cells'
    for sub in i:
        print(sub)
#print(a) #prints the list of tuples


#for index, tuple in enumerate(a): #gets individual 'cells'
#    for i in tuple:
#        print(i)
    #element_one = tuple[0]
    #element_two = tuple[1]
    #element_three = tuple[2]
    #element_four = tuple[3]
    #element_five = tuple[4]
    #element_six = tuple[5]
    #element_seven = tuple[6]
    #print(element_one, element_two, element_three, element_four, element_five, element_six, element_seven)
