import sys

# Install psycopg2-binary python driver
import psycopg2
import yaml

try:
    with open("pgsql-auth.yaml") as yamlfile:
        pgsql_auth = yaml.load(yamlfile)
    myConnection = psycopg2.connect(host="localhost", user=pgsql_auth['user'], password=pgsql_auth['password'],
                                    database=pgsql_auth['database'], port=pgsql_auth['port'])
    print("Connection to the PostgreSQL DB is sucessful")
    sys.exit(0)
except Exception as e:
    print("Connection to PGSQL DB failed", e)
    sys.exit(2)
