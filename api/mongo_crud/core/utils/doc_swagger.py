# from flask_restplus import fields
#
#
# # api = Api(version='2.0', title='Documentação - Dilbert para API do MongoDB')
#
# # entradas e saidas do swagger endpoint delete / http://localhost:9001/api/mongo/delete
#
# INPUT_DATA_DELETE = api.model('input_delete',
#                               {
#                                   'id': fields.String(required=True, description='mongo item to be deleted',
#                                                       example='5e3b0ba256d95efdacf44fdd')
#                               })
#
# OUTPUT_DATA_DELETE = api.model('output_delete',
#                                {'mensage': fields.String(required=True, description='item delete', example='successfuly deleted item')})
#
# # entradas e saidas do swagger endpoint insert / http://localhost:9001/api/mongo/insert
#
# INPUT_DATA_INPUT = api.model('input_input',
#                              {
#                                  'rotina': fields.String(required=True, description='server error routine', example='Rotinateste'),
#                                  'programa': fields.String(required=True, description='server error program', example='Programateste'),
#                                  'pilha': fields.String(required=True, description='error list of logs', example='Logteste'),
#                                  'solucao': fields.String(required=True, description='error solution', example='solucaoteste')
#                              })
#
# OUTPUT_DATA_INPUT = api.model('output_input',
#                               {'mensage': fields.String(required=True, description='item delete', example='successfuly deleted item')})
#
# # entradas e saidas do swagger endpoint update / http://localhost:9001/api/mongo/update
#
# INPUT_DATA_UPDATE = api.model('input_update',
#                               {
#                                   'id': fields.String(required=True, description='mongo item to be deleted',
#                                                       example='5e3c6357a97305a64eebf551'),
#                                   'rotina': fields.String(required=True, description='server error routine', example='Rotinateste'),
#                                   'programa': fields.String(required=True, description='server error program', example='Programateste'),
#                                   'pilha': fields.String(required=True, description='error list of logs', example='Logteste'),
#                                   'solucao': fields.String(required=True, description='error solution', example='solucaoteste')
#                               })
#
# OUTPUT_DATA_UPDATE = api.model('output_update',
#                                {'mensage': fields.String(required=True, description='item delete', example='successfuly deleted item')})
