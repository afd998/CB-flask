import os
from flask import Flask, render_template, g
from flask import jsonify, request, session, redirect
import warnings, csv



app = Flask(__name__, template_folder="htmltemplates")
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')


@app.route("/")
def hello():

    return render_template('index.html')

@app.route("/about")
def about():
    return "<h1>About page</h1>"

@app.route("/update",methods= ['GET'])
def update():

    final_string = str(main())
    return jsonify(keke=final_string)

@app.route("/calculate",methods= ['POST'])
def calculate():

    items = request.form.getlist("x[]")
    print(items)

    the_list_of_items = []
    the_list_of_items.append("")
    the_list_of_items.extend(items) # so that the id requirement gets fufilled.
    print(the_list_of_items)

    return jsonify(str(main(the_list_of_items)))#THIS ALREADY RETURNS MAIN!!! JUST PUT ARGS IN!

@app.route("/login", methods= ['POST'])
def login():
    username= request.form['username']
    password= request.form['password']
    if username=="username" and password=="password":
        session['username'] = 'admin'
        return redirect('/dashboard')
    else:
        return render_template('index.html', message="Wrong username/password!")



@app.route("/dashboard", methods= ['GET'])
def dshboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/')



@app.route("/logout", methods= ['GET'])
def logout():
    session.pop('username', None)
    return redirect('/')


def main(input):

    print("this",input)

    #Record ID,Family Resource Center,Age,Race / Ethnicity,Gender,Primary Language,Geography,Poverty Level
    #98653,La Manzana Community Resources,0-5,Multi-racial,Female,Other,Monterey County,Below 100%
    #be able to add more than one option

    test_category = input
    #test_category = ["","La Manzana Community Resources|Live Oak Community Resources","","Multi-racial","Female","","Monterey County","Below 100%"]

    #reads in csv file then outputs data to all_data and creates categories which hold all of the categories
    with open('raw.csv') as csvfile:

        readCSV = csv.reader(csvfile, delimiter=',')
        #print(readCSV)
        temp_data = []
        for row in readCSV:
            temp_data.append(row)
        organizations = temp_data[0] #FIXME need to find a way to determine which row has categories

    all_data = temp_data[1:]
    user_category = test_category #TODO change this to the query from the webpage or something
    list_of_users = Get_Specific_People(user_category, all_data)

    print(list_of_users)
    print(len(list_of_users))
    return len(list_of_users)


def Get_Specific_People(user_category, all_data):
    for i in range(len(user_category)):
        all_data = Look_For_Category(i, user_category[i], all_data)

    return all_data


def Look_For_Category(index, category_name, data_array):
    # this is crappy code to find the categories
    '''
    names = []
    for data in data_array:
        if data[index] not in names:
            names.append(data[index])
    print(names)
    return data_array
    '''

    if category_name == "":
        return data_array

    new_array = []

    category_names = category_name.split("|")
    print(category_names)

    for data in data_array:
        if data[index] in category_names:
            new_array.append(data)

    if new_array == []:
        warnings.warn("Applying "+category_name+" does not work or exist in the index "+str(index)+ " Check spelling, or possibly ignore if there are no people that match the criteria")

    return new_array


def Get_Category_List(user_category,all_data):
    the_list = []
    for data in all_data:
        if data[0].lower() == user_category:
            the_list.append(data)
    return the_list

def Organization_Selected(user_org, organizations):
    for i in range(len(organizations)):
        print(organizations[i].lower())
        print(user_org)
        if organizations[i].lower().strip() == user_org:#strip removes beginning and ending spaces, in other languages this may not be smart because of ==
            return i

    #if not reached
    raise Exception("Not Valid ORG")

def Get_Category_Indicies(user_category_list, organizations):
    user_category_indicies = []
    for categories in user_category_list:
        user_category_indicies.append(Organization_Selected(categories, organizations))
    return user_category_indicies



if __name__ == '__main__':

app.run(debug=True)
