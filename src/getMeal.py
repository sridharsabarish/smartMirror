import csv
import datetime


# NOTE: Remember to create meal_plan.csv and place it in the same directory
# Format : Day,Breakfast,Lunch,Dinner
# TODO : Think how to use a .csv or database instead 
# TOdo : Think how to randomize the meals for health.
class MealPlan:
    def __init__(self):
        self.meal_plan = {}
        self.generate_meal_plan(self.get_today())
        self.print_meal_plan()
        pass
   
    def generate_meal_plan(self,day_of_week):
        
        with open('meal_plan.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Day'] == day_of_week:
                    self.meal_plan['Breakfast'] = row['Breakfast']
                    self.meal_plan['Lunch'] = row['Lunch']
                    self.meal_plan['Dinner'] = row['Dinner']
    


    def get_today(self):
        today = datetime.date.today()
        return today.strftime("%A")
    


    def return_json(self):
        import json
        return json.dumps({"Breakfast": self.meal_plan["Breakfast"], "Lunch": self.meal_plan["Lunch"], "Dinner": self.meal_plan["Dinner"]})

    def print_meal_plan(self):
        import json
        print(self.return_json())

meal_plans= MealPlan();
meal_plans.print_meal_plan()
