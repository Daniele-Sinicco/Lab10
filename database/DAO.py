from database.DB_connect import DBConnect
from model.confine import Confine
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNodes(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query1 = """select *
                    from country
                    where CCode in 
                    (select distinct state1no
                    from contiguity
                    where year<=%s)"""

        cursor.execute(query1, (anno,))

        for row in cursor:
            result.append(Country(row["CCode"], row["StateAbb"], row["StateNme"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(anno, idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query1 = """select distinct state1no, state2no from contiguity where conttype = 1 and year <= %s and state1no < state2no"""

        cursor.execute(query1, (anno,))

        for row in cursor:
            result.append(Confine(idMap[row["state1no"]], idMap[row["state2no"]]))

        cursor.close()
        conn.close()
        return result