import pandas as pd
import datetime
import smtplib
with open("confidential.txt","r") as fr:
    lines=fr.readlines()
    user=lines[0]
    password=lines[1]
def snd_mail(to,sub,msg):
    print(f"I snd this email to {to}, with the subject of {sub}, and the msg is {msg}")
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(user,password)
    s.sendmail(user,{to},f"Subject: {sub}\n\n\n{msg}")
    s.quit()

if __name__ == "__main__":
    df=pd.read_excel("mail.xlsx")
    today= datetime.datetime.now().strftime("%m-%d")
    year_now=datetime.datetime.now().strftime("%Y")
    yr_lst=[]
    for index,item in df.iterrows():
        if today==item["Birthday"].strftime("%m-%d") and year_now not in str(item["Year"]):
            snd_mail(item["Email"],"Happy Birthday",item["Dialog"])
            yr_lst.append(index)
    if yr_lst:
        for i in yr_lst:
            p_year=df.loc[i,"Year"]
            df.loc[i,"Year"]=str(p_year) +','+str(year_now)
            df.to_excel("mail.xlsx",index=False)