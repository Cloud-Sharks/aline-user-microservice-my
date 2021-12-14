import sqlalchemy as db
from sqlalchemy import text
from faker import Faker

fake = Faker()

# specify db config
config = {
    'host' : 'localhost',
    'port' : 3307,
    'user' : 'user',
    'password' : 'pwd',
    'database' : 'alinedb'
}

db_user = config.get('user')
db_pwd = config.get('password')
db_host = config.get('host')
db_port = config.get('port')
db_name = config.get('database')

# specify connection string
connection_str = f'mysql+pymysql://{db_user}:{db_pwd}@{db_host}:{db_port}/{db_name}'
# connect to database
engine = db.create_engine(connection_str)
connection = engine.connect()

# optional clear table entries
clear = True
if clear:
    connection.execute(text('DELETE FROM user'))
    connection.execute(text('ALTER TABLE user AUTO_INCREMENT = 1'))

# create and insert X entries
num_entries = 10
for i in range(num_entries):
    # define values to be inserted into user table
    role = fake.word() # varchar(31)
    # id is bigInt auto-inc
    enabled = 0 # bit(1)
    password = fake.word() # varchar(255)
    username = fake.user_name() # varchar(255)
    email = fake.email() # varchar(255) nullable
    first_name = fake.first_name() # varchar(255) nullable
    last_name = fake.last_name() # varchar(255) nullable
    phone = fake.phone_number() # varchar(255) nullable
    # member_id is restricted foreign key from table 'member'

    # create and execute insert string
    user_ins = text("INSERT INTO user (role, enabled, password, username, email, first_name, last_name, phone) VALUES (:role, :enabled, :password, :username, :email, :first_name, :last_name, :phone)")
    connection.execute(user_ins, role=role, enabled=enabled, password=password, username=username, email=email, first_name=first_name, last_name=last_name, phone=phone)

