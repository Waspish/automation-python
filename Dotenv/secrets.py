from mysql import connector as mysql
import os
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user='st-onl',
    passwd=os.getenv('DB_PASSWD'),
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor_inst = db.cursor(dictionary=True)

cursor_inst.execute('SELECT * FROM books order by id DESC LIMIT 2')
print(cursor_inst.fetchall())
