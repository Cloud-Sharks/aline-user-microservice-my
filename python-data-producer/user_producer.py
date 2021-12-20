import requests
from faker import Faker

def populate_user(auth, mem_ids):
    fake = Faker()
    register_url = 'http://localhost:8070/users/registration'

    user_entries = len(mem_ids)
    for i in range(user_entries):
        register_info = {
            "role" : fake.random_element(elements=('admin','member')),
            "username" : fake.user_name(),
            "password" : fake.lexify('Aa1!?????'),
            "firstName" : fake.first_name(),
            "lastName" : fake.last_name(),
            "email" : fake.email(),
            "phone" : fake.numerify('(###)-###-####'),
            "membershipId" : mem_ids[i],
            "lastFourOfSSN" : str(i+1)*4
        }
        reg_user = requests.post(register_url, json=register_info, headers=auth)
        # print(reg_user.text)

# login_info = {
#     'username' : 'adminUser',
#     'password' : 'Password*8'
# }
# login_response = requests.post('http://localhost:8070/login', json=login_info)
# bearer_token = login_response.headers['Authorization']
# auth = {'Authorization' : bearer_token}
# populate_user(auth)
