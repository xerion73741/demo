import pandas as pd
import folium
from longterm_care_db import LongTermCareDB


def create_longtermcare_map(city, dist):
    ltc_list_dict = []
    ltc_datas = LongTermCareDB().find_by_city_dist(city, dist)

    for data in ltc_datas:
        ltc_list_dict.append({
            'id': data[0],
            'name': data[1],
            'address': data[2],
            'lat': data[3],
            'lng': data[4],
        })

    if not ltc_list_dict:
        return "<p style='color:red;'>查無資料，請重新輸入</p>"
    
    center_lat = sum([item['lat'] for item in ltc_list_dict]) / len(ltc_list_dict)
    center_lng = sum([item['lng'] for item in ltc_list_dict]) / len(ltc_list_dict)
    m = folium.Map(location=[center_lat,center_lng], zoom_start=14)

    for item in ltc_list_dict:
        folium.Marker(
            location=[item['lat'],item['lng']],
            popup= folium.Popup(
                f"機構名稱: {item['name']}<br>地址: {item['address']}",
                max_width=300)
        ).add_to(m)
    

    return m._repr_html_()

if __name__ == '__main__':
    city = '高雄市'
    dist = '前金區'
    datas = create_longtermcare_map(city, dist)

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