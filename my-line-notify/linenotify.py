import requests
import datetime
import pytz


time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
time = time.strftime('%Y年%m月%d日 %H:%M:%S')

TOKEN = '0zMhjX029zTsDMaZ4fr2CbYfAVaXwdGlDNgWvDfw9Yc'
api_url = 'https://notify-api.line.me/api/notify'

send_contents = '\n' + time + '\n\n定期実行をテストしています。' 

TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}

"""requests.post(api_url,
              headers = TOKEN_dic,
              data = send_dic)"""

try:
    binary = open(self.image_file, 'rb')
    image_dic = {'imageFile': binary}

    requests.post(api_url,
                  headers = TOKEN_dic,
                  data = send_dic,
                  files = image_dic)

except (NameError,FileNotFoundError):
    
    requests.post(api_url,
                  headers = TOKEN_dic,
                  data = send_dic)