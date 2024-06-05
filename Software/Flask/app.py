# Flask server for Arduino Storage Cart Project
# Written by Michael Lance
# Created: 6/04/2024
# Last Modified: 6/04/2024
#---------------------------------------------------------------------------------------------------#

import sys
import os

from flask import Flask, send_from_directory
from flask_mysqldb import MySQL


#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Communications')))

#import communications

app = Flask(__name__, static_folder='dist')

# MySQL configurations
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flask_vue_db'

mysql = MySQL(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

# Example usage of the imported module
@app.route('/api/example')
def example():
    result = my_module.some_function()  # Replace with actual function you need to call
    return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)