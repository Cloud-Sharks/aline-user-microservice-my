import sqlalchemy as db
from sqlalchemy import text
from faker import Faker

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

def populate_applicant(conn):
    fake = Faker()
    # optional clear table entries
    clear = True
    if clear:
        conn.execute(text('DELETE FROM applicant'))
        conn.execute(text('ALTER TABLE applicant AUTO_INCREMENT = 1'))

    # create and insert X entries
    num_entries = 10
    for i in range(num_entries):
        # define values to be inserted into user table
        # id is bigInt auto-inc
        address = fake.street_name() # varchar(255)
        city = fake.city() # varchar(255)
        created_at = fake.date_time() # datetime(6) nullable
        date_of_birth = fake.date_time() # date
        drivers_license = fake.numerify('#########') # varchar(255) unique
        email = fake.email() # varchar(255) unique
        first_name = fake.first_name() # varchar(255)
        gender = fake.word() # varchar(255)
        income = fake.numerify('######') # int
        last_modified_at = fake.date_time() # datetime(6) nullable
        last_name = fake.last_name() # varchar(255)
        mailing_address = fake.street_name() # varchar(255)
        mailing_city = fake.city() # varchar(255)
        mailing_state = fake.state() # varchar(255)
        mailing_zipcode = fake.zipcode() # varchar(255)
        middle_name = fake.first_name() # varchar(255) nullable
        phone = fake.phone_number() # varchar(255) unique
        social_security = fake.numerify('###-##-####') # varchar(255) unique
        state = fake.state() # varchar(255)
        zipcode = fake.zipcode() # varchar(255)

        # create and execute insert string
        applicant_ins = text("INSERT INTO applicant (address, city, created_at, date_of_birth, drivers_license, email, first_name, gender, income, last_modified_at, last_name, mailing_address, mailing_city, mailing_state, mailing_zipcode, middle_name, phone, social_security, state, zipcode) VALUES (:address, :city, :created_at, :date_of_birth, :drivers_license, :email, :first_name, :gender, :income, :last_modified_at, :last_name, :mailing_address, :mailing_city, :mailing_state, :mailing_zipcode, :middle_name, :phone, :social_security, :state, :zipcode)")
        conn.execute(applicant_ins, address=address, city=city, created_at=created_at, date_of_birth=date_of_birth, drivers_license=drivers_license, email=email, first_name=first_name, gender=gender, income=income, last_modified_at=last_modified_at, last_name=last_name, mailing_address=mailing_address, mailing_city=mailing_city, mailing_state=mailing_state, mailing_zipcode=mailing_zipcode, middle_name=middle_name, phone=phone, social_security=social_security, state=state, zipcode=zipcode)

populate_applicant(connection)