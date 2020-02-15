from bson.errors import InvalidId
from flask import request
from flask_restplus import Namespace, Resource, fields
from bson.objectid import ObjectId
from core.constants import http_code
from core.bo.mongo import findall, getcurso, getmateria
from core.bo.mongo import postdados, deletedados, putdados

api = Namespace('mongo', description='Request operations in MongoDB')


@api.route('/search/all')
class GetAll(Resource):
    def get(self):
        """
        This function searches all MongoDB data.

        params
        ------

        Get

        return
        ------

        All MongoDB data.
        """

        result_all = findall()
        return result_all, 200


@api.route('/search/curso/<string:curso>')
class GetCurso(Resource):
    def get(self, curso=None):
        """
        This function searches for a curso.

        params
        ------

        curso: str, serve curso.

        return
        ------

        result_getrotinas: JSON, search result for curso.
        """

        request_data = request.json

        result_getrotina = {"mensage": ""}
        result_getrotina["mensage"] = getcurso(curso)
        return result_getrotina


@api.route('/search/materia/<string:materia>')
class GetMateria(Resource):
    def get(self, materia=None):
        """
        This function searches for a materia.

        params
        ------

        materia: str, serve materia.

        return
        ------

        result_getrotinas: JSON, search result for materia.
        """

        request_data = request.get_json()
        result_programa = getmateria(materia)
        return result_programa


# swagger input
INPUT_DATA_INPUT = api.model('input_input',
                             {
                                 'curso': fields.String(required=True, description='curso', example='Machine Learning'),
                                 'materia': fields.String(required=True, description='materia', example='aprendizado supervisionado'),
                                 'professor': fields.String(required=True, description='professor', example='Paulo Cotta'),
                                 'horas': fields.String(required=True, description='horas', example='40')
                             })


@api.route('/insert')
class PostDados(Resource):
    @api.expect(INPUT_DATA_INPUT)
    def post(self):
        """
        This function creates a json of the items to be inserted in MongoDB.

        params
        ------

        curso: str, curso\n
        materia: str, materia\n
        professor: str, professor\n
        horas: str, horas\n

        return
        ------

        new_item_id: object.mongo, inserted item id.
        """

        request_data = request.get_json()
        new_item_id = {}

        mensage_ = {"messages": "", "status": ""}

        new_item_id['curso'] = request_data['curso']
        new_item_id['materia'] = request_data['materia']
        new_item_id['professor'] = request_data['professor']
        new_item_id['horas'] = request_data['horas']

        mensage_['messages'] = postdados(new_item_id)

        mensage_['status'] = http_code.SUCCESS_201

        return mensage_


# swagger delete
INPUT_DATA_DELETE = api.model('input_delete',
                              {
                                  'id': fields.String(required=True, description='mongo item to be deleted',
                                                      example='5e3b0ba256d95efdacf44fdd')
                              })


@api.route('/delete')
class DeleteDados(Resource):
    @api.expect(INPUT_DATA_DELETE)
    def delete(self):
        """
        This function deletes an item from mongodb by ID.

        params
        ------

        id: str, mongo item to be deleted

        return
        ------

        id_item: delete item id.
        """

        request_data = request.get_json()

        # Json que será inserido na funcao de delete do mongo
        id_item = {}

        # Json de resposta para o front
        mensage_ = {"messages": "", "status": ""}

        # key que recebe o id que sera deletado
        id_item['_id'] = request_data['id']

        # tratamento para erro de id invalido
        try:
            mensage_["messages"] = deletedados(id_item)

        except InvalidId as invalid:
            mensage_["messages"] = str(invalid)
            mensage_["status"] = http_code.ERROR_500

            return mensage_

        mensage_["status"] = http_code.SUCCESS_200

        return mensage_


# swagger upadate
INPUT_DATA_UPDATE = api.model('input_update',
                              {
                                  'id': fields.String(required=True, description='mongo item to be update',
                                                      example='5e3c6357a97305a64eebf551'),
                                  'curso': fields.String(required=True, description='curso', example='Machine Learning'),
                                  'materia': fields.String(required=True, description='materia', example='aprendizado supervisionado'),
                                  'professor': fields.String(required=True, description='professor', example='Paulo Cotta'),
                                  'horas': fields.String(required=True, description='horas', example='40')
                              })


@api.route('/update')
class PutDados(Resource):
    @api.expect(INPUT_DATA_UPDATE)
    def put(self):
        """
        This function updates mongodb data.

        params
        ------

        curso: str, curso\n
        materia: str, materia\n
        professor: str, professor\n
        horas: str, horas\n

        return
        ------

        Nothing.
        """

        request_data = request.get_json()

        response = {}

        # Json de resposta para o front
        mensage_ = {"messages": "", "status": ""}

        try:
            response['id'] = {'_id': ObjectId(request_data['id'])}

        except InvalidId as invalid:
            mensage_["messages"] = str(invalid)
            mensage_["status"] = http_code.ERROR_500

            return mensage_

        response['set'] = {"$set": {"curso": request_data['curso'],
                                    "materia": request_data['materia'],
                                    "professor": request_data['professor'],
                                    "horas": request_data['horas']}}

        # A variavel "_" é o status de retorno do mongo, que é despresivel.
        mensage_["messages"] = putdados(response)
        mensage_["status"] = http_code.SUCCESS_200

        return mensage_
