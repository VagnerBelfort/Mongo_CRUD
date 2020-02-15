from bson.errors import InvalidId
from flask import request
from flask_restplus import Namespace, Resource, fields
from bson.objectid import ObjectId
import settings
from core.constants import http_code
from core.bo.mongo import findall, getrotina, getprograma
from core.bo.mongo import postdados, deletedados, putdados

api = Namespace('mongo', description='Post operação.')


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


@api.route('/search/rotina/<string:rotina>')
class GetRotina(Resource):
    def get(self, rotina=None):
        """
        This function searches for a routine.

        params
        ------

        rotina: str, serve routine.

        return
        ------

        result_getrotinas: JSON, search result for routine.
        """

        request_data = request.json

        result_getrotina = {"mensage": ""}
        result_getrotina["mensage"] = getrotina(rotina)
        return result_getrotina


@api.route('/search/programa/<string:programa>')
class GetPrograma(Resource):
    def get(self, programa=None):
        """
        This function searches for a routine.

        params
        ------

        rotina: str, serve routine.

        return
        ------

        result_getrotinas: JSON, search result for routine.
        """

        request_data = request.get_json()
        result_programa = getprograma(programa)
        return result_programa


# swagger input
INPUT_DATA_INPUT = api.model('input_input',
                             {
                                 'rotina': fields.String(required=True, description='server error routine', example='Rotinateste'),
                                 'programa': fields.String(required=True, description='server error program', example='Programateste'),
                                 'pilha': fields.String(required=True, description='error list of logs', example='Logteste'),
                                 'solucao': fields.String(required=True, description='error solution', example='solucaoteste')
                             })


@api.route('/insert')
class PostDados(Resource):
    @api.expect(INPUT_DATA_INPUT)
    def post(self):
        """
        This function creates a json of the items to be inserted in MongoDB.

        params
        ------

        rotina: str, server error routine.\n
        programa: str, server error program.\n
        pilha: str, error list of logs.\n
        solucao: str, error solution.\n

        return
        ------

        new_item_id: object.mongo, inserted item id.
        """

        request_data = request.get_json()
        new_item_id = {}

        mensage_ = {"messages": "", "status": ""}

        new_item_id['rotina'] = request_data['rotina']
        new_item_id['programa'] = request_data['programa']
        new_item_id['pilha'] = request_data['pilha']
        new_item_id['solucao'] = request_data['solucao']

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
                                  'id': fields.String(required=True, description='mongo item to be deleted',
                                                      example='5e3c6357a97305a64eebf551'),
                                  'rotina': fields.String(required=True, description='server error routine', example='Rotinateste'),
                                  'programa': fields.String(required=True, description='server error program', example='Programateste'),
                                  'pilha': fields.String(required=True, description='error list of logs', example='Logteste'),
                                  'solucao': fields.String(required=True, description='error solution', example='solucaoteste')
                              })


@api.route('/update')
class PutDados(Resource):
    @api.expect(INPUT_DATA_UPDATE)
    def put(self):
        """
        This function updates mongodb data.

        params
        ------

        Rotina: str, server error routine.\n
        Programa: str, server error program.\n
        Pilha: str, error list of logs.\n
        Solucao: str, error solution.\n

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

        response['set'] = {"$set": {"rotina": request_data['rotina'],
                                    "programa": request_data['programa'],
                                    "pilha": request_data['pilha'],
                                    "solucao": request_data['solucao']}}

        # A variavel "_" é o status de retorno do mongo, que é despresivel.
        mensage_["messages"] = putdados(response)
        mensage_["status"] = http_code.SUCCESS_200

        return mensage_
