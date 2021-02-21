import csv
from library.point import *


class VillageDAO(object):

    def __init__(self, path):
        self.path = path
        self.columns = [
            # "pref",
            # "city",
            # "district",
            "country",
            "latitude",
            "longitude",
            "population",
            "size",
            "urban_point",
            # "is_island",
            # "point_keys",
            "point_grid_ids"
        ]

        # self.pref_idx = self.columns.index("pref")
        # self.city_idx = self.columns.index("city")
        # self.district_idx = self.columns.index("district")
        self.country_idx = self.columns.index("country")
        self.lat_idx = self.columns.index("latitude")
        self.lon_idx = self.columns.index("longitude")
        self.pop_idx = self.columns.index("population")
        self.size_idx = self.columns.index("size")
        self.urban_point_idx = self.columns.index("urban_point")
        # self.is_island_idx = self.columns.index("is_island")
        # self.point_keys_idx = self.columns.index("point_keys")
        self.point_grid_ids_idx = self.columns.index("point_grid_ids")

    def make_village_data(self, villages):
        """
        集落データをcsvに書き込む
        :param villages:
        :return:
        """
        with open(self.path, "w", encoding="utf8") as f:

            writer = csv.writer(f, lineterminator="\n")

            # ヘッダ
            writer.writerow(self.columns)

            # データ
            for v in villages:

                row = []
                for _ in range(len(self.columns)):
                    row.append(None)

                # row[self.pref_idx] = v.pref
                # row[self.city_idx] = v.city
                # row[self.district_idx] = v.district
                row[self.country_idx] = v.country
                row[self.pop_idx] = v.population
                row[self.lat_idx] = v.latitude
                row[self.lon_idx] = v.longitude
                row[self.size_idx] = v.size
                row[self.urban_point_idx] = v.urban_point
                # row[self.is_island_idx] = v.is_island
                # row[self.point_keys_idx] = v.points
                row[self.point_grid_ids_idx] = v.point_grid_ids

                writer.writerow(row)

    def read_village_data(self):
        """
        集落データを読み込み、集落クラスオブジェクトのリストを返す
        :return:
        """

        villages = []
        with open(self.path, "r", encoding="utf8") as f:
            reader = csv.reader(f)
            for i, line in enumerate(reader):

                if i == 0:
                    continue

                v = Village()

                # v.pref = line[self.pref_idx]
                # v.city = line[self.city_idx]
                # v.district = line[self.district_idx]
                v.country = line[self.country_idx]
                v.population = int(line[self.pop_idx])
                v.latitude = float(line[self.lat_idx])
                v.longitude = float(line[self.lon_idx])
                v.latitude_round = round(v.latitude, LAT_LON_ROUND)
                v.longitude_round = round(v.longitude, LAT_LON_ROUND)
                v.size = int(line[self.size_idx])
                try:
                    v.urban_point = float(line[self.urban_point_idx])
                    v.urban_point_round = round(v.urban_point, URBAN_POINT_ROUND)
                except ValueError:
                    v.urban_point = -1
                    v.urban_point_round = -1
                # v.point_keys = line[self.point_keys_idx]
                v.point_grid_ids = line[self.point_grid_ids_idx]
                # if line[self.is_island_idx] == "True":
                #     v.is_island = True
                # else:
                #     v.is_island = False

                villages.append(v)

        return villages
