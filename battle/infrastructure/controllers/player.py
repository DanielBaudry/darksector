from flask import current_app as app, jsonify

from domain.player import Player
from infrastructure.database.db import db_session


@app.route('/player', methods=['GET'])
def create_new_player():
    player = Player(name='John', health=100, damage=20)
    db_session.add(player)
    db_session.commit()

    player = db_session.query(Player).get(1)

    return jsonify({
        'id': player.id,
        'name': player.name,
        'health': player.health,
        'damage': player.damage,
    }), 200
