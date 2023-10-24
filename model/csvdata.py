from typing import List, Callable
import pandas as pd
from os import path


# Module to store database
class CSV_Data():

    # Attributes
    def __init__(self):

        self._csv_data = pd.DataFrame()

    def get_data(self)-> pd.DataFrame:

        return self._csv_data
    
    def export_data(self, output_dir):

        if self._csv_data.empty:
            return
        else:
            try:
                self._csv_data.to_csv(output_dir + "\\" + "merged data.csv", 
                                    header=True, index=False, 
                                    sep=",", compression=None)
            except Exception as e:
                print(str(e))
                # self._status = f"An error occurred: <font color='red'>{str(e)}</font>"
                # self.notify()


    def init_csv_data(self):

        self._csv_data = pd.DataFrame();
    """
    Define normal class method
    """
    def import_csv_file(
            self,
            csv_filepath: str,
            reading_col,
            reading_skip_rows: list
            )->None:

        # Checking csv_filepath direct to a file or not
        if len(reading_col) == 0:
            reading_col = None

        if len(reading_skip_rows) == 0:
            reading_skip_rows = None
            
        df = pd.read_csv(csv_filepath, index_col=None, 
                         sep=',', header=0, 
                         usecols=reading_col, skiprows=reading_skip_rows)

        # Remove duplicated rows
        df = df.drop_duplicates()
        # Merging data frames into one frame
        try:
            if not df.empty:
                self._csv_data = pd.concat([self._csv_data, df], axis=0, ignore_index=True)

        except:
            return None


    def import_csv_files(
            self,
            filepaths: str,
            reading_cols: List[str],
            skip_rows: List[int],
            callbackMessage: Callable[[str], None]
    )-> pd.DataFrame:

        self.init_csv_data()

        if reading_cols is None:
            return

        # Notice reading file:
        total_df = []
        imported_count = 0

        for filepath in filepaths:
            callbackMessage(f"Reading file:  {path.basename(filepath)}")
            
            extracted_file_df = pd.DataFrame()
            current_data_chunk = pd.DataFrame()
            found_cols = []

            try:
                imported_df = pd.read_csv(filepath, index_col=None, sep=',', header=0, skiprows=skip_rows)
                imported_df_cols = list(imported_df.columns)
            except Exception as e:
                print(str(e))
                continue

            for col in reading_cols:
                if col in imported_df_cols:
                    found_cols.append(col)
                else:
                    if len(found_cols) > 0:
                        # get piece of data which have header as column in 'found_colnames'
                        current_data_chunk = imported_df[found_cols]
                        # build a single empty column data with header as 'col'
                        empty_data_chunk = pd.Series(data=None, name=col, dtype='object')
                        # push it to 'extracted_df'
                        extracted_file_df = pd.concat([extracted_file_df, current_data_chunk, empty_data_chunk], axis=1)

                        found_cols.clear()
                        current_data_chunk = None

            # After iterate over all column name in needed_columns
            # If found_colnames is not empty then extract data and push to 'extracted_df'
            if len(found_cols) > 0:
                current_data_chunk = imported_df[found_cols]
                extracted_file_df = pd.concat([extracted_file_df, current_data_chunk], axis=1)
                found_cols.clear()
                current_data_chunk = None

            # append the data extracted from file to total dataframe
            if not extracted_file_df.empty:
                total_df.append(extracted_file_df)
                imported_count += 1

        # Merging data frames into one frame
        if len(total_df) > 0:
            self._csv_data = pd.concat(total_df, axis=0, ignore_index=True)

        return imported_count


