from flask import Flask, render_template, request, redirect, url_for
from library.setting import Setting,  VillageSetting
import time
import search_village_main
# import search_faculty_main
# import search_max_urban_points_main
# import uranai_main
# import uranai_faculty_main
from settings.constants import *
from library import common_function as cf
import settings.file_path as fp
# import tokaido_taiketsu_main

app = Flask(__name__)
title = "秘境集落探索ツール"


@app.route("/")
def index():
    """
    秘境集落探索ツール
    :return:
    """
    return render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def post():
    """
    秘境集落探索ツール結果
    :return:
    """
    if request.method == "POST":

        start = time.time()

        country = request.form["country"]
        village_pop_lower_limit = int(request.form["village_pop_lower_limit"])
        village_pop_upper_limit = int(request.form["village_pop_upper_limit"])
        village_size_lower_limit = int(request.form["village_size_lower_limit"])
        village_size_upper_limit = int(request.form["village_size_upper_limit"])
        # island_setting = request.form["island_setting"]
        # key_words = request.form["key_words"]

        setting = VillageSetting(
            country,
            village_pop_lower_limit,
            village_pop_upper_limit,
            village_size_lower_limit,
            village_size_upper_limit
            # island_setting,
            # key_words
        )

        result = search_village_main.main(setting)

        elapsed_time = time.time() - start
        print(str(elapsed_time) + "[sec]")

        return render_template("index.html", result=result, setting=setting)
    else:
        return redirect(url_for('index'))


@app.route("/mesh_map")
def get_mesh_map():
    """
    メッシュマップの中心とズームを編集して返す
    :return:
    """
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    zoom = request.args.get("zoom")
    map_file = request.args.get("map_file")

    # マップファイルの中心を編集
    new_map_file = os.path.join(fp.output_dir, "map_" + str(time.time()).replace(".", "") + ".html")
    print(new_map_file)
    cf.create_modified_map(lat, lon, zoom, map_file, new_map_file)
    # new_map_file = new_map_file.replace("\\", "/")  # バックスラッシュをスラッシュに置換
    q = int(os.stat(new_map_file).st_mtime)  # キャッシュをクリアして再読み込みするためのパラメータ

    return redirect(new_map_file + "?q=" + str(q))


# @app.route("/<faculty>")
# def index_faculty(faculty):
#     """
#     秘境施設探索ツール
#     :param faculty: 施設名
#     :return:
#     """
#     return render_template("faculty.html", faculty=faculty, faculty_ja=get_faculty_ja(faculty))


# @app.route("/<faculty>/result", methods=["GET", "POST"])
# def result_faculty(faculty):
#     """
#     秘境施設探索ツール結果
#     :param faculty: 施設名
#     :return:
#     """
#     faculty = faculty
#     region = request.form["region"]
#     island_setting = request.form["island_setting"]
#     key_words = request.form["key_words"]
#     fs = FacultySetting(region, faculty, island_setting, key_words)
#     result = search_faculty_main.main(fs)
#     return render_template("faculty.html", faculty=faculty, setting=fs, faculty_ja=get_faculty_ja(faculty), result=result)


# @app.route("/uranai")
# def uranai():
#     return render_template("uranai.html")


# @app.route("/uranai/result", methods=["GET", "POST"])
# def result_uranai():
#     result = uranai_main.main()
#     return render_template("uranai.html", result=result)


# @app.route("/<faculty>/uranai")
# def uranai_faculty(faculty):
#     return render_template("uranai_faculty.html", faculty=faculty, faculty_ja=get_faculty_ja(faculty))


# @app.route("/<faculty>/uranai/result", methods=["GET", "POST"])
# def uranai_faculty_result(faculty):
#     faculty = faculty
#     result = uranai_faculty_main.main(faculty)
#     return render_template("uranai_faculty.html", faculty=faculty, result=result, faculty_ja=get_faculty_ja(faculty))


# @app.route("/tokaido_taiketsu")
# def tokaido_taiketsu():
#     return render_template("tokaido_taiketsu.html")


# @app.route("/tokaido_taiketsu/result", methods=["GET", "POST"])
# def tokaido_taiketsu_result():
#     point1_name = request.form["point1_name"]
#     point1_latlon = request.form["point1_latlon"].split(",")
#     point1_lat = float(point1_latlon[0].strip())
#     point1_lon = float(point1_latlon[1].strip())
#     point2_name = request.form["point2_name"]
#     point2_latlon = request.form["point2_latlon"].split(",")
#     point2_lat = float(point2_latlon[0].strip())
#     point2_lon = float(point2_latlon[1].strip())
#     result = tokaido_taiketsu_main.main(point1_name, point1_lat, point1_lon, point2_name, point2_lat, point2_lon)


#     return render_template("tokaido_taiketsu.html", result=result)


# @app.route("/max_tokaido")
# def max_tokaido():
#     return render_template("max_urban_point.html")


# @app.route("/max_tokaido/result", methods=["GET", "POST"])
# def max_tokaido_result():
#     region = request.form["region"]
#     island_setting = request.form["island_setting"]
#     key_words = request.form["key_words"]
#     s = Setting(region, island_setting, key_words)
#     result = search_max_urban_points_main.main(s)
#     return render_template("max_urban_point.html", setting=s, result=result)


@app.route("/about")
def about():
    """
    秘境集落探索ツール
    :return:
    """
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
