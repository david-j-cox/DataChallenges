from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)
api = Api(app)

with open('/Users/dcox/Dropbox/InsightFellowship/DataChallenges/MyDataChallenges/data_challenge_3/model.pkl', 'rb') as mod_file:
    lr = pickle.load(mod_file)

# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('clump_thickness', type=int, required=True, help="Clump thickness, specified as an integer.")
parser.add_argument('unif_cell_size', type=int, required=True, help="Uniformity of cell size, specified as an integer.")
parser.add_argument('unif_cell_shape', type=int, required=True, help="Uniformity of cell shape, specified as an integer.")
parser.add_argument('marginal_adhesion', type=int, required=True, help="Marginal adhesion, specified as an integer.")
parser.add_argument('single_epi_size', type=int, required=True, help="Single epithelial cell size, specified as an integer.")
parser.add_argument('bare_nuclei', type=int, required=True, help="Bare nuclei, specified as an integer.")
parser.add_argument('chromatin', type=int, required=True, help="Chromatin, specified as an integer.")
parser.add_argument('nucleoli', type=int, required=True, help="Nucleoli, specified as an integer.")
parser.add_argument('mitoses', type=int, required=True, help="Mitoses, specified as an integer.")

class predictCancer(Resource):
    """Classification to predict whether a cell is benign or malignant."""
    def __init__(self):
        pass
    
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        clump_thickness = args['clump_thickness']
        unif_cell_size = args['unif_cell_size']
        unif_cell_shape = args['unif_cell_shape']
        marginal_adhesion = args['marginal_adhesion']
        single_epi_size = args['single_epi_size']
        bare_nuclei = args['bare_nuclei']
        chromatin = args['chromatin']
        nucleoli = args['nucleoli']
        mitoses = args['mitoses']
        arr_in = np.array([[clump_thickness, unif_cell_size, unif_cell_shape, marginal_adhesion, single_epi_size, \
                            bare_nuclei, chromatin, nucleoli, mitoses, 1]])
        pred = lr.predict(arr_in)
        pred_probs = lr.predict_proba(arr_in)

        if pred[0] == 0:
            pred_text = 'Benign'
            confidence = np.round(pred_probs[0][0] * 100, 1)
        else:
            pred_text = 'Malignant'
            confidence = np.round(pred_probs[0][1] * 100, 1)        

        output = {'prediction': pred_text,
                  'confidence': confidence}

        return output

api.add_resource(predictCancer, '/api/v1/')


if __name__ == '__main__':
    app.run(debug=False)