import pyodbc 

server = 'tcp:instance.abcd12345.rds.amazonaws.com'
database = 'database4'
username = 'your_username'
password = 'your_password'
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

cursor = cnxn.cursor()

cursor.execute('''

                INSERT INTO TabelaDados(ID,LastName,FirstName,Address,City,Timestamp)
VALUES ('128', 'Marques', 'Maria','Av Faria Lima, 777', 'São Paulo',GETDATE());

                ''')

cnxn.commit()

cursor.execute("SELECT * FROM Database4.dbo.TabelaDados;")

row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

    
    
    
    
cursor.execute('INSERT INTO TempDados(Temperature,Timestamp) VALUES ({}, GETDATE())'.format(68.1))
