from flask import current_app as app, render_template, redirect, url_for
from flask_login import login_required, current_user

from infrastructure.dependencies_injections import get_current_expedition, complete_sector_level, start_new_expedition


@app.route('/darksector', methods=['GET'])
@login_required
def get_darksector():
    expedition = get_current_expedition.execute(user_id=current_user.id)
    error = None
    sector = None
    if not expedition:
        error = 'No darksector in progress'
    else:
        sector = expedition.sector
    return render_template('darksector.html', sector=sector, expedition=expedition, error=error)


@app.route('/darksector/start', methods=['GET'])
@login_required
def start_darksector():
    expedition = start_new_expedition.execute(user_id=current_user.id)
    return render_template('darksector.html', sector=expedition.sector, expedition=expedition)


@app.route('/darksector/next', methods=['GET'])
@login_required
def complete_sector():
    expedition = complete_sector_level.execute(user_id=current_user.id)
    return render_template('darksector.html', sector=expedition.sector, expedition=expedition, error=None)
