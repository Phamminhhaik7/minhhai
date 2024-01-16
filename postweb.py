from time import sleep
import requests 

def run_thread(select):
  check=''
  while True:
    with open(select,'r') as f:
       data=f.read().replace('''
    ''','/n')
    if data!=check:
      check=data
      cookies = {
          'cf_clearance': 'gBwAJ_GqXwEN71_OwrYRuU2s4pCGsEZ2NfVpnU9fYHg-1704075328-0-2-4e07bc0c.12f6849c.d386c53c-160.0.0',
          '_gid': 'GA1.2.1489158886.1704075338',
          '_gcl_au': '1.1.732486307.1704075339',
          '_hjFirstSeen': '1',
          '_hjIncludedInSessionSample_1471681': '0',
          '_hjSession_1471681': 'eyJpZCI6ImVkMzliZDJiLTk2NmMtNDZiYi1hNDYwLTkxYTZlZDc0ZGU4OSIsImMiOjE3MDQwNzUzMzk5NDIsInMiOjAsInIiOjAsInNiIjoxfQ==',
          '_hjAbsoluteSessionInProgress': '0',
          '_fbp': 'fb.1.1704075341015.403348285',
          'token': '%7B%22access_token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJodHRwOi8vcmVzdC4wMDB3ZWJob3N0LmNvbS92MS9vYXV0aC9hY2Nlc3NfdG9rZW4iLCJpYXQiOjE3MDQwNzUzNTQsImV4cCI6MTcwNDA3ODk1NCwibmJmIjoxNzA0MDc1MzU0LCJqdGkiOiJkcjNDSGhmdTI2SVNHcDhXIiwic3ViIjoiMzU3MDQ4NDEiLCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.aNmrrs5-8crxjK6GGnHimAMOWLP4nGjbESve8BRUNW_cwePS6AGxhklhlvhccSkYr1_NuoO0wiEN6hEMrPW3WTurcuVjBa_U-1LNZyQWrmGA_9bsIEjVpGrpgGI3QTliqGuf22XJbCcdZcdaIa4KQav33UvMl2CJfa_ieYrIMcKVs3xa1FOTLiCnObxcohMbdXuE-y53eRMkTUtZZn9jRkYr4QJfrZK9LT6WQO5r7bKsUQQB8kflq9bFiqlSuzymVvNXMqZmc2joLlFuuEMBXWjCdcJl2ux7Ukc6uW-imvjeA2pVX280Tk625bPuITQ2geSkgWaSjE9gCo2v57qiHOckCfEv4u-1XPb78tlkDWrDki2J7SgRHlSYB5t3cUhtJnhsuHHXBDl_pKAThfFlyjy0ajtYOlG1mIbp6H1jnYICN6kswCTwITpxquNRxCzbkOiyHFCtPpHnjg4DUfzWx2SB0gcslCIKASx9wj80Hz_9SO6niE36JP8PJuWIJ15blRSPFC-zfAcit8Ok3wWOEEYMtkRyLfQLPPEwOMLlDKyFrjcHfmGEFPkucZcdabJibOu5lD_xYkh_xMwiIW7_nMSqQ8JpwxqG6u_PAQcjl14tDfL8QI-KoTgWbSequPYsMs9vysbAh3Ifskfr9t2Xm3bUIkoFYblXO4AKsDHMROk%22%2C%22refresh_token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJodHRwOi8vcmVzdC4wMDB3ZWJob3N0LmNvbS92MS9vYXV0aC9hY2Nlc3NfdG9rZW4iLCJpYXQiOjE3MDQwNzUzNTQsImV4cCI6MTcwNDA3ODk1NCwibmJmIjoxNzA0MDc1MzU0LCJqdGkiOiJkcjNDSGhmdTI2SVNHcDhXIiwic3ViIjoiMzU3MDQ4NDEiLCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.aNmrrs5-8crxjK6GGnHimAMOWLP4nGjbESve8BRUNW_cwePS6AGxhklhlvhccSkYr1_NuoO0wiEN6hEMrPW3WTurcuVjBa_U-1LNZyQWrmGA_9bsIEjVpGrpgGI3QTliqGuf22XJbCcdZcdaIa4KQav33UvMl2CJfa_ieYrIMcKVs3xa1FOTLiCnObxcohMbdXuE-y53eRMkTUtZZn9jRkYr4QJfrZK9LT6WQO5r7bKsUQQB8kflq9bFiqlSuzymVvNXMqZmc2joLlFuuEMBXWjCdcJl2ux7Ukc6uW-imvjeA2pVX280Tk625bPuITQ2geSkgWaSjE9gCo2v57qiHOckCfEv4u-1XPb78tlkDWrDki2J7SgRHlSYB5t3cUhtJnhsuHHXBDl_pKAThfFlyjy0ajtYOlG1mIbp6H1jnYICN6kswCTwITpxquNRxCzbkOiyHFCtPpHnjg4DUfzWx2SB0gcslCIKASx9wj80Hz_9SO6niE36JP8PJuWIJ15blRSPFC-zfAcit8Ok3wWOEEYMtkRyLfQLPPEwOMLlDKyFrjcHfmGEFPkucZcdabJibOu5lD_xYkh_xMwiIW7_nMSqQ8JpwxqG6u_PAQcjl14tDfL8QI-KoTgWbSequPYsMs9vysbAh3Ifskfr9t2Xm3bUIkoFYblXO4AKsDHMROk%22%2C%22token_type%22%3A%22bearer%22%2C%22expires_in%22%3A3600%7D',
          '_hjSessionUser_1471681': 'eyJpZCI6IjhkMWZlZjRhLTRjZWUtNWZmZC04MjY5LTQzZWVhZGUwMzJhNyIsImNyZWF0ZWQiOjE3MDQwNzUzMzk5MzMsImV4aXN0aW5nIjp0cnVlfQ==',
          '_ga': 'GA1.2.951045563.1704075338',
          '_ga_4X6HMPKXDF': 'GS1.1.1704075340.1.1.1704075394.0.0.0',
          'file_manager_session': '21a18a9bbf00f6653cc304fba05c95cb',
      }
      
      headers = {
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
          'Connection': 'keep-alive',
          'Content-Type': 'application/json;charset=UTF-8',
          # 'Cookie': 'cf_clearance=gBwAJ_GqXwEN71_OwrYRuU2s4pCGsEZ2NfVpnU9fYHg-1704075328-0-2-4e07bc0c.12f6849c.d386c53c-160.0.0; _gid=GA1.2.1489158886.1704075338; _gcl_au=1.1.732486307.1704075339; _hjFirstSeen=1; _hjIncludedInSessionSample_1471681=0; _hjSession_1471681=eyJpZCI6ImVkMzliZDJiLTk2NmMtNDZiYi1hNDYwLTkxYTZlZDc0ZGU4OSIsImMiOjE3MDQwNzUzMzk5NDIsInMiOjAsInIiOjAsInNiIjoxfQ==; _hjAbsoluteSessionInProgress=0; _fbp=fb.1.1704075341015.403348285; token=%7B%22access_token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJodHRwOi8vcmVzdC4wMDB3ZWJob3N0LmNvbS92MS9vYXV0aC9hY2Nlc3NfdG9rZW4iLCJpYXQiOjE3MDQwNzUzNTQsImV4cCI6MTcwNDA3ODk1NCwibmJmIjoxNzA0MDc1MzU0LCJqdGkiOiJkcjNDSGhmdTI2SVNHcDhXIiwic3ViIjoiMzU3MDQ4NDEiLCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.aNmrrs5-8crxjK6GGnHimAMOWLP4nGjbESve8BRUNW_cwePS6AGxhklhlvhccSkYr1_NuoO0wiEN6hEMrPW3WTurcuVjBa_U-1LNZyQWrmGA_9bsIEjVpGrpgGI3QTliqGuf22XJbCcdZcdaIa4KQav33UvMl2CJfa_ieYrIMcKVs3xa1FOTLiCnObxcohMbdXuE-y53eRMkTUtZZn9jRkYr4QJfrZK9LT6WQO5r7bKsUQQB8kflq9bFiqlSuzymVvNXMqZmc2joLlFuuEMBXWjCdcJl2ux7Ukc6uW-imvjeA2pVX280Tk625bPuITQ2geSkgWaSjE9gCo2v57qiHOckCfEv4u-1XPb78tlkDWrDki2J7SgRHlSYB5t3cUhtJnhsuHHXBDl_pKAThfFlyjy0ajtYOlG1mIbp6H1jnYICN6kswCTwITpxquNRxCzbkOiyHFCtPpHnjg4DUfzWx2SB0gcslCIKASx9wj80Hz_9SO6niE36JP8PJuWIJ15blRSPFC-zfAcit8Ok3wWOEEYMtkRyLfQLPPEwOMLlDKyFrjcHfmGEFPkucZcdabJibOu5lD_xYkh_xMwiIW7_nMSqQ8JpwxqG6u_PAQcjl14tDfL8QI-KoTgWbSequPYsMs9vysbAh3Ifskfr9t2Xm3bUIkoFYblXO4AKsDHMROk%22%2C%22refresh_token%22%3A%22eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJodHRwOi8vcmVzdC4wMDB3ZWJob3N0LmNvbS92MS9vYXV0aC9hY2Nlc3NfdG9rZW4iLCJpYXQiOjE3MDQwNzUzNTQsImV4cCI6MTcwNDA3ODk1NCwibmJmIjoxNzA0MDc1MzU0LCJqdGkiOiJkcjNDSGhmdTI2SVNHcDhXIiwic3ViIjoiMzU3MDQ4NDEiLCJwcnYiOiI4N2UwYWYxZWY5ZmQxNTgxMmZkZWM5NzE1M2ExNGUwYjA0NzU0NmFhIn0.aNmrrs5-8crxjK6GGnHimAMOWLP4nGjbESve8BRUNW_cwePS6AGxhklhlvhccSkYr1_NuoO0wiEN6hEMrPW3WTurcuVjBa_U-1LNZyQWrmGA_9bsIEjVpGrpgGI3QTliqGuf22XJbCcdZcdaIa4KQav33UvMl2CJfa_ieYrIMcKVs3xa1FOTLiCnObxcohMbdXuE-y53eRMkTUtZZn9jRkYr4QJfrZK9LT6WQO5r7bKsUQQB8kflq9bFiqlSuzymVvNXMqZmc2joLlFuuEMBXWjCdcJl2ux7Ukc6uW-imvjeA2pVX280Tk625bPuITQ2geSkgWaSjE9gCo2v57qiHOckCfEv4u-1XPb78tlkDWrDki2J7SgRHlSYB5t3cUhtJnhsuHHXBDl_pKAThfFlyjy0ajtYOlG1mIbp6H1jnYICN6kswCTwITpxquNRxCzbkOiyHFCtPpHnjg4DUfzWx2SB0gcslCIKASx9wj80Hz_9SO6niE36JP8PJuWIJ15blRSPFC-zfAcit8Ok3wWOEEYMtkRyLfQLPPEwOMLlDKyFrjcHfmGEFPkucZcdabJibOu5lD_xYkh_xMwiIW7_nMSqQ8JpwxqG6u_PAQcjl14tDfL8QI-KoTgWbSequPYsMs9vysbAh3Ifskfr9t2Xm3bUIkoFYblXO4AKsDHMROk%22%2C%22token_type%22%3A%22bearer%22%2C%22expires_in%22%3A3600%7D; _hjSessionUser_1471681=eyJpZCI6IjhkMWZlZjRhLTRjZWUtNWZmZC04MjY5LTQzZWVhZGUwMzJhNyIsImNyZWF0ZWQiOjE3MDQwNzUzMzk5MzMsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.2.951045563.1704075338; _ga_4X6HMPKXDF=GS1.1.1704075340.1.1.1704075394.0.0.0; file_manager_session=21a18a9bbf00f6653cc304fba05c95cb',
          'Origin': 'https://files.000webhost.com',
          'Referer': 'https://files.000webhost.com/',
          'Sec-Fetch-Dest': 'empty',
          'Sec-Fetch-Mode': 'cors',
          'Sec-Fetch-Site': 'same-origin',
          'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
          'X-Requested-With': 'XMLHttpRequest',
          'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
          'sec-ch-ua-mobile': '?1',
          'sec-ch-ua-platform': '"Android"',
      }
      
      params = {
          'action': 'edit',
      }
      
      json_data = {
          'action': 'edit',
          'item': '/public_html/'+select,
          'content': data  }
      
      response = requests.post('https://files.000webhost.com/handler.php', params=params, cookies=cookies, headers=headers, json=json_data)
      print(f"Đã post:{select}")
      sleep(10)
    else:
      sleep(10)
import threading




# Táº¡o hai threads
luong1 = threading.Thread(target=run_thread,args=('index.php'))
luong2 = threading.Thread(target=run_thread,args=('goblin_no_suana_4.php'))
luong3 = threading.Thread(target=run_thread,args=('styles.css'))
luong4 = threading.Thread(target=run_thread,args=('script.js'))
luong5 = threading.Thread(target=run_thread,args=('the_loai.php'))


# Báº¯t Äáº§u thá»±c thi cÃ¡c threads
luong1.start()
luong3.start()
luong4.start()
luong5.start()
luong2.start()


# Äá»£i cho cáº£ hai threads hoÃ n thÃ nh
luong1.join()
luong2.join()
luong3.join()
luong4.join()
luong5.join()

print("ChÆ°Æ¡ng trÃ¬nh chÃ­nh káº¿t thÃºc.")      
