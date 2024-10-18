import pandas as pd

class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.file_path)
            df = self._add_relevant_info(df)
            return df
        except FileNotFoundError:
            print(f"Error: El archivo {self.file_path} no se pudo encontrar.")
            return pd.DataFrame()

    def _add_relevant_info(self, df: pd.DataFrame) -> pd.DataFrame:
        # Agregar información relevante al DataFrame
        df['informacion_relevante'] = df.apply(
            lambda row: f"Director: {row['Cast']}, Valor ganado: {row['Info']}", axis=1
        )
        return df