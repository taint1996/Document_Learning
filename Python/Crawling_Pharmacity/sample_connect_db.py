import psycopg2
from psycopg2 import Error

from datetime import datetime

class ConnectionPostgresQL:
  def __init__(self):
    self.conn = psycopg2.connect(database="refer_pharmacy_dev", user="postgres",
                    password="postgres", host="localhost", port=5432)
    self.cursor = self.conn.cursor()

  def close_connection(self):
    if self.conn:
      self.cursor.close()
      self.conn.close()
      print("PostgreSQL connection is closed")

  def get_all_refer_pharmacies_query(self):
    try:
      query = ''' SELECT * FROM refer_pharmacies; '''
      self.cursor.execute(query)

      self.conn.commit()

      records = self.cursor.fetchall()
      for row in records:
        print("Row: ", row)
      print("Successfully select all data in Refer Pharmacies PostgresQL")
    except (Exception, psycopg2.DatabaseError) as error:
      print("Error while get all refer_pharmacies table", error)

    finally:
      self.close_connection()

  def update_refer_pharmacies_with_id_and_source(self, pharmacy_id, pharmacy_source, pharmacy_name, pharmacy_price):
    try:
      query = "SELECT * FROM refer_pharmacies where pharmacy_id={} and pharmacy_source={}".format(pharmacy_id, pharmacy_source)
      self.cursor.execute(query)

      record = self.cursor.fetchone()

      if record:
        update_query = "UPDATE refer_pharmacies set pharmacy_name={}, pharmacy_price={}".format(pharmacy_name, pharmacy_price)

        self.cursor.execute(update_query)
        self.conn.commit()
        print("Successfully UPDATE data with {} Refer Pharmacies PostgresQL".format(pharmacy_id))
    except (Exception, psycopg2.DatabaseError) as error:
      print("Error while UPDATE refer_pharmacies table", error)

    finally:
      self.close_connection()

  def insert_refer_pharmacies_data(self, pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data):
    try:
      query = "SELECT * FROM refer_pharmacies where pharmacy_id={} and pharmacy_source={}".format(pharmacy_id, pharmacy_source)
      self.cursor.execute(query)

      record = self.cursor.fetchone()

      if not record:
        create_data_query = """ INSERT INTO refer_pharmacies (pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit,pharmacy_source, pharmacy_url, crawl_data) VALUES("{}, {}, {}, {}, {}, {}, {}".format(pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data)); """

        self.cursor.execute(create_data_query)
        self.conn.commit()
        print("Record inserted successfully into refer_pharmacies table")
    except (Exception, psycopg2.DatabaseError) as error:
      print("Error while INSERT INTO refer_pharmacies table", error)

    finally:
      self.close_connection()

# if __name__ == "__main__":
#   obj = ConnectionPostgresQL()
#   ConnectionPostgresQL.get_all_refer_pharmacies_query(obj)
