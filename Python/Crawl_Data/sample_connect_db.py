import psycopg2
from psycopg2 import Error

from datetime import datetime
import simplejson as json
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

  def insert_refer_pharmacies_data(self, pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, created_at, updated_at):
    create_data_query = """ INSERT INTO refer_pharmacies (pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, created_at, updated_at) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s); """

    self.cursor.execute(create_data_query, (pharmacy_id, pharmacy_name,
                                            pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, json.dumps(crawl_data), created_at, updated_at))
    self.conn.commit()
    print("Successfully CREATE data Refer Pharmacies PostgresQL")

  def update_refer_pharmacies_data(self, pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, updated_at):
    update_query = """ UPDATE refer_pharmacies SET pharmacy_name=%s, pharmacy_price=%s,       pharmacy_unit=%s, pharmacy_url=%s, crawl_data=%s, updated_at=%s WHERE pharmacy_id=%s and pharmacy_source=%s """

    self.cursor.execute(update_query, (pharmacy_name, pharmacy_price, pharmacy_unit,
                                       pharmacy_url, json.dumps(crawl_data), updated_at, pharmacy_id, pharmacy_source))
    self.conn.commit()
    print("Successfully UPDATE data with {} Refer Pharmacies PostgresQL".format(
        pharmacy_id))

  def insert_update_refer_pharmacies(self, pharmacy_id, pharmacy_name, pharmacy_price, pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, created_at, updated_at):
    try:
      query = """SELECT * FROM refer_pharmacies WHERE pharmacy_id=%s AND pharmacy_source=%s"""
      self.cursor.execute(query, (pharmacy_id, pharmacy_source))

      record = self.cursor.fetchone()

      if record is None:
        self.insert_refer_pharmacies_data(pharmacy_id, pharmacy_name, pharmacy_price,
                                          pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, created_at, updated_at)

      else:
        self.update_refer_pharmacies_data(pharmacy_id, pharmacy_name, pharmacy_price,
                                          pharmacy_unit, pharmacy_source, pharmacy_url, crawl_data, updated_at)
    except (Exception, psycopg2.DatabaseError) as error:
      print(" --- Error while INSERT UPDATE refer_pharmacies table", error)

    finally:
      self.close_connection()

# if __name__ == "__main__":
#   obj = ConnectionPostgresQL()
#   ConnectionPostgresQL.get_all_refer_pharmacies_query(obj)
