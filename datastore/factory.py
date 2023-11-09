from datastore.datastore import DataStore
from settings import get_settings


async def get_datastore() -> DataStore:
    datastore = get_settings().datastore
    assert datastore is not None

    # TODO: none
    return None

    match datastore:
        case _:
            raise ValueError(
                f"Unsupported vector database: {datastore}. "
                f"Try one of the following: llama, elasticsearch, pinecone, weaviate, milvus, zilliz, redis, azuresearch, or qdrant"
            )
