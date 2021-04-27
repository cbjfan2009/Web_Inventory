from flask import Flask, render_template, url_for, request, redirect
import sqlite3


def add_inventory_count(item_count, item_num):
    with sqlite3.connect('Inventory.db') as con:
        cur = con.cursor()
        update_string = "Update WEB_INVENTORY SET InventoryCount =" + str(item_count) +\
                        " WHERE ITEMNUM = " + str(item_num)
        cur.execute(update_string)
        con.commit()


def add_item(itemnumber, proddescrip, weight, length, width, height, invcount):
    with sqlite3.connect('Inventory.db') as con:
        cur = con.cursor()
        item_values = (itemnumber, proddescrip, weight, length, width, height, invcount)
        cur.execute(
            "INSERT INTO WEB_INVENTORY (ItemNum, Description, Weight, PkgL, PkgW, PkgH, InventoryCount) "
            "VALUES (?,?,?,?,?,?,?)",
            item_values)
        con.commit()


def delete_item(user_selected):
    with sqlite3.connect('Inventory.db') as con:
        cur = con.cursor()
        # takes the first element of user_selected and puts it into a tuple
        selected = (user_selected[0],)
        cur.execute(
            "DELETE FROM WEB_INVENTORY WHERE ItemNum = ?", selected)
        con.commit()


# flask routes setup
app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def main():
    with sqlite3.connect('Inventory.db') as con:
        cur = con.cursor()
        cur.execute('Select * FROM WEB_INVENTORY ORDER BY ItemNum')
        data = cur.fetchall()
        return render_template('index.html', data=data)


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
        return redirect('add_inventory.html')
    else:
        return render_template('add_inventory.html')


@app.route("/delete_inventory", methods=['POST', 'GET'])
def delete_inventory():
    with sqlite3.connect('Inventory.db') as con:
        cur = con.cursor()
        cur.execute('Select * FROM WEB_INVENTORY ORDER BY ItemNum')
        data = cur.fetchall()

    if request.method == 'POST':
        selected_item = request.form.get('inventory_select')
        # the input is a string with a tuple inside.
        # "eval" executes the code in the string and returns a tuple
        selected_item_tuple = eval(selected_item)
        delete_item(selected_item_tuple)
        return redirect('/')
    else:
        return render_template('delete_inventory.html', data=data)


@app.route("/update_specifications")
def update_specifications():
    return render_template('update_specifications.html')


@app.route("/update_inventory")
def update_inventory():
    return render_template('update_inventory.html')

if __name__ == '__main__':
    app.run(debug=True)

#conn = sqlite3.connect("Inventory.db")
#cur = conn.cursor()
#cur.execute('Select * FROM WEB_INVENTORY ORDER BY ItemNum')
#data = cur.fetchall()
#print(data)
