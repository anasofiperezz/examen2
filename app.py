from flask import Flask, render_template, jsonify, abort, request
from flask import Flask, jsonify, abort, request

app = Flask(__name__)


uri = '/api/games'
games = [
    {
        'id': 1,
        'titulo': 'Super Smash Bros',
        'desarrollador': 'Nintendo',
        'fecha_lanzamiento': '2018',
        'plataforma': 'Nintendo entertainment',
        'clasificacion': 'E (Everyone)',
        'imagen': 'https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000012332/ac4d1fc9824876ce756406f0525d50c57ded4b2a666f6dfe40a6ac5c3563fad9',
    },
    {
        'id': 2,
        'titulo': 'Mario Kart 8',
        'desarrollador': 'Nintendo',
        'fecha_lanzamiento': '2017',
        'plataforma': 'Nintendo entertainment',
        'clasificacion': 'E (Everyone)',
        'imagen': 'https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000000153/de697f487a36d802dd9a5ff0341f717c8486221f2f1219b675af37aca63bc453',
    },
    {
        'id': 3,
        'titulo': 'Resident evil',
        'desarrollador': 'PlayStation',
        'fecha_lanzamiento': '2023',
        'plataforma': 'PlayStation entertainment',
        'clasificacion': 'E (Everyone)',
        'imagen': 'https://img.youtube.com/vi/XrgTFWJHUWI/maxresdefault.jpg',
    },
    {
        'id': 4,
        'titulo': 'Minecraft',
        'desarrollador': 'Mojang Studios',
        'fecha_lanzamiento': '2011',
        'plataforma': 'Mojang Studios',
        'clasificacion': 'E (Everyone)',
        'imagen': 'https://assets.nintendo.com/image/upload/ar_16:9,c_lpad,w_1240/b_white/f_auto/q_auto/ncom/software/switch/70010000000964/811461b8d1cacf1f2da791b478dccfe2a55457780364c3d5a95fbfcdd4c3086f',
    },
    {
        'id': 5,
        'titulo': 'Fornite',
        'desarrollador': 'EpicGames',
        'fecha_lanzamiento': '2017',
        'plataforma': 'Game engine',
        'clasificacion': 'E (Everyone)',
        'imagen': 'https://cdn1.epicgames.com/offer/fn/24BR_S24_EGS_Launcher_Blade_2560x1440_2560x1440-437d0424d02f5fd286ab659ddade30db?h=270&quality=medium&resize=1&w=480',
    },
]


@app.route("/")
def games():
    return jsonify({'message': 'Bienvenido al servidor de la API', 'games': games})


@app.route(uri+'/<int:id>', methods=['GET'])
def get_game(id):
    this_game = [game for game in games if game['id'] == id]
    if len(this_game) == 0:
        abort(404)
    return jsonify({'game': this_game[0]})


@app.route(uri, methods=['POST'])
def create_task():
    if request.json:
        task = {
            'id': len(task)+1,
            'name': request.json('name'),
            'status': False
        }
        task.append(task)
        return jsonify({'tasks': games}), 201
    else:
        abort(404)


@app.route(uri+'/<int:id>', methods=['PUT'])
def update_task(id):
    if request.json:
        this_task = [task for task in games if task['id'] == id]
        if this_task:
            if request.json:
                if request.json.get['name']:
                    this_task[0]['name'] = request.jason['name']
                if request.json.get['status']:
                    this_task[0]['status'] = request.jason['status']
                return jsonify({'task': this_task[0]}), 201
        else:
            abort(404)
    else:
        abort(404)


@app.route(uri+'/<int:id>', methods=['DELETE'])
def delete_task(id):
    this_task = [task for task in games if task['id'] == id]
    if this_task:
        games.remove(this_task[0])
        return jsonify({'tasks': games})
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
