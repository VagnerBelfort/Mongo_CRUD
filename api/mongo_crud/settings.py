import os

# flask settings
FLASK_APP = os.environ.get('FLASK_APP', 'PDFto')
FLASK_ENVIRONMENT = os.environ.get('FLASK_ENVIRONMENT', 'development')
FLASK_SERVER_NAME = os.environ.get('FLASK_SERVER_NAME', None)
FLASK_HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
FLASK_PORT = os.environ.get('FLASK_PORT', '5000')
FLASK_DEBUG = os.environ.get('FLASK_DEBUG', True)
FLASK_RESTPLUS_VALIDATE = os.environ.get('FLASK_RESTPLUS_VALIDATE', True)
FLASK_RESTPLUS_MASK_SWAGGER = os.environ.get('FLASK_RESTPLUS_MASK_SWAGGER', False)

# endpoints



# swagger settings
SWAGGER_DOC = '/swagger'
SWAGGER_TITLE = 'MongoDB CRUD'
SWAGGER_DESCRIPTION = 'A Python Flask API to manage MongoDB CRUD.'
SWAGGER_VERSION = '1.0'
SWAGGER_CONTACT = 'Vagner Menezes Belfort de Lima'
SWAGGER_CONTACT_URL = 'https://www.linkedin.com/in/vagner-belfort-7157b8142/'
SWAGGER_CONTACT_EMAIL = 'vagner_mbl@gmail.com'
