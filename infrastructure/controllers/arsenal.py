from flask import current_app as app, render_template, redirect, url_for, request
from flask_login import login_required, current_user

from infrastructure.dependencies_injections import get_player_details, equip_gear


@app.route('/arsenal', methods=['GET'])
@login_required
def arsenal_details():
    player = get_player_details.execute(user_id=current_user.id)
    return render_template('arsenal.html', player=player)


@app.route('/arsenal', methods=['POST'])
@login_required
def equip_selected_gear():
    player_gear_id = int(request.form.get('player_gear_id'))
    to_equip = request.form.get('to_equip') == 'True'
    equip_gear.execute(user_id=current_user.id, player_gear_id=player_gear_id, to_equip=to_equip)
    return redirect(url_for('arsenal_details'))
