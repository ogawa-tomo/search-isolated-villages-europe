import json
# from library.setting import RegionSetting
from tqdm import tqdm
from library.point import *
from library import common_function as cf
from settings.constants import *
from abc import ABCMeta, abstractmethod
import copy


class JsonPointDataReader(object):
    """
    geojson形式のデータを読み込む基底クラス
    """

    def __init__(self, file):
        self.file = file
        self.raw_data_set = self.get_raw_data_set()

    def get_raw_data_set(self):
        with open(self.file, "r", encoding="utf8") as f:
            data = f.read()
        data = json.loads(data)
        data = data["features"]
        return data


class JsonMeshPointDataReader(JsonPointDataReader):
    """
    geojson形式の人口メッシュデータを読み込むクラス
    """

    def __init__(self, file):
        super().__init__(file)
        self.points = []
        self.read_points()

    def read_points(self):
        """
        点の読み込み（人口のある点と海岸点）
        :return:
        """

        # print("人口点の読み込み中")
        for raw_data in self.raw_data_set:
            """
            jsonデータから全ポイントデータのリストを生成
            """

            p = PopPoint()

            data = JsonPointData(raw_data)
            p.population = data.get_population()
            if p.population is None or p.population == 0:
                # 空データは読まない
                continue
            # p.key_code = data.get_key_code()
            p.grid_id = data.get_grid_id()
            p.country = data.get_country()
            p.latitude = data.get_latitude()
            p.longitude = data.get_longitude()
            # p.first_mesh_code = self.first_mesh_code
            # p.coast = data.get_coast()

            self.points.append(p)

    def get_points(self):
        return self.points


class JsonPointData(object):
    """
    geojson形式のポイントデータを保持し、値を取り出すメソッドを提供するクラス
    """

    def __init__(self, data):
        self.data = data

    def get_grid_id(self):
        grid_id = self.data["properties"]["GRD_ID"]
        return grid_id
    
    def get_population(self):
        population = self.data["properties"]["GEOSTAT_grid_POP_1K_2011_V2_0_1_TOT_P"]
        return population
    
    def get_country(self):
        country = self.data["properties"]["GEOSTAT_grid_POP_1K_2011_V2_0_1_DATA_SRC"]
        return country

    def get_latitude(self):
        latitude = self.data["geometry"]["coordinates"][1]
        return latitude

    def get_longitude(self):
        longitude = self.data["geometry"]["coordinates"][0]
        return longitude


class NotTargetFacultyException(Exception):
    """
    対象施設でないとき吐く例外（例：小学校でない）
    """
    pass
