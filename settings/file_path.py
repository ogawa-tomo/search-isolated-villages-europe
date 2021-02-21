import os
import time


# 人口ポイントデータ読み込み
# raw_pop_point_file = os.path.join("./raw_data", "europe.geojson")
raw_pop_point_file = os.path.join("./raw_data", "europe_test_southwest.geojson")

# 境界メッシュshpデータ格納ディレクトリ
# raw_mesh_shp_dir = os.path.join("./raw_data", "mesh_shp")

# 境界jsonデータ格納ディレクトリ
# raw_mesh_json_dir = os.path.join("./input_data", "mesh_json")
# raw_mesh_json_dir = os.path.join("./input_data", "mesh_json_test")

# 境界jsonデータ（メッシュポリゴン）格納ディレクトリ
raw_mesh_json_polygon_dir = os.path.join("./input_data", "mesh_json_polygon")
# raw_mesh_json_polygon_dir = os.path.join("./input_data", "mesh_json_polygon_test")

# 人口データ格納ディレクトリ
raw_pop_dir = os.path.join("./raw_data", "population")
# raw_pop_dir = os.path.join("./raw_data", "population_test")


# 隣接点つき人口データファイル
pop_point_file = os.path.join("./input_data", "pop_points.csv")

# 集落データファイル
villages_file = os.path.join("./input_data", "villages.csv")

# アウトプットフォルダ
# output_dir = os.path.join("./tmp")
output_dir = os.path.join("./static", "output")
