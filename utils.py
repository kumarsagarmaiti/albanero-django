import pymongo


def create_connection(db_name: str, collection_name: str):
    connection_string = "mongodb+srv://kumarsagar_functionup:CjDCkJbsxcpkMf5N@cluster0.fnt89sj.mongodb.net/albanero-demo"
    client = pymongo.MongoClient(connection_string)
    db = client[db_name]
    collections = db[collection_name]
    return collections
