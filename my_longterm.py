# html讓使用者輸入city、dist,傳出去後action 用post夾帶給/search
# 觸發flask search(), search()要用request.form.get()拿取city、dist
# 這時候呼叫longtermcare_map(.py)來製作地圖
# 這個模組要帶參數city、dist並回傳map(folium)

# 現在看到longtermcare_map
# 這裡用def創建後設定要兩個參數city、 dist
# 呼叫LongTermCareDB.find_by_city(), 就是她要吃這兩個變數

import pandas as pd
import sys
import folium

def create_longtermcare_map(LocationCity, LocationDist):
    longtermfile = 'longterm_care_data.csv'

    df = pd.read_csv(longtermfile, encoding='utf-8-sig')
    # print(df)
    # LocationCity = input('請輸入 您所在的縣市: ')
    # LocationDist = input('請輸入 您所在的行政區或路名: ')
    # print()
    filtered = df[ (df['地址全址'].str.contains(LocationCity, regex = False)) & (df['地址全址'].str.contains(LocationDist, regex = False)) ]
    result = filtered[['機構名稱', '地址全址', '經度','緯度']]
    print(result)
#     print('查詢結果: ')
#     if result.empty: 
#         # print('附近沒有長照機構')
#         return '附近沒有長照機構'

#     ltc_list_dict=[]
#     for index, row in result.iterrows():
#         print(f"機構名稱：{row['機構名稱']}")
#         print(f"地址：{row['地址全址']}")
#         print()
#         ltc_list_dict.append({
#             'name': row['機構名稱'],
#             'address': row['地址全址'],
#             'lat': row['緯度'],
#             'lng': row['經度'],
#         })

#     #print(ltc_list_dict)

#     # -------------------------------------------------------------
#     center_lat = sum([item['lat'] for item in ltc_list_dict]) / len(ltc_list_dict)
#     center_lng = sum([item['lng'] for item in ltc_list_dict]) / len(ltc_list_dict)

#     m = folium.Map(location=(center_lat, center_lng), zoom_start=14)

#     for item in ltc_list_dict:
#         folium.Marker(
#             location=[item['lat'], item['lng']],
#             popup=folium.Popup(
#                 f"機構名稱: {item['name']}<br>地址: {item['address']}",
#                 max_width=300
#             )
            
#         ).add_to(m)

#     return m

# if __name__ == '__main__':
#     # 測試用範例，直接給定測試參數
#     test_city = '123'
#     test_dist = '123'
#     result = create_longtermcare_map(test_city, test_dist)

#     if isinstance(result, str):
#         print(result)  # 輸出錯誤訊息
#     else:
#         result.save('test_map.html')  # 儲存地圖檔案方便查看
#         print('地圖已生成，請打開 test_map.html 查看')