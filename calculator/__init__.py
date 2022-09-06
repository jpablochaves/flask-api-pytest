from flask import Flask

flask_app = Flask(__name__)
"""
Para aplicaciones de pequeño y medio tamaño se puede hacer lo siguiente: 
importar el modulo de vistas (todos los @), en otros lados son los routes también
"""
import calculator.routes.routes

"""
La documentación de Flask recomienda utilizar Blueprints para aplicaciones de gran tamañao.
Blueprint: Flask concept for making app components and supporting common patterns within an application or across applications. Can simplify how large application work and provide a central means for Flask extension to register operations on applications.
"""