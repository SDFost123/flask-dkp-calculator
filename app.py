from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Путь к папке с иконками
current_dir = os.path.dirname(os.path.abspath(__file__))
icons_dir = os.path.join(current_dir, "static", "Icons")

# Проверка наличия иконок
icon_files = {
    "benir": "bm_ensoul_stone_PvP_empty.png",
    "weapon": "variation_mineral_wp.png",
    "armor": "variation_mineral_am.png",
    "crown": "variation_mineral_bm.png"
}

for key, icon_file in icon_files.items():
    if not os.path.exists(os.path.join(icons_dir, icon_file)):
        print(f"Ошибка: файл {icon_file} не найден в папке Icons!")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Получаем данные из формы
            benir = int(request.form.get("benir", 0)) if request.form.get("benir") else 0
            ls_weapon = int(request.form.get("ls_weapon", 0)) if request.form.get("ls_weapon") else 0
            ls_armor = int(request.form.get("ls_armor", 0)) if request.form.get("ls_armor") else 0
            ls_crown = int(request.form.get("ls_crown", 0)) if request.form.get("ls_crown") else 0

            # Расчет ДКП
            dkp_benir = benir * 5
            dkp_weapon = ls_weapon * 2
            dkp_armor = ls_armor * 5
            dkp_crown = ls_crown * 3
            total_dkp = dkp_benir + dkp_weapon + dkp_armor + dkp_crown

            # Результаты с количеством в скобках
            results = {
                "benir": f"Фрагменты бенира: {dkp_benir} ДКП ({benir} шт.)",
                "weapon": f"ЛС на оружие: {dkp_weapon} ДКП ({ls_weapon} шт.)",
                "armor": f"ЛС на армор: {dkp_armor} ДКП ({ls_armor} шт.)",
                "crown": f"ЛС на венец: {dkp_crown} ДКП ({ls_crown} шт.)",
                "total": f"Итого: {total_dkp} ДКП"
            }
        except ValueError:
            results = {
                "benir": "Фрагменты бенира: 0 ДКП (0 шт.)",
                "weapon": "ЛС на оружие: 0 ДКП (0 шт.)",
                "armor": "ЛС на армор: 0 ДКП (0 шт.)",
                "crown": "ЛС на венец: 0 ДКП (0 шт.)",
                "total": "Ошибка: введите числа!"
            }
        return render_template("index.html", results=results)

    # При GET-запросе показываем пустую форму
    results = {
        "benir": "Фрагменты бенира: 0 ДКП (0 шт.)",
        "weapon": "ЛС на оружие: 0 ДКП (0 шт.)",
        "armor": "ЛС на армор: 0 ДКП (0 шт.)",
        "crown": "ЛС на венец: 0 ДКП (0 шт.)",
        "total": "Итого: 0 ДКП"
    }
    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))