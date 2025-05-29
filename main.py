import pandas as pd
import csv
from datetime import datetime
from data_entery import get_amount ,get_category,get_date,get_description

class Csv:

    FILE_CSV = 'financial_data.csv'
    COLUMNS = ['date','amount','category','description']
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



def add():
    Csv.intialize_csv()
    date=get_date("Enter Data like (dd-mm-yyyy)",allow_default=True)
    amount = get_amount()
    catagory = get_category()
    discription = get_description()
    Csv.add_data(date,amount,catagory,discription)
        
    
    
# Csv.intialize_csv()
# Csv.add_data("10-1-19",128.5,"Income","Salary")


add()

