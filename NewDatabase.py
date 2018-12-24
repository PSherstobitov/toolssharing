import sqlite3

conn = sqlite3.connect('app.db')


c = conn.cursor()

c.execute('''
CREATE TABLE users (
           userID INTEGER PRIMARY KEY AUTOINCREMENT,
           password TEXT,
           email TEXT,
           fullname TEXT,
           userinformation TEXT,
           toolsavailable TEXT,
           toolswished TEXT
           
)
''')
conn.commit()



c.execute('''
CREATE TABLE tools (
           toolID INTEGER PRIMARY KEY AUTOINCREMENT,
           toolstatus TEXT,
           tooltype TEXT,
           ownerID INTEGER,
           FOREIGN KEY (ownerID) REFERENCES users(userID),
           
)
''')
conn.commit()



c.execute (''' 
CREATE TABLE shares ( 
    exchangeID INTEGER PRIMARY KEY AUTOINCREMENT, 
    giver INTEGER, 
    taker INTEGER, 
    tool INTEGER,  
    date_of_borrow INTEGER, 
    FOREIGN KEY (giver) REFERENCES users(userID), 
    FOREIGN KEY (tool) REFERENCES tools(toolID), 
    FOREIGN KEY (taker) REFERENCES users(userID), 

) 
''')
conn.commit()




c.execute ('''
CREATE TABLE types (
          typeID INTEGER PRIMARY KEY AUTOINCREMENT,
          typename TEXT    
)
''')
conn.commit()




users = [
      {
        'fullname': 'Svyatoslav Belyaev',
        'password': 'werwerwer',
        'email': 'xd@gmail.com',
        'userinformation': 'cool',
        'toolsavailable': 'duct tape',
        'toolswished': 'drill',
        }
]

tools = [
      {
        'toolstatus': 'New',
        'tooltype': 'Drill',
        }
]


shares = [
      {
        'giver': '0',
        'taker': '1',
        'tool': '1',
        'date_of_borrow': '22.02.2015'
        }
]



for user in users:
    c.execute("INSERT INTO users "
              "(fullname, email, password, userinformation, toolswished) "
              "VALUES "
              "('{fullname}', '{email}', '{password}','{userinformation}','{toolswished}')".format(**user))

    conn.commit()


for book in tools:
    c.execute("INSERT INTO tools "
              "(email, toolstatus, toolowner) "
              "VALUES "
              "('{email}','{toolstatus}', '{toolowner}')".format(**tool))

    conn.commit()


for exchange in shares:
    c.execute("INSERT INTO exchanges "
              "(giver, taker, tool, date_of_borrow)"
              "VALUES "
              "('{giver}','{taker}', '{tool}', {date_of_borrow}')".format(**borrow))

    conn.commit()



conn.close()
