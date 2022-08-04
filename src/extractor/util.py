import datetime
import os
import pandas as pd

class Util:
    @staticmethod
    def get_all_files_in_dir(path: str):
        assert path != ""
        filenames = os.listdir(path)
        return filenames

    @staticmethod
    def write_to_csv(data: dict, directory: str="./output", filename: str="data.csv"):
        if not os.path.exists(directory):
            os.makedirs(directory)

        df = pd.DataFrame(data)
        df.to_csv(os.path.join(directory, filename), index=False)
        print("[+] Saved to {}".format(os.path.join(directory, filename)))
        
    @staticmethod
    def read_from_csv(filepath: str):
        assert filepath != ""
        try:
            df = pd.read_csv(filepath)
            df.drop_duplicates(subset="emails", inplace=True)
            return df
        except:
            return None