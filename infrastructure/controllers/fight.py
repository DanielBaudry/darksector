from flask import current_app as app, request, redirect, url_for
from flask_login import login_required, current_user

from infrastructure.dependencies_injections import player_attack_monster


@app.route('/attack', methods=['POST'])
@login_required
def attack_monster():
    monster_name = request.form['monster_name']
    player_attack_monster.execute(user_id=current_user.id, monster_name=monster_name)
    return redirect(url_for('enter_darksector'))


@app.route('/turn', methods=['POST'])
@login_required
def end_turn():
    player_end_turn.execute(player_id=player)
    return '', 200
