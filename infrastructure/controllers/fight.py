from flask import current_app as app, request, redirect, url_for
from flask_login import login_required, current_user

from infrastructure.dependencies_injections import player_attack_monster, player_end_turn, use_skill_on_monster


@app.route('/attack', methods=['POST'])
@login_required
def attack_monster():
    monster_name = request.form['monster_name']
    player_attack_monster.execute(user_id=current_user.id, monster_name=monster_name)
    return redirect(url_for('get_darksector'))


@app.route('/skill', methods=['POST'])
@login_required
def use_skill():
    skill_name = request.form['skill_name']
    monster_name = request.form['monster_name']
    use_skill_on_monster.execute(user_id=current_user.id, monster_name=monster_name, skill_name=skill_name)
    return redirect(url_for('get_darksector'))


@app.route('/turn', methods=['GET'])
@login_required
def end_turn():
    player_end_turn.execute(user_id=current_user.id)
    return redirect(url_for('get_darksector'))
