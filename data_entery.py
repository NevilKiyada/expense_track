
from datetime import datetime

date_format ="%d-%m-%Y"
CATAGORY = {"I":"Income","E":"Expence"}


def get_date(prompt,allow_default=False):
    date_str=input(prompt)
    
    if(allow_default and not date_str):
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_str,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("invalid date yoou enetr please enter valid date in dd-mm-yyyy")
        return get_date(prompt,allow_default)
        

def get_amount():
    try:
        amount =  float(input("enter Amount: "))
        if(amount<=0):
            raise ValueError("amount must be possitive ")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()
        

def get_category():
    catagory = input("enter catagory ('I' for Incomee or 'E' for Expence:  )").upper()
    if catagory in CATAGORY:
        return CATAGORY[catagory]
    print("Please Enter valid catagory ('I' for Incomee or 'E' for Expence:  )") 
    return get_category()

def get_description():
    return input("enter Discription(optional): ")


