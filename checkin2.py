import requests,json,os

# 填入glados账号对应cookie
cookie = os.environ["COOKIE2"]


def start():    
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    referer = 'https://glados.rocks/console/checkin'
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
    print(checkin)
    print(state)

def main_handler(event, context):
  return start()

if __name__ == '__main__':
    start()
