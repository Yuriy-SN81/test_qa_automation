import pymssql


# from AT_project.Library_create_preliminary_offer import *

def test_db():
    server = 'AG-CLUSTER02.DEVTEST.LOCAL'
    user = 'btcs223'
    password = 'btcs223'

    try:

        conn = pymssql.connect(server, user, password, "223-trunk-oos223fl")
        cursor = conn.cursor()

        SQL_QUERY = """
        SELECT TOP(1) * FROM OutgoingSaga order by id desc ;
        """

        cursor.execute(SQL_QUERY)

        records = cursor.fetchall()
        for r in records:
            print(
                f"Id: '{r[0]}', RowVersion: '{r[1]}', CreationDate: '{r[2]}', ErrorMessage: '{r[3]}', ExternalObjectId: '{r[12]}' \t")

        print('successfully connected...')

        cursor.close()
        conn.close()

    except Exception as ex:
        print('Connection refused...')
        print(ex)

