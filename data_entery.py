import pandas as pd
import csv
from datetime import datetime

class csv:

    FILE_CSV = 'financial_data.csv'

    try:
        pd.read_csv(FILE_CSV)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['date','amount','category','description'])