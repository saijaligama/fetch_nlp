from flask import Blueprint, request, jsonify, render_template
from scripts.core.handlers.search_handler import SearchHandler

search_service_bp = Blueprint('search_service_bp', __name__)


@search_service_bp.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        try:
            req_data = request.get_json()
            query = req_data['search_query']

            searcher = SearchHandler()
            results = searcher.search(query)

            return jsonify(results)
        except Exception as e:
            return {'error': str(e)}, 500
    else:
        return "check type of request sent"


# if __name__ == '__main__':
#     app.run()