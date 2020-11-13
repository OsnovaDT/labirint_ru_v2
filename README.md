# labirint_ru_v2

First you need to create .env file in your project folder (this is where the .gitignore file is).
Then you nedd to write next parametres in this file:
1.  SECRET_KEY (your site secret key)
2.  DEBUG (True if you don't want to deploy this site on a server)
3.  DB_NAME (Name your database which will use for save data)
4.  DB_USER (User name which can use database with name in parametr DB_NAME)
5.  DB_PASSWORD (User password for database)
6.  DB_HOST (Host which you will use for database; If DEBUG = True, DB_HOST = '127.0.0.1')
7.  EMAIL_HOST_USER (Host user for send email messages)
8.  EMAIL_HOST_PASSWORD (Password for host use)
9.  SOCIAL_AUTH_VK_OAUTH2_KEY (VK key for login with VK; For get this key you nedd to create a VK application. You can do it here: https://vk.com/apps?act=manage)
10. SOCIAL_AUTH_VK_OAUTH2_SECRET (VK secret key for login vith VK)

If you don't use Pgbouncer, in settings.py in parametr DATABASES in PORT instead of 6432 set 5432

Then you need to create superuser by command 'python3 manage.py createsuperuser'.
Next you need to run server by command 'python3 manage.py runserver'.
If you use Windows, instead of 'python3' you need to use 'python'.

Then transfer on 'http://127.0.0.1:8000/admin', login and fill data.

After this transfer on 'http://127.0.0.1:8000/index' and enjoy!
