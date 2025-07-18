from flask import Blueprint
from flask_dashboard.controllers.dashboard_controller import *

dashboard_bp = Blueprint('dashboard_bp', __name__)

dashboard_bp.route('/top_active_students', methods=['GET'])(get_top_active_students)
dashboard_bp.route('/ratings_distribution', methods=['GET'])(get_ratings_distribution)
dashboard_bp.route('/appointments_status', methods=['GET'])(get_appointments_status)
dashboard_bp.route('/treatment_orders_by_month', methods=['GET'])(get_treatment_orders_by_month)
