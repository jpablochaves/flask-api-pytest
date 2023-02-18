from calculator.calculator import flask_app


"""
Para aplicaciones de pequeño y medio tamaño se puede hacer lo siguiente: 
importar el modulo de vistas (todos los @), en otros lados son los routes también
"""


if __name__ == '__main__':
    flask_app.run(host='0.0.0.0', port=3000)
    
"""
La documentación de Flask recomienda utilizar Blueprints para aplicaciones de gran tamañao.
Blueprint: Flask concept for making app components and supporting common patterns within an application or across applications. Can simplify how large application work and provide a central means for Flask extension to register operations on applications.
"""
