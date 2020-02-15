from flask_restplus import Api

import settings
from apis.mongo_crud import api as api_1

api = Api(doc=settings.SWAGGER_DOC,
          title=settings.SWAGGER_TITLE,
          description=settings.SWAGGER_DESCRIPTION,
          contact=settings.SWAGGER_CONTACT,
          contact_url=settings.SWAGGER_CONTACT_URL,
          contact_email=settings.SWAGGER_CONTACT_EMAIL)

api.add_namespace(api_1)
