import sample_connect_db as connect_db

if __name__ == "__main__":
  obj = connect_db.ConnectionPostgresQL()
  connect_db.ConnectionPostgresQL.get_all_refer_pharmacies_query(obj)
