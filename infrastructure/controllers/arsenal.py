from flask import current_app as app, render_template
from flask_login import login_required, current_user

from infrastructure.dependencies_injections import get_player_details


@app.route('/arsenal', methods=['GET'])
@login_required
def arsenal_details():
    player = get_player_details.execute(user_id=current_user.id)
    return render_template('arsenal.html', player=player)
