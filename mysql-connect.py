import sys

# Install mysql-connector-python to import this package
import mysql.connector
import yaml

try:

    with open("mysql-auth.yaml") as yamlfile:
        mysql_auth = yaml.load(yamlfile)
    # Ensure you have the credentials are valid, else connection might fail

    connection = mysql.connector.connect(host='localhost',
                                         user=mysql_auth['user'],
                                         password=mysql_auth['password'])
    if connection.is_connected():
        print("Connection to the MySQL database is sucessful")
        connection.close()
        sys.exit(0)

except Exception as e:
    print("Connection to the MySQL database failed", e)
    sys.exit(2)
