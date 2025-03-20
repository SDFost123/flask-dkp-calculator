from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Путь к папке с иконками
current_dir = os.path.dirname(os.path.abspath(__file__))
icons_dir = os.path.join(current_dir, "static", "Icons")

# Статус предметов (True - активен, False - недействителен)
item_status = {
    "benir": True,
    "weapon": False,
    "armor": False,
    "crown": False,
    "accessory": False,  # ЛС на Бижу - недействителен
    "talisman_hb": True,
    "box_1000": True,
    "box_800": True,
    "box_40000": True,
    "sa_weapon": True,  # СА на Оружие
    "sa_armor": True,   # СА на Броню
    "hardin": True      # Хардин
}

# Проверка наличия иконок
icon_files = {
    "benir": "bm_ensoul_stone_PvP_empty.png",
    "weapon": "variation_mineral_wp.png",
    "armor": "variation_mineral_am.png",
    "crown": "variation_mineral_bm.png",
    "accessory": "variation_mineral_acc.png",
    "talisman_hb": "etc_high_gem_black_i00.png",
    "box_1000": "bm_lcoin_box_i00.png",
    "box_800": "bm_sayhas_talisman_box.png",
    "box_40000": "bm_sayhas_talisman_box_40k.png",
    "sa_weapon": "aden_rune_i01.png",         # СА на Оружие
    "sa_armor": "aden_rune_am_i01.png",       # СА на Броню
    "hardin": "aden_rune_high_i01.png"        # Хардин
}

for key, icon_file in icon_files.items():
    if not os.path.exists(os.path.join(icons_dir, icon_file)):
        print(f"Ошибка: файл {icon_file} не найден в папке Icons!")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Получаем данные из формы
            benir = int(request.form.get("benir", 0)) if request.form.get("benir") and item_status["benir"] else 0
            ls_weapon = int(request.form.get("ls_weapon", 0)) if request.form.get("ls_weapon") and item_status["weapon"] else 0
            ls_armor = int(request.form.get("ls_armor", 0)) if request.form.get("ls_armor") and item_status["armor"] else 0
            ls_crown = int(request.form.get("ls_crown", 0)) if request.form.get("ls_crown") and item_status["crown"] else 0
            ls_accessory = int(request.form.get("ls_accessory", 0)) if request.form.get("ls_accessory") and item_status["accessory"] else 0
            talisman_hb = int(request.form.get("talisman_hb", 0)) if request.form.get("talisman_hb") and item_status["talisman_hb"] else 0
            box_1000 = int(request.form.get("box_1000", 0)) if request.form.get("box_1000") and item_status["box_1000"] else 0
            box_800 = int(request.form.get("box_800", 0)) if request.form.get("box_800") and item_status["box_800"] else 0
            box_40000 = int(request.form.get("box_40000", 0)) if request.form.get("box_40000") and item_status["box_40000"] else 0
            sa_weapon = int(request.form.get("sa_weapon", 0)) if request.form.get("sa_weapon") and item_status["sa_weapon"] else 0
            sa_armor = int(request.form.get("sa_armor", 0)) if request.form.get("sa_armor") and item_status["sa_armor"] else 0
            hardin = int(request.form.get("hardin", 0)) if request.form.get("hardin") and item_status["hardin"] else 0

            # Расчет ДКП
            dkp_benir = benir * 5 if item_status["benir"] else 0
            dkp_weapon = ls_weapon * 2 if item_status["weapon"] else 0
            dkp_armor = ls_armor * 3 if item_status["armor"] else 0
            dkp_crown = ls_crown * 3 if item_status["crown"] else 0
            dkp_accessory = ls_accessory * 5 if item_status["accessory"] else 0
            dkp_talisman_hb = talisman_hb * 75 if item_status["talisman_hb"] else 0
            dkp_box_1000 = box_1000 * 25 if item_status["box_1000"] else 0
            dkp_box_800 = box_800 * 20 if item_status["box_800"] else 0
            dkp_box_40000 = box_40000 * 1000 if item_status["box_40000"] else 0
            dkp_sa_weapon = sa_weapon * 2 if item_status["sa_weapon"] else 0
            dkp_sa_armor = sa_armor * 5 if item_status["sa_armor"] else 0
            dkp_hardin = hardin * 10 if item_status["hardin"] else 0

            total_dkp = (dkp_benir + dkp_weapon + dkp_armor + dkp_crown +
                         dkp_accessory + dkp_talisman_hb + dkp_box_1000 +
                         dkp_box_800 + dkp_box_40000 + dkp_sa_weapon +
                         dkp_sa_armor + dkp_hardin)

            # Результаты с количеством в скобках
            results = {
                "benir": f"Фрагменты Бенира: {dkp_benir} ДКП ({benir} шт.)",
                "weapon": f"ЛС на Оружие: {dkp_weapon} ДКП ({ls_weapon} шт.)",
                "armor": f"ЛС на Армор: {dkp_armor} ДКП ({ls_armor} шт.)",
                "crown": f"ЛС на Венец: {dkp_crown} ДКП ({ls_crown} шт.)",
                "accessory": f"ЛС на Бижу: {dkp_accessory} ДКП ({ls_accessory} шт.)",
                "talisman_hb": f"Фрагменты на Талисман ХБ: {dkp_talisman_hb} ДКП ({talisman_hb} шт.)",
                "box_1000": f"Коробки Л 1000: {dkp_box_1000} ДКП ({box_1000} шт.)",
                "box_800": f"Коробки Л 800: {dkp_box_800} ДКП ({box_800} шт.)",
                "box_40000": f"Коробки Л 40000: {dkp_box_40000} ДКП ({box_40000} шт.)",
                "sa_weapon": f"СА на Оружие: {dkp_sa_weapon} ДКП ({sa_weapon} шт.)",
                "sa_armor": f"СА на Броню: {dkp_sa_armor} ДКП ({sa_armor} шт.)",
                "hardin": f"Хардин: {dkp_hardin} ДКП ({hardin} шт.)",
                "total": f"Итого: {total_dkp} ДКП"
            }
        except ValueError:
            results = {
                "benir": "Фрагменты Бенира: 0 ДКП (0 шт.)",
                "weapon": "ЛС на Оружие: 0 ДКП (0 шт.)",
                "armor": "ЛС на Армор: 0 ДКП (0 шт.)",
                "crown": "ЛС на Венец: 0 ДКП (0 шт.)",
                "accessory": "ЛС на Бижу: 0 ДКП (0 шт.)",
                "talisman_hb": "Фрагменты на Талисман ХБ: 0 ДКП (0 шт.)",
                "box_1000": "Коробки Л 1000: 0 ДКП (0 шт.)",
                "box_800": "Коробки Л 800: 0 ДКП (0 шт.)",
                "box_40000": "Коробки Л 40000: 0 ДКП (0 шт.)",
                "sa_weapon": "СА на Оружие: 0 ДКП (0 шт.)",
                "sa_armor": "СА на Броню: 0 ДКП (0 шт.)",
                "hardin": "Хардин: 0 ДКП (0 шт.)",
                "total": "Ошибка: введите числа!"
            }
        return render_template("index.html", results=results, item_status=item_status)

    # При GET-запросе показываем пустую форму
    results = {
        "benir": "Фрагменты Бенира: 0 ДКП (0 шт.)",
        "weapon": "ЛС на Оружие: 0 ДКП (0 шт.)",
        "armor": "ЛС на Армор: 0 ДКП (0 шт.)",
        "crown": "ЛС на Венец: 0 ДКП (0 шт.)",
        "accessory": "ЛС на Бижу: 0 ДКП (0 шт.)",
        "talisman_hb": "Фрагменты на Талисман ХБ: 0 ДКП (0 шт.)",
        "box_1000": "Коробки Л 1000: 0 ДКП (0 шт.)",
        "box_800": "Коробки Л 800: 0 ДКП (0 шт.)",
        "box_40000": "Коробки Л 40000: 0 ДКП (0 шт.)",
        "sa_weapon": "СА на Оружие: 0 ДКП (0 шт.)",
        "sa_armor": "СА на Броню: 0 ДКП (0 шт.)",
        "hardin": "Хардин: 0 ДКП (0 шт.)",
        "total": "Итого: 0 ДКП"
    }
    return render_template("index.html", results=results, item_status=item_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))