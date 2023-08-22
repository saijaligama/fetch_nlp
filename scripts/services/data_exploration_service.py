from flask import Blueprint, render_template

data_exploration_bp = Blueprint('data_exploration_bp', __name__)


@data_exploration_bp.route('/data_exp')
def data():
    return render_template('data_exploration.html')