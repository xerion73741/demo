import sqlite3
import pandas as pd

DB_NAME = 'longterm_care.db'

class LongTermCareDB:
    def __init__(self, db_path=DB_NAME):
        self.db_path = db_path
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_path)
    
    def _create_table(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS longterm_care (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    latitude REAL NOT NULL,
                    longitude REAL NOT NULL
                )             
            ''')
            conn.commit()

    def insert_institution(self, name, address, lat, lng):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO longterm_care (name, address, latitude, longitude)
                VALUES (?, ?, ?, ?)
            ''', (name, address, lat, lng))
            conn.commit()

    def get_all_institutions(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM longterm_care')
            return cursor.fetchall()
        
    def find_by_city_dist(self, city, dist):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM longterm_care
                WHERE address LIKE ? AND address LIKE ?
            ''', (f'%{city}%', f'%{dist}%')) # % 萬用字元 代表任意字元任意長度
            return cursor.fetchall()
        
    def _delete_all(self):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM longterm_care')
            conn.commit()

    def public_delete_all(self):
        self._delete_all()






if __name__ == '__main__':
    ltc = LongTermCareDB()

# csvfile = 'longterm_care_data.csv'
# df = pd.read_csv(csvfile, encoding='utf-8-sig')

# csv 寫入資料庫
# # print(df.columns.tolist())
# for _, row in df.iterrows():
#     if pd.notnull(row['緯度']):
#         try:
#             ltc.insert_institution(row['機構名稱'],row['地址全址'], row['緯度'], row['經度'])
#         except Exception as e:
#             print(f"insert 失敗: {row['機構名稱']}, 錯誤訊息：{e}")
#     else:
#         print(f"跳過一筆無效資料：{row['機構名稱']}")
        

            
# 看資料庫內容
# datas = ltc.get_all_institutions()
# for data in datas:
#     print(data)

# 查看部分資料庫內容
# city = "臺中市"              
# dist = "豐原區"              
# datas = ltc.find_by_city_dist(city, dist)   
# for data in datas:
#     print(data)         

# 保存缺失值至 csv
# missing_df = df[df['緯度'].isnull() | df['經度'].isnull()]
# missing_df.to_csv('缺經緯度ltc.csv', encoding='utf-8-sig', index=False)
# print('完成缺失值csv')

#--------------------------
# 處理缺失值
# from geopy.geocoders import Nominatim
# import time

# geolocator = Nominatim(user_agent="longtermcare_app")

# def get_lat_lng(address):
#     try:
#         location = geolocator.geocode(address)
#         if location:
#             return location.latitude, location.longitude
#         else:
#             return None, None
#     except Exception as e:
#         print(f"錯誤: {e}")
#         return None, None

# # 範例
# lat, lng = get_lat_lng("臺中市豐原區圓環東路312巷3號")
# print(lat, lng)
# time.sleep(1)  # 避免被伺服器擋，休息1秒
#------------------------------