import sys
sys.path.append("./")  # pypyで実行するためにこれが必要
import glob
from library.json_data_reader import *
from library.pop_data_reader import *
# from library.island_checker import IslandChecker
from tqdm import tqdm
import settings.file_path as fp
from library.point_dao import PopPointDAO
# from library.pop_polygon_dao import PopPolygonDAO
# import library.common_function as cf
# from library.point_container import PointContainer
# from library.setting import RegionSetting


"""
人口ポイントと小地域ポイントのjsonデータを読み込む
小地域ポイントデータをもとに、人口ポイントデータに住所を付与する
人口ポイントデータに隣接関係を付与する
人口ポイントデータをcsvに吐き出す
"""


def main():

    # ポイント・人口データ読み込み
    all_points = read_pop_data(fp.raw_pop_point_file)

    print("隣接点を登録")
    register_neighbors(all_points)

    # 人口データの作成
    dao = PopPointDAO(fp.pop_point_file)
    dao.make_pop_point_data(all_points)


def read_pop_data(pop_data):
    """
    メッシュ点のJsonデータと人口データを読み、人口つきポイントオブジェクトのリストを返す
    :param raw_mesh_json_dir:
    :param raw_pop_dir:
    :return:
    """
    print("メッシュ人口データ読み込み")
    all_points = []
    id_count = 0

    # 1次メッシュ区分ごとに処理
    # mesh_files = glob.glob(os.path.join(raw_mesh_json_dir, "*.txt"))
    # for mesh_file in tqdm(mesh_files):

    # メッシュデータ読み込み
    mpd = JsonMeshPointDataReader(pop_data)

    # # 一次メッシュコード読み込み
    # first_mesh_code = os.path.basename(mesh_file).lstrip("MESH0").rstrip(".txt")

    # 人口データ読み込み
    # pop_file = os.path.join(raw_pop_dir, "tblT000876Q" + first_mesh_code + ".txt")
    # try:
    #     prd = PopRawDataReader(pop_file)
    # except FileNotFoundError:
    #     # 人口データがなければ無視
    #     continue
    # pop_data = prd.get_data()

    # 各PointにIDを付与
    for point in mpd.get_points():
        point.id = id_count
        id_count += 1
        all_points.append(point)

    return all_points


def register_neighbors(points):
    """
    隣接点を登録する
    :param point_container:
    :return:
    """
    target_points = points.copy()
    for p in tqdm(points):
        target_points.remove(p)
        for tp in target_points:
            if p.get_is_adjacent(tp):
                p.add_neighbor(tp)
                tp.add_neighbor(p)
                if len(p.neighbors) >= 8:
                    break


if __name__ == "__main__":
    main()
