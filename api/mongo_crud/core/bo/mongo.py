from pymongo import MongoClient
from bson.objectid import ObjectId

# connect MongoDB
client = MongoClient('mongo', 27017)
db = client.escola
cursos_collections = db.cursos


def findall():
    """
    This function searches all MongoDB data.

    params
    ------

    Get

    return
    ------

    All MongoDB data.
    """

    dataset = {
        "curso": [],
        "materia": [],
        "professor": [],
        "horas": [],
        "ids": []
    }
    request_data_get = cursos_collections.find()

    for result in request_data_get:
        dataset['curso'].append(result["curso"])
        dataset['materia'].append(result["materia"])
        dataset['professor'].append(result["professor"])
        dataset['horas'].append(result["horas"])
        dataset['ids'].append(str(result["_id"]))

    return dataset


def getcurso(curso):
    """
    This function searches for a curso.

    params
    ------

    rotina: str, curso.

    return
    ------

    dataset: JSON, search result for curso.
    """

    dataset = {
        "curso": [],
        "materia": [],
        "professor": [],
        "horas": [],
        "ids": []
    }
    request_data_get = cursos_collections.find({"curso": curso})

    for result in request_data_get:
        dataset['curso'].append(result["curso"])
        dataset['materia'].append(result["materia"])
        dataset['professor'].append(result["professor"])
        dataset['horas'].append(result["horas"])
        dataset['ids'].append(str(result["_id"]))

    return dataset


def getmateria(materia):
    """
    This function searches for a materia.

    params
    ------

    rotina: str, serve materia.

    return
    ------

    dataset: JSON, search result for materia.
    """

    dataset = {
        "curso": [],
        "materia": [],
        "professor": [],
        "horas": [],
        "ids": []
    }
    request_data_get = cursos_collections.find({"materia": materia})

    for result in request_data_get:
        dataset['curso'].append(result["curso"])
        dataset['materia'].append(result["materia"])
        dataset['professor'].append(result["professor"])
        dataset['horas'].append(result["horas"])
        dataset['ids'].append(str(result["_id"]))

    return dataset


def postdados(new_item_id):
    """
    This function registers data.

    params
    ------

    new_item_id: JSON, json of the data to be inserted in MongoDB.

    return
    ------

    item_id: object.mongo, inserted item id.
    """

    item_id = cursos_collections.insert_one(new_item_id).inserted_id

    mensage = 'o item do id {} foi inserido'.format(item_id)
    print(item_id)

    return mensage


def deletedados(id_item):
    """
    This function deletes an item from mongodb by ID.

    params
    ------

    id: str.

    return
    ------

    id_item: delete item id.
    """

    delete = {
        "_id": ObjectId(id_item['_id'])
    }

    cursos_collections.delete_one(delete)

    mensage = 'o item do id {} foi deletado'.format(id_item['_id'])

    return mensage


def putdados(response):
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

    cursos_collections.update_one(response['id'], response['set'], upsert=True)

    mensage = 'O id {} foi atualizado'.format(response['id']['_id'])

    return mensage
