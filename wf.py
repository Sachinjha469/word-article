import pandas as pd
import numpy as np
import csv
import psycopg2

conn1 = psycopg2.connect(dbname='augli4allname', user = 'RdsInstance', password = 'augli4all', host = 'augli4allinstance.c5kamoli1el6.ap-south-1.rds.amazonaws.com', port = 5432, sslmode='require')
cursor1 = conn1.cursor()

conn = psycopg2.connect(dbname='augli', user = 'augli1234', password = 'augli1234', host = 'kamal1234.c5kamoli1el6.ap-south-1.rds.amazonaws.com', port = 5432, sslmode='require')
cursor = conn.cursor()

# word='elaborate'
cursor1.execute("SELECT distinct(word),cefr_rating FROM public.magneto_vocabulary where cefr_rating>2 order by cefr_rating asc")
output=cursor1.fetchall()


cursor.execute("Select id,url from content_mainarticle where appropriate_ind=0")
result=cursor.fetchall()
print(result)
list=[]
predecessor=0
for out in output:
    # count=0
    
    word=out[0]
    cefr=out[1]

    for res in result:
        print(res[0])
        print("*******************************************************")
        cursor.execute("select para_no,para_text from content_paraarticle where article_id='"+str(res[0])+"'")
        result1=cursor.fetchall()
        for r in result1:
            print(r)
            print(r[1])
            if(r[1].find(word)!=-1):
                print("Found the word")
                print(len(r[1]))
                data={
                    'Word':[word],
                    'Article_id':[res[0]],
                    'Article_url':[res[1]],
                    'Para_no':[r[0]],
                    'cefr_rating':[cefr]
                }
                df = pd.DataFrame(data)
                df.to_csv("Word-article-mapping.csv",index=False, header = False,sep=',',mode='a+')
                print("111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
                break
        #     print("####################################################")
        # count=count+1
        # if(count>50):
        #     break
            
            
            
            
        
        
        
        
        
        # break




    # break