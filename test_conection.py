from pymongo import MongoClient
import pymongo

def test_connection():
    try:
        # Intentar establecer conexión
        client = MongoClient('mongodb://localhost:27017/')

        # Intentar acceder a la base de datos Crhistmas
        db = client['Crhistmas']

        # Intentar acceder a la colección wish
        wish_collection = db['wish']

        # Intentar una operación simple para verificar la conexión
        wish_collection.find_one()

        # Obtener información del servidor
        server_info = client.server_info()

        print("✅ Conexión exitosa a MongoDB!")
        print(f"Versión del servidor: {server_info['version']}")
        print(f"Base de datos: {db.name}")
        print(f"Colecciones disponibles: {db.list_collection_names()}")

        return True

    except pymongo.errors.ServerSelectionTimeoutError:
        print("❌ Error: No se pudo conectar al servidor MongoDB")
        print("Por favor, verifica que MongoDB esté ejecutándose en localhost:27017")
        return False

    except pymongo.errors.OperationFailure as e:
        print(f"❌ Error de operación: {e}")
        return False

    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return False

    finally:
        client.close()

if __name__ == "__main__":
    test_connection()