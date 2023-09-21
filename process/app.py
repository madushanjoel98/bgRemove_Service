from flask import Flask, request, jsonify
import bgremover
import loginforms
from db.tables import userTable
app = Flask(__name__)
lio = loginforms.User()
userTables = userTable.UserTable()
@app.route('/bas64remover', methods=['POST'])
def submit():
    try:
        remover = bgremover.BGRemover()
        # Access JSON data from the request body
        data = request.get_json()
        # Access specific JSON fields
        base = data.get('base')
        name = data.get('name')
        password = data.get('password')
        if userTables.userLogin(name, password):
            base = str(remover.removeBg_baseTO_base(base))
            # Process the data (e.g., save it to a database)
            # # In this example, we'll just return a JSON response
            response = {
                'remove': f"{base}"
            }
            return jsonify(response), 200
        else:
            response = {
                'message': "Invalid Login"
            }
            return jsonify(response), 401
    except Exception as e:
        error_response = {
            'error': 'Invalid JSON data: ' + str(e)
        }
        return jsonify(error_response), 400


if __name__ == '__main__':
    app.run(debug=True)
