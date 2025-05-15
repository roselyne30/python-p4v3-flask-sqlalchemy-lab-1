from flask import Flask, jsonify, abort
from models import db, Earthquake

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/earthquakes/<int:id>')
def get_earthquake(id):
    quake = Earthquake.query.get(id)
    if quake:
        return jsonify(quake.to_dict())
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404

@app.route('/earthquakes/magnitude/<float:magnitude>')
@app.route('/earthquakes/<int:id>')
def get_earthquakes_by_magnitude(magnitude):
    
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    return jsonify({
        "count": len(quakes),
        "quakes": [quake.to_dict() for quake in quakes]
    })

def get_earthquake(id):
    quake = Earthquake.query.get(id)
    if quake:
        return jsonify(quake.to_dict())
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)
