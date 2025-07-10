# -*- coding: utf-8 -*-
"""
Created on Wed Jul  2 17:36:24 2025

@author: UserJ
"""

import csv
import webbrowser  # 網頁瀏覽器模組 
import sys

# 讀取"長照longterm_care_data.csv據點資料",存入LTCcenter串列
LongtermFile = 'longterm_care_data.csv'  # 讀取"長照longterm_care_data據點.csv"
LTCcenter = list()
with open(LongtermFile,encoding='utf-8-sig') as LtcFile:
# 讀檔時指定 utf-8-sig , 編碼會自動去除檔案開頭的 BOM。
    LTCDictReader = csv.DictReader(LtcFile)  # 讀檔建立DictReader物件 
    for row in LTCDictReader:
        LTCcenter.append(row)


# 詢問使用者,所在位置,以便回復鄰近長照機構資訊
print("☆ 我來幫助您, 查詢附近的'長照服務機構' ☆")
LocationCity = input("請輸入 您所在的縣市 : ")
LocationDist = input("請輸入 您所在的行政區或路名 : ")
print()  # 輸出空一行


# 依照輸入的"所在位置 縣市/行政區", 取出同區域中的"長照機構" (並刪除重複的機構名稱資料)
NearLTC = list()
for i in LTCcenter:
    if LocationCity in i['地址全址'] and LocationDist in i['地址全址']:
        checkdouble = 0  # 此參數, 用於確認"機構名稱"不重複! 
        for row in NearLTC:
            if row['機構名稱']==i['機構名稱']:
                checkdouble = checkdouble+1
        if checkdouble == 0:            
            NearLTC.append(i)

# 確認輸入的所在地區是否有長照機構! 
if not NearLTC:
    print("😓 很抱歉! 您的位置附近沒有長照服務機構! 😓")
    sys.exit()


# 依照"輸入位置",提供 長照機構 名稱&地址
print("☆ 靠近您的位置,有以下長照機構 ☆")
print()  # 輸出 空一行
for i in NearLTC:
    print("➔ 機構名稱 :",i['機構名稱'])
    print("   機構地址 :",i['地址全址'])
print()  # 輸出 空一行


# 詢問使用者,"希望前往的長照機構",再回覆提供"詳細資訊"&"Google地圖資訊"
print("☆ 參考以上信息, 請輸入想了解的機構名稱, 我將提供詳細資料及地圖資訊 ☆")
PreferLTC = input("想了解的機構名稱(關鍵字即可) : ")
print()  # 輸出 空一行


# 依照使用者提供的長照機構關鍵字,找出此機構完整資訊並存入"LikeLTC"串列中
LikeLTC = list()
for i in NearLTC:
    if PreferLTC in i['機構名稱']:
        # LikeLTC.append(i)
        LikeLTC=i


# 確認"輸入機構名稱"是否為"建議之長照機構"!
if not LikeLTC:
    print("😓 很抱歉! 您輸入的機構名稱有誤! 或 機構不存在! 😓")
    sys.exit()


# 輸出 使用者需要的機構的相關資訊 (機構名稱,地址,服務項目,負責人,電話,email)
# print("機構名稱 :",LikeLTC['機構名稱']," 地址 :",LikeLTC['地址全址'])
print("➔ 機構名稱 :",LikeLTC['機構名稱'])
print("   機構地址 :",LikeLTC['地址全址'])
# 列出"機構服務項目",因原始檔中,將"相同機構"的"不同服務項目" 分開列出!
print("   服務項目 :",end=" ")
for i in LTCcenter:
    if LikeLTC['機構名稱']==i['機構名稱']:
        print(i['特約服務項目'],end=" ")
print()  # 輸出 空一行
print("   負責人姓名 :",LikeLTC['機構負責人姓名']," 電話 :",LikeLTC['機構電話']," 電子郵件 :",LikeLTC['電子郵件'])
print()  # 輸出 空一行


# # 用資料裡的"經緯度位置"開啟對應地圖 (實測結果,地圖上沒有mark點!)
# lat_f = eval(LikeLTC['緯度'])
# lon_f = eval(LikeLTC['經度'])
# # 建立 Google Maps URL
# url = f"https://www.google.com/maps/@{lat_f},{lon_f},17z"  # 17z 是縮放等級
# # 開啟預設瀏覽器
# webbrowser.open(url)點!
# print(f"🔍 開啟地圖：{url}")


# 用資料裡的"機構地址"開啟對應地圖 (實測結果,地圖顯示有mark點!)
# 建立 Google Maps 搜尋網址
url2 = f"https://www.google.com/maps/search/{LikeLTC['地址全址']}"
# 開啟瀏覽器顯示地圖
webbrowser.open(url2)
print(f"✅ 已開啟 Google 地圖搜尋：{LikeLTC['地址全址']}")

