from flask import Flask, request, json, Response
from pymongo import MongoClient
import configparser
import logging as log

config = configparser.ConfigParser()
config.read('Config.ini')
config_dict = config['MongoAPIConfig']

class MongoAPI:
    def __init__(self, data):
        '''
        connect to mongodb server
        Args:
            data: parameter needed for operating CRUD operations.
        returns:
            Initialized database collection object.
        '''
        self.client = MongoClient("mongodb+srv://"+
                                  config_dict['user']+":"+
                                  config_dict['password']+"@"+
                                  config_dict['server']+
                                  config_dict['database']+
                                  "?retryWrites=true&w=majority")

        database = config_dict['database']
        collection = config_dict['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data

    def read(self):
        '''
        read all of the documents present in the collection
        returns:
        The output of the collection object is of datatype dictionary
        '''
        documents = self.collection.find()
        output = [{item: data[item] for item in data if item != '_id'} for data in documents]
        return output

    def write(self, data):
        '''
        Add new document ot mongodb collection.
        Args:
            data: accepting data from the user under the key “Document”.
        returns:
        The output of the collection object is of datatype dictionary
        '''
        log.info('Writing Data')
        new_document = data['Document']
        response = self.collection.insert_one(new_document)
        output = {'Status': 'Successfully Inserted',
                  'Document_ID': str(response.inserted_id)}
        return output

    def update(self):
        '''
        update any existing documents.
        returns:
        The output of the collection object is of datatype dictionary
        '''
        filt = self.data['Filter']
        updated_data = {"$set": self.data['DataToBeUpdated']}
        response = self.collection.update_one(filt, updated_data)
        output = {'Status': 'Successfully Updated' if response.modified_count > 0 else "Nothing was updated."}
        return output

    def delete(self, data):
        '''
        delete any existing documents.
        returns:
        The output of the collection object is of datatype dictionary
        '''
        filt = data['Filter']
        response = self.collection.delete_one(filt)
        output = {'Status': 'Successfully Deleted' if response.deleted_count > 0 else "Document not found."}
        return output


if __name__ == '__main__':
    data = {
        "Status": "True",
        "Document":{
            "brand_name": "VictorBasu",
            "classification_l1": "baby & child",
            "classification_l2": "soft toys",
            "classification_l3": "",
            "classification_l4": "",
            "currency": "GBP",
            "image_url": "https://johnlewis.scene7.com/is/image/JohnLewis/237070760?",
            "name": "Pet Shop, Pink",
            "offer_price_value": 30,
            "regular_price_value": 30
        },
        "Filter":{
           "brand_name": "VictorBasu"
        },
        "DataToBeUpdated":{
           "name": "Pet Shop, Black",
           "offer_price_value": 40,
        }
    }
    mongo_obj = MongoAPI(data)
    print(json.dumps(mongo_obj.read(), indent=4))
