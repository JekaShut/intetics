# intetics
Test task

# connect to DB
0. Make sure you have installed mongoDB installed "https://www.mongodb.com/dr/fastdl.mongodb.org/win32/mongodb-win32-x86_64-2008plus-ssl-3.6.2-signed.msi/download"
1. Unpack db to D:\data 
2. Open CMD in “C:\Program Files\MongoDB\Server\3.6\bin>” folder and paste : "mongod —dbpath D:\data"
3. python manage.py runserver

# or create a new DB
1. Open CMD in “C:\Program Files\MongoDB\Server\3.6\bin>” folder and paste : "mongod —dbpath D:\data"
3. Open project folder 
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver

# or use sqlite3
1. Project>settings.py
2: 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
3. python manage.py runserver
