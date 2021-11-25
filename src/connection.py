import pyodbc
from extract import Extract
from timsort import TimSort


def extract_data():

    cont_page = 1

    ext_data = Extract(cont_page)

    return ext_data.get_data()


def organize_data():

    ord_data = TimSort()

    data = extract_data()

    return ord_data.tim_sort(data)


result = organize_data()
if(result is not None):
    print("Dados organizados!!")
    print(len(result))

server = '127.0.0.1, 1433'
database = 'Data_API'
username = 'SA'
password = '-....-..-..14J'


cnxn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
    server+';DATABASE='+database+';UID='+username+';PWD=' + password)
print("Conexão Bem Sucedida")

cursor = cnxn.cursor()
cont = 0

while True:

    if cont >= len(result):
        break
    query = f"""INSERT INTO datas(id, numeros)
    VALUES ({cont}, {result[cont]})"""
    print(f"Número {cont}: {result[cont]}")

    cursor.execute(query)
    cursor.commit()
    cont += 1
