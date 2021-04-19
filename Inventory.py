from flask import Flask, render_template, url_for, request
import sqlite3

#connection to DB
conn = sqlite3.connect('Inventory.db')

#setup cursor object
cursor = conn.cursor()

def add_inventory_count(item_count, item_num):
    update_string = str(
    "Update WEB_INVENTORY SET InventoryCount =" + str(item_count)+
    " WHERE ITEMNUM = " + str(item_num))
    cursor.execute(update_string)
    conn.commit()

###trying to get this query to work correctly for the add_inventory html###
def add_item(itemNumber,prodDescrip,weight,length, width, height,invCount): #Item-Number, Description, Weight, Package-Length,  Package-Width, Package-Height, Inventory-Count
    item_values = (itemNumber, prodDescrip, weight, length, width, height, invCount)
    #sql_text = "INSERT INTO WEB_INVENTORY (ItemNum, Description, Weight, PkgL, PkgW, PkgH, InventoryCount) VALUES (?,?,?,?,?,?,?), item_values"
    #sql = "INSERT INTO WEB_INVENTORY (ItemNum, Description, Weight, PkgL, PkgW, PkgH, InventoryCount) VALUES (" + itemNumber + ", " + prodDescrip + ", " + weight + ", " + length + ", " + width + ", " + height + ", " + count + ")"
    cursor.execute("INSERT INTO WEB_INVENTORY (ItemNum, Description, Weight, PkgL, PkgW, PkgH, InventoryCount) VALUES (?,?,?,?,?,?,?), item_values")
    conn.commit()

# flask routes setup
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def main():
    with sqlite3.connect('Inventory.db') as con:
        cur = con.cursor()
        cur.execute('Select * FROM WEB_INVENTORY')
        data = cur.fetchall()
        return render_template('index.html', data=data)


##############################Currently Working On This Route#####################
@app.route("/add_inventory.html", methods=['POST', 'GET'])
def add_inventory():
    if request.method == 'POST':
        itemNumber = str(request.form['itemNumber'])
        prodDescrip = str(request.form['prodDescrip'])
        weight = str(request.form['weight'])
        length = str(request.form['length'])
        height = str(request.form['height'])
        width = str(request.form['width'])
        invCount = str(request.form['invCount'])
        add_item(itemNumber, prodDescrip, weight, length, height, width, invCount)
        return render_template('add_inventory.html',)

    else:
        return render_template('add_inventory.html')

@app.route("/delete_inventory.html")
def delete_inventory():
    return render_template(('delete_inventory.html'))

@app.route("/update_specifications.html")
def update_specifications():
    return render_template(('update_specifications.html'))

@app.route("/update_inventory.html")
def update_inventory():
    return render_template(('update_inventory.html'))

#query = cursor.execute('Select * FROM WEB_INVENTORY WHERE InventoryCount !=0')

#for row in query:
#    print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])

conn
item_values2 = ("10101010101", "TESTING", "20","12", "12", "12", "58008")

###this works directly...how about when i click on the webpage?!?!
cursor.execute("INSERT INTO WEB_INVENTORY (ItemNum, Description, Weight, PkgL, PkgW, PkgH, InventoryCount) VALUES (?,?,?,?,?,?,?)", item_values2)
conn.commit()
#conn.close()
#print("------------------------NEW QUERY------------------")

sql = 'Select * FROM WEB_INVENTORY WHERE InventoryCount !=0'
query2 = cursor.execute(sql)

for row in query2:
    print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])

#querytest = cursor.execute('Select * FROM WEB_INVENTORY WHERE InventoryCount !=0')
#for row in query:
#    print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])

#a = (querytest.fetchall())
#for i in a: #gets individual 'cells'
#    for sub in i:
#        print(sub)
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
