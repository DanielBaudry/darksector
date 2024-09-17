from random import randrange

from flask import current_app as app, jsonify, render_template, request

from domain.fight import Fight
from domain.monster import Monster
from domain.player import Player
from infrastructure.database.db import db_session
from infrastructure.fight_logger_in_memory import FightLoggerInMemory


@app.route('/play', methods=['GET'])
def test_view():
    return render_template('player.html')


@app.route('/monsters', methods=['GET'])
def test_view2():
    monsters = db_session.query(Monster).limit(3).all()
    if len(monsters) == 0:
        for i in range(3):
            monster = Monster(health=randrange(10, 20))
            monsters.append(monster)
            db_session.add(monster)
        db_session.commit()

    return render_template('monsters.html', monsters=monsters)


@app.route('/fight', methods=['POST'])
def test_post():
    current_fight = db_session.query(Fight).first()
    if not current_fight:
        player = db_session.query(Player).filter(Player.name == 'John').first()
        current_fight = Fight(player, db_session.query(Monster).limit(3).all())

        monsters = []
        for i in range(3):
            monster = Monster(health=randrange(10, 20))
            monsters.append(monster)
            db_session.add(monster)

        current_fight.monsters = monsters

    fight_logger = FightLoggerInMemory()
    current_fight.register(fight_logger)
    current_fight.run(int(request.json.get('monster_index')))

    db_session.add(current_fight)
    db_session.commit()

    return render_template('monsters.html', monsters=current_fight.monsters)


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
