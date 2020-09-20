from flask import current_app as app, render_template, request, url_for, redirect
from flask_login import login_required, current_user

from src.infrastructure.dependencies_injections import get_player_details, create_new_player


@app.route('/player', methods=['GET'])
@login_required
def player_details():
    player = get_player_details.execute(user_id=current_user.id)
    return render_template('player.html', player=player)


@app.route('/player', methods=['POST'])
@login_required
def create_player():
    name = request.form['name']
    create_new_player.execute(user_id=current_user.id, player_name=name)
    return redirect(url_for('player_details'))
