import sqlite3
import pandas as pd



def DataFetch(dnum):
    cnx = sqlite3.connect('resourceDB.db')
    cursor = cnx.cursor()
    MY_SQL ="SELECT test FROM inspection WHERE claimid =?"
     
    

    df = pd.read_sql(MY_SQL, con=cnx, params=[dnum])
    return df.values[0][0]


if __name__=="__main__":
    df=DataFetch(0.1)
    print(df)