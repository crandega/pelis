from data_loader import DataLoader
from semantica import SemanticSearch

class MovieSearchApp:
    def __init__(self, data_file_path: str):
        self.data_loader = DataLoader('src/IMDB.csv')
        self.search_engine = SemanticSearch()
        self.df = self.data_loader.load_data()
        self.embeddings = self.search_engine.encode_data(self.df['Description'].tolist())

    def run(self):
        while True:
            query = input('Ingresa el término de búsqueda (o escribe "salir" para terminar): ')
            if query.lower() == 'salir':
                print("Saliendo del programa. ¡Hasta luego!")
                break

            similarities = self.search_engine.find_similarities(query, self.embeddings)
            self.df['similarity'] = similarities
            df_sorted = self.df.sort_values(by='similarity', ascending=False)
            self._display_results(df_sorted)

    def _display_results(self, df_sorted):
        print("Resultados similares:")
        print(df_sorted[['Title', 'Cast', 'Info']].head())

if __name__ == '__main__':
    app = MovieSearchApp('src/IMDB.csv')
    app.run()