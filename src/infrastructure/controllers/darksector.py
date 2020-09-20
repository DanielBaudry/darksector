from flask import current_app as app, render_template
from flask_login import login_required, current_user

from src.infrastructure.dependencies_injections import get_current_expedition, start_new_expedition, player_end_turn


@app.route('/darksector', methods=['GET'])
@login_required
def get_darksector():
    expedition = get_current_expedition.execute(user_id=current_user.id)
    error = None
    sector = None
    player = None
    if not expedition:
        error = 'No darksector in progress'
    else:
        sector = expedition.sector
        player = expedition.player
    return render_template('darksector.html', sector=sector, expedition=expedition, player=player,
                           error=error)


@app.route('/darksector/start', methods=['GET'])
@login_required
def start_darksector():
    expedition = start_new_expedition.execute(user_id=current_user.id)
    return render_template('darksector.html', sector=expedition.sector, expedition=expedition, player=expedition.player)


@app.route('/darksector/next', methods=['GET'])
@login_required
def complete_sector():
    expedition = player_end_turn.execute(user_id=current_user.id)
    return render_template('darksector.html', sector=expedition.sector, expedition=expedition, player=expedition.player,
                           error=None)
