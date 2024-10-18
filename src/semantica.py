from sentence_transformers import SentenceTransformer, util

class SemanticSearch:
    def __init__(self, model_name: str = 'sentence-transformers/all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def encode_data(self, data: list) -> list:
        # Crear embeddings para las descripciones
        return self.model.encode(data, show_progress_bar=True)

    def find_similarities(self, query: str, data_embeddings: list) -> list:
        query_embedding = self.model.encode(query)
        similarities = util.cos_sim(query_embedding, data_embeddings)
        return similarities.flatten()