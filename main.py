from operator import index
from string import Formatter
import pandas as pd
import csv
from datetime import datetime
from data_entery import get_amount ,get_category,get_date,get_description

class Csv:

    FILE_CSV = 'financial_data.csv'
    COLUMNS = ['date','amount','category','description']
    FORMAT_DATE = "%d-%m-%Y"
    @classmethod
    def intialize_csv(cls):
        try:
            pd.read_csv(cls.FILE_CSV)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.FILE_CSV,index=False)
            
            
    @classmethod
    def add_data(cls,date,amount,category,description):
        new_entry={
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        }

        with open(cls.FILE_CSV,"a",newline="")as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("entery added succesfully !! ")
        
        
    @classmethod
    def get_transection(cls,start_date,end_date):
        df = pd.read_csv(cls.FILE_CSV)
        df["date"] = pd.to_datetime(df["date"],format=Csv.FORMAT_DATE, errors='coerce') #A Pandas function that converts string (or object) values into proper datetime objects.
        start_date=datetime.strptime(start_date,Csv.FORMAT_DATE)
        end_date=datetime.strptime(end_date,Csv.FORMAT_DATE)
        
        mask = (df["date"] >= start_date ) & (df["date"]<= end_date)
        filter_datafrem = df.loc[mask]
        
        if filter_datafrem.empty:
            print(f"NO transection found in your given date range ${start_date} to ${end_date}")       
        else:
            print(f"Transection From ${start_date.strftime(Csv.FORMAT_DATE)} to ${end_date.strftime(Csv.FORMAT_DATE)} ")
            
            print(
                filter_datafrem.to_string(
                    index=False , formatters = {"date" : lambda x: x.strftime(Csv.FORMAT_DATE)} 
                    )
                )
            total_income = filter_datafrem[filter_datafrem["category"]=="Income"]["amount"].sum()
            total_expence = filter_datafrem[filter_datafrem["category"]=="Expence"]["amount"].sum()
            
            # total_saving = total_income - total_expence
            print("summary -*>")
            print(f"total Income :${total_income:.2f}")
            print(f"total Expence :${total_expence:.2f}")
            print(f"total saving  :${(total_income-total_expence):.2f}")
        return filter_datafrem

def add():
    Csv.intialize_csv()
    date=get_date("Enter Data like (dd-mm-yyyy)",allow_default=True)
    amount = get_amount()
    catagory = get_category()
    discription = get_description()
    Csv.add_data(date,amount,catagory,discription)
        
    
def main():
    while True:
        print("\n--------------Enter Your choice -------------------")
        print("1. for insert New recorde ")
        print("2. for view trasaction and summary  within  a date range ")
        print("3. for exit")
        
        choice = int(input("Enter Your choice : "))
        
        if choice == 1 :
            add()
        elif choice == 2 :
            start_date = get_date("Enter The Start date (dd-mm-yyyy)")
            end_date = get_date("Enter The End date (dd-mm-yyyy)")
            df= Csv.get_transection(start_date,end_date)
            pass
        elif choice == 3 :
            print("Exiting ...")
            break    
        else:
            print("Pease Enter valid choice 1, 2 or 3")
            

        
        
    
# Csv.intialize_csv()
# Csv.add_data("10-1-19",128.5,"Income","Salary")
# Csv.get_transection("01-01-2023","01-01-2026")

# add()

if __name__ == "__main__":
    main()
