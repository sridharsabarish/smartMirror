import csv
import datetime


# NOTE: Remember to create meal_plan.csv and place it in the same directory
# Format : Day,Breakfast,Lunch,Dinner
class MealPlan:


    def __init__(self):
        self.meal_plan = {}
        self.generate_meal_plan(self.get_today())
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
    
    def print_meal_plan(self):
        print("Breakfast:", self.meal_plan['Breakfast'])
        print("Lunch:", self.meal_plan['Lunch'])
        print("Dinner:", self.meal_plan['Dinner'])

meal_plans= MealPlan();
meal_plans.print_meal_plan()
