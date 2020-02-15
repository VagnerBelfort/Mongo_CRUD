from pymongo import MongoClient
from bson.objectid import ObjectId

# connect MongoDB
client = MongoClient('mongo', 27017)
db = client.dilbert
dilbert_collections = db.dataset_dilbert


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
        "rotina": [],
        "programa": [],
        "pilha": [],
        "ids": []
    }
    request_data_get = dilbert_collections.find()

    for result in request_data_get:
        dataset['rotina'].append(result["rotina"])
        dataset['programa'].append(result["programa"])
        dataset['pilha'].append(result["pilha"])
        dataset['ids'].append(str(result["_id"]))

    return dataset


def getrotina(rotina):
    """
    This function searches for a routine.

    params
    ------

    rotina: str, serve routine.

    return
    ------

    result_getrotinas: JSON, search result for routine.
    """

    dataset = {
        "rotina": [],
        "programa": [],
        "pilha": [],
        "ids": []
    }
    request_data_get = dilbert_collections.find({"rotina": rotina})

    for result in request_data_get:
        dataset['rotina'].append(result["rotina"])
        dataset['programa'].append(result["programa"])
        dataset['pilha'].append(result["pilha"])
        dataset['ids'].append(str(result["_id"]))

    return dataset


def getprograma(programa):
    """
    This function searches for a routine.

    params
    ------

    rotina: str, serve routine.

    return
    ------

    result_getrotinas: JSON, search result for routine.
    """

    dataset = {
        "rotina": [],
        "programa": [],
        "pilha": [],
        "ids": []
    }
    request_data_get = dilbert_collections.find({"programa": programa})

    for result in request_data_get:
        dataset['rotina'].append(result["rotina"])
        dataset['programa'].append(result["programa"])
        dataset['pilha'].append(result["pilha"])
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

    item_id = dilbert_collections.insert_one(new_item_id).inserted_id

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

    dilbert_collections.delete_one(delete)

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

    dilbert_collections.update_one(response['id'], response['set'], upsert=True)

    mensage = 'O id {} foi atualizado'.format(response['id']['_id'])

    return mensage
