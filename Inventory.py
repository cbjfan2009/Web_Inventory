from flask import Flask, render_template, url_for, request
import _sqlite3

#connection to DB
conn = _sqlite3.connect('Inventory.db')

#setup cursor object
cursor = conn.cursor()

def add_inventory_count(item_count, item_num):
    update_string = str(
    "Update WEB_INVENTORY SET InventoryCount =" + str(item_count)+
    " WHERE ITEMNUM = " + str(item_num))
    cursor.execute(update_string)
    conn.commit()

def add_item(itemNumber,prodDescrip,weight,length, width, height,count): #Item-Number, Description, Weight, Package-Length,  Package-Width, Package-Height, Inventory-Count
    item_values = (itemNumber, prodDescrip, weight, length, width, height, count)
    #sql_text = "INSERT INTO WEB_INVENTORY (ItemNum, Description, Weight, PkgL, PkgW, PkgH, InventoryCount) VALUES (" + itemNumber + ", " + prodDescrip + ", " + weight + ", " + length + ", " + width + ", " + height + ", " + count + ");"
    sql = "INSERT INTO WEB_INVENTORY (ItemNum, Description, Weight, PkgL, PkgW, PkgH, InventoryCount) VALUES (" + itemNumber + ", " + prodDescrip + ", " + weight + ", " + length + ", " + width + ", " + height + ", " + count + ")"
    cursor.execute(sql)
    conn.commit()

# flask routes setup
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def main():
    with _sqlite3.connect('Inventory.db') as con:
        cur = con.cursor()
        cur.execute('Select * FROM WEB_INVENTORY')
        data = cur.fetchall()
        return render_template('index.html', data=data) #=enumerate(data)


##############################Currently Working On This Route#####################
@app.route("/add_inventory.html", methods=['POST', 'GET'])
def add_inventory():
    if request.method == 'POST':
        itemNumber = str(request.form['itemNumber'])
        prodDescrip = str(request.form['prodDescrip'])
        weight = str(request.form['weight'])
        length = str(request.form['length'])
        height = str(request.form['height'])
        invCount = str(request.form['invCount'])
        add_item(itemNumber, prodDescrip, weight, length, height, invCount)
        return render_template(('add_inventory.html', ))

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

query = cursor.execute('Select * FROM WEB_INVENTORY WHERE InventoryCount !=0')

for row in query:
    print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])

#add_item("10101010101", "TESTING", "20","12", "12", "12", "58008")


#print("------------------------NEW QUERY------------------")

sql = "INSERT INTO Web_Inventory (ItemNum, Description, Weight, PkgL, PkgW, PkgH, InventoryCount) VALUES (0000001, 0000001, 100, 12, 12, 12, 55555)"
cursor.execute(sql)


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
