from flask import Flask, render_template, request
import csv

app = Flask(__name__)

def add_user_to_csv(details):
    filepath = "data/users.csv"
    
    # name,age,grade,institute,designation
    print(details)
    record = ','.join(details) + '\n'
    try:
        csvfile = open(filepath, 'a')
        csvfile.write(record)
        csvfile.close()
        return True
    except:
        print("Something went wrong when adding this user to the database")
        return False

@app.route('/', methods=["GET"])
def hello():
    return render_template('createUser.html')

@app.route('/add-user', methods=["POST"])
def add_user():
    val = list(request.form.values())
    print(val, type(val))
    checkpt = add_user_to_csv(val)
    return "User Added successfully" if checkpt else "Something went wrong!"

if __name__ == "__main__":
    app.run(debug=True)