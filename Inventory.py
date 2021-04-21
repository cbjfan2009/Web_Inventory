from flask import Flask, render_template, url_for, request, redirect
import sqlite3


def add_inventory_count(item_count, item_num):
    with sqlite3.connect('Inventory.db') as con:
        cur = con.cursor()
        update_string = "Update WEB_INVENTORY SET InventoryCount =" + str(item_count) +\
                        " WHERE ITEMNUM = " + str(item_num)
        cur.execute(update_string)
        con.commit()


###trying to get this query to work correctly for the add_inventory html; my cursor.execute() works when run by itself....###
# Item-Number, Description, Weight, Package-Length,  Package-Width, Package-Height, Inventory-Count
def add_item(itemnumber, proddescrip, weight, length, width, height, invcount):
    with sqlite3.connect('Inventory.db') as con:
        cur = con.cursor()
        item_values = (itemnumber, proddescrip, weight, length, width, height, invcount)
        cur.execute(
            "INSERT INTO WEB_INVENTORY (ItemNum, Description, Weight, PkgL, PkgW, PkgH, InventoryCount) VALUES (?,?,?,?,?,?,?)",
            item_values)
        con.commit()


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
@app.route("/add_inventory", methods=['POST', 'GET'])
def add_inventory():
    if request.method == 'POST':
        item_number = request.form['itemNumber']
        product_description = request.form['prodDescrip']
        weight = request.form['weight']
        length = request.form['length']
        height = request.form['height']
        width = request.form['width']
        inv_count = request.form['invCount']
        add_item(item_number, product_description, weight, length, height, width, inv_count)
        return redirect('/')
    else:
        return render_template('add_inventory.html')


@app.route("/delete_inventory.html")
def delete_inventory():
    return render_template('delete_inventory.html')


@app.route("/update_specifications.html")
def update_specifications():
    return render_template('update_specifications.html')


@app.route("/update_inventory.html")
def update_inventory():
    return render_template('update_inventory.html')

#query = cursor.execute('Select * FROM WEB_INVENTORY WHERE InventoryCount !=0')

#for row in query:
#    print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])


#item_values2 = ("10101010101", "TESTING", "20","12", "12", "12", "58008")

###this works directly...how about when i click on the webpage?!?!
#cursor.execute("INSERT INTO WEB_INVENTORY (ItemNum, Description, Weight, PkgL, PkgW, PkgH, InventoryCount) VALUES (?,?,?,?,?,?,?)", item_values2)
#conn.commit()



#print("------------------------NEW QUERY------------------")

#sql = 'Select * FROM WEB_INVENTORY WHERE InventoryCount !=0'
#query2 = cursor.execute(sql)

#for row in query2:
#    print("Item ID: ", row[0], " ", "Item Name: ", row[1], " ", "Item Inventory Count: ", row[6])

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
