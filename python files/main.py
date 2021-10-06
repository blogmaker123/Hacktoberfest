import pandas as pd
import datetime
import smtplib

GMAIL_ID = "jha36binayak@gmail.com"
GMAIL_PASS = "umhuzrkqaxvamoap"
def sendEmail(to,sub,msg,link):
    print(f"Email to {to} sent with subject: {sub} and message {msg}{link}")
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(GMAIL_ID,GMAIL_PASS)
    s.sendmail(GMAIL_ID,to,f"Subject: {sub}\n\n{msg}\n {link}")
    s.quit()
    pass

if __name__ == '__main__':
    df = pd.read_excel('data.xlsx')
    # print(df)
    for index,item in df.iterrows():
        sendEmail(item['Email Address'],"Just a important information send from python :)",item['Dialogue'],item['Link'])
