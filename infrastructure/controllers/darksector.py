from flask import current_app as app, render_template
from flask_login import login_required, current_user

from infrastructure.dependencies_injections import get_current_expedition, complete_sector_level


@app.route('/darksector', methods=['GET'])
@login_required
def enter_darksector():
    expedition = get_current_expedition.execute(user_id=current_user.id)
    return render_template('darksector.html', sector=expedition.sector, expedition=expedition)


@app.route('/darksector/next', methods=['GET'])
@login_required
def complete_sector():
    expedition = complete_sector_level.execute(user_id=current_user.id)
    return render_template('darksector.html', sector=expedition.sector, expedition=expedition)
