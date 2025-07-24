from flask import Flask,render_template,request
import csv

app = Flask(__name__)

def load_car_data(file_path):
    cars=[]
    with open(file_path,mode="r",encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['price_Min']=int(row['price_Min'])
            row['Price_Max']=int(row['Price_Max'])
            row['seating capacity']=int(row['seating capacity'])
            cars.append(row)
    return cars

def find_cars_in_range(cars,min_budget,max_budget):
    matching_cars = []
    for car in cars:
        if not (car['Price_Max'])<min_budget or car['Price_Min']>max_budget:
            matching_cars.append(car)
    return matching_cars

@app.route('/',methods=['GET','POST'])
def index():
    cars=[]
    if request.method == 'POST':
            try:
                 min_budget=int(request.form['min_budget'])
                 max_budget=int(request.form['max_budget'])

                 if min_budget>max_budget:
                      return render_template('index.html',error="Minimum budget cannot be greater than maximum.",cars=[])
                 
                 car_list = load_car_data('car.csv')
                 cars = find_cars_in_range(car_list,min_budget,max_budget)
            except ValueError:
                 return render_template('index.html',cars=cars)
            
if __name__=='_main':
     app.run(debug=True)


    