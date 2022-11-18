import requests
import urllib
import datetime
from ..Crawl import dbcon

token = 'alBi5OAo3eYx95nfmxRhoHr4FycAQPWjKa3EmRk4JIB'

def send():
    url = 'https://notify-api.line.me/api/notify'
    Date = []
    Lunch = []
    Date, Lunch = dbcon.dbGet()
    obj = {
        'day' : Date[0],
        'menu' : Lunch[0]
    }
    
    today = datetime.datetime.today().weekday()
    payload = obj['day'][today]
    print(payload)
    #response = requests.request("POST", url, data = )
    
    
    return

send()