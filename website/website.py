from flask import Flask, render_template
import sqlite3
import pathlib 

base_path = pathlib.Path.home() / r"C:\Users\Gaurav Malik\OneDrive\Documents\DAB111\DAB111_project_Group11\database"

db_name = "supermarket_sales.db"
db_path = base_path / db_name


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/features")
def features():
    return render_template("index.html") 

@app.route("/data")
def data():
    con = sqlite3.connect(db_path)
    cursor = con.cursor()
    sales = cursor.execute("SELECT * FROM sales LIMIT 10").fetchall()
    con.close()

    return render_template("data_table.html", sales = sales) # template data_table 

@app.route("/link")
def references():
    return render_template("references.html")
  
if __name__=="__main__":
    app.run(debug=True)
