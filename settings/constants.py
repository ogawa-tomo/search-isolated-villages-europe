import os

# 抽出する集落範囲上限
# VILLAGE_SIZE_UPPER_LIMIT = 150  # 5次メッシュ
VILLAGE_SIZE_UPPER_LIMIT = 10  # ヨーロッパ

# 隣接判定の緯度閾値
# NEIGHBOR_THRESHOLD_LAT = 0.012  # 3次メッシュ
# NEIGHBOR_THRESHOLD_LAT = 0.006  # 4次メッシュ
# NEIGHBOR_THRESHOLD_LAT = 0.003  # 5次メッシュ

# 隣接判定の経度閾値
# NEIGHBOR_THRESHOLD_LON = 0.018  # 3次メッシュ
# NEIGHBOR_THRESHOLD_LON = 0.009  # 4次メッシュ
# NEIGHBOR_THRESHOLD_LON = 0.0045  # 5次メッシュ

# 隣接判定の閾値（ヨーロッパ）
NEIGHBOR_THRESHOLD_EUROPE = 1.9

# 隣接でない閾値（ヨーロッパ）
NOT_NEIGHBOR_THRESHOLD_LON = 0.03
NOT_NEIGHBOR_THRESHOLD_LAT = 0.03

# メッシュ内にあると判定する閾値
# IS_IN_MESH_THRESHOLD_LAT = 0.0011  # 5次メッシュ
# IS_IN_MESH_THRESHOLD_LON = 0.0016  # 5次メッシュ

# 緯度1度あたりの距離（km）
# LAT_DISTANCE = 111

# 経度1度あたりの距離（km）
# https://www.wingfield.gr.jp/archives/9721
# def get_lon_distance(lat):
#     if lat > 74:
#         return 29
#     elif lat > 72:
#         return 33
#     elif lat > 70:
#         return 37
#     elif lat > 68:
#         return 40
#     elif lat > 66:
#         return 44
#     elif lat > 64:
#         return 47
#     elif lat > 62:
#         return 51
#     elif lat > 60:
#         return 54
#     elif lat > 58:
#         return 57
#     elif lat > 56:
#         return 61
#     elif lat > 54:
#         return 64
#     elif lat > 52:
#         return 67
#     elif lat > 50:
#         return 70
#     elif lat > 45:
#         return 75
#     elif lat > 40:
#         return 82
#     elif lat > 35:
#         return 88
#     elif lat > 30:
#         return 94
#     elif lat > 25:
#         return 99
#     elif lat > 20:
#         return 103
#     elif lat > 10:
#         return 108
#     else:
#         return 111


# 都会度計算時に人口に乗じる値
POP_PARAM = 1

# 都会度計算時に距離に乗じる値
DIST_PARAM = 2

# マップ出力の最大点数
OUTPUT_MAP_NUM = 1000

# 結果のページに出す集落数
OUTPUT_HTML_NUM = 1000

# 同一座標とみなす閾値
SAME_COORDINATE_THRESHOLD = 0.0001

# 緯度経度を丸める数字
LAT_LON_ROUND = 5

# 都会度を丸める数字
URBAN_POINT_ROUND = 2

# folium地図のズーム値
ZOOM_DEFAULT = 10
ZOOM_POINT = 14

ALL = "全域"
# ZENKOKU = "全国"
# ELEMENTARY_SCHOOL = "elementary_school"
# POST_OFFICE = "post_office"
# NEW_TOWN = "new_town"
# MICHINOEKI = "michinoeki"
# STATION = "station"
# ABANDONED_STATION = "abandoned_station"
# RESEARCH_INSTITUTE = "research_institute"


# 国名
def get_country_name(country):
    
    if country == "IE":
        return "アイルランド"
    elif country == "AL":
        return "アルバニア"
    elif country == "UK":
        return "イギリス"
    elif country == "IT":
        return "イタリア"
    elif country == "EE":
        return "エストニア"
    elif country == "NL":
        return "オランダ"
    elif country == "AT":
        return "オーストリア"
    elif country == "HR":
        return "クロアチア"
    elif country == "EL":
        return "ギリシャ"
    elif country == "CH":
        return "スイス"
    elif country == "SE":
        return "スウェーデン"
    elif country == "ES":
        return "スペイン"
    elif country == "SK":
        return "スロバキア"
    elif country == "SI":
        return "スロベニア"
    elif country == "CZ":
        return "チェコ"
    elif country == "DK":
        return "デンマーク"
    elif country == "DE":
        return "ドイツ"
    elif country == "NO":
        return "ノルウェー"
    elif country == "HU":
        return "ハンガリー"
    elif country == "FI":
        return "フィンランド"
    elif country == "FR":
        return "フランス"
    elif country == "BG":
        return "ブルガリア"
    elif country == "BE":
        return "ベルギー"
    elif country == "PL":
        return "ポーランド"
    elif country == "PT":
        return "ポルトガル"
    elif country == "MT":
        return "マルタ"
    elif country == "LV":
        return "ラトビア"
    elif country == "LT":
        return "リトアニア"
    elif country == "LI":
        return "リヒテンシュタイン"
    elif country == "RO":
        return "ルーマニア"
    elif country == "XK*":
        return "？？？"    
    else:
        print(country)
        raise Exception


# def get_faculty_ja(faculty):
#     if faculty == POST_OFFICE:
#         return "郵便局"
#     elif faculty == ELEMENTARY_SCHOOL:
#         return "小学校"
#     elif faculty == NEW_TOWN:
#         return "ニュータウン"
#     elif faculty == MICHINOEKI:
#         return "道の駅"
#     elif faculty == STATION:
#         return "駅"
#     elif faculty == ABANDONED_STATION:
#         return "廃駅"
#     elif faculty == RESEARCH_INSTITUTE:
#         return "研究機関"


# # 離島設定
# EXCLUDE_ISLANDS = "離島を含まない"
# INCLUDE_ISLANDS = "離島を含む"
# ONLY_ISLANDS = "離島のみ"


