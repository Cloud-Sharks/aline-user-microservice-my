import requests
import logging
import os
from faker import Faker

def populate_user(auth, mem_ids):
    logging.basicConfig(level=logging.INFO, filename="aline_files/core-my/docker-data/aline_log.log", filemode='a', format='%(process)d - [%(levelname)s ] - %(message)s')
    fake = Faker()
    # user_url = 'http://localhost:8070/users/registration'
    user_url = f"{os.environ.get('USER_URL')}/users/registration"

    user_entries = len(mem_ids)
    for i in range(user_entries):
        user_info = {
            "role" : fake.random_element(elements=('admin','member')),
            "username" : fake.user_name(),
            "password" : fake.lexify('Aa1!?????'),
            "firstName" : fake.first_name(),
            "lastName" : fake.last_name(),
            "email" : fake.email(),
            "phone" : fake.numerify('(###)-###-####'),
            "membershipId" : mem_ids[i],
            "lastFourOfSSN" : str((i%10)+1)*4
        }
        logging.info(f'Trying to post {user_info}')
        try:
            reg_user = requests.post(user_url, json=user_info, headers=auth)
            logging.info('User posted')
        except Exception as e:
            logging.error(f'Error entering user: ', exc_info=True)

print('', end='')
