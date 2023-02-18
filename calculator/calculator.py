import os
import sys
from flask import Flask

flask_app = Flask(__name__)

# Get the directory where this file is located
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
# add the parent directory to the sys.path
sys.path.append(parent)

import calculator.routes.routes