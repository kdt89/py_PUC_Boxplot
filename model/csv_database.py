from __future__ import annotations
from typing import List, Callable, Any
import pandas as pd
from numpy import ndarray
from pandas import DataFrame
from pandas.core.groupby.generic import DataFrameGroupBy
from os import path


# Module to store database
class CSV_Database():

    DATASET_ID_COLUMN_NAME = "DATA_FILENAME"

    # Attributes
    def __init__(self) -> None:
        self._csv_data: DataFrame = DataFrame(data=None)


    @property
    def size(self) -> tuple[int, int]:
        return len(self._csv_data.index), len(self._csv_data.columns)
    
    
    # def clearDatabase(self) -> None:
    #     self._csv_data = DataFrame(data=None)

    def export_data(self, output_dir) -> None:
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


    def import_csv_files(
            self,
            filepaths: str,
            reading_cols: List[str],
            skip_rows: List[int],
            callbackMessage: Callable[[str], None]
    ) -> DataFrame:

        if reading_cols is None:
            return

        total_df: List[DataFrame] = []
        imported_count: int = 0

        for filepath in filepaths:
            filename = path.splitext(path.basename(filepath))[0] # splitext() return (filename, extension)
            # Notice reading file:
            callbackMessage(f"Reading file:  {path.basename(filepath)}")

            df_extracted_from_file = pd.DataFrame()
            df_current_chunk = pd.DataFrame()
            found_cols: List[str] = []

            try:
                df_raw_imported = pd.read_csv(filepath, index_col=None, sep=',', header=0, skiprows=skip_rows)
                columns_df_raw_imported = list(df_raw_imported.columns)
            except Exception as e:
                print(str(e))
                continue

            for col in reading_cols:
                if col in columns_df_raw_imported:
                    found_cols.append(col)
                else:
                    if len(found_cols) > 0:
                        # get piece of data which have header as column in 'found_colnames'
                        df_current_chunk = df_raw_imported[found_cols]
                        # build a single empty column data with header as 'col'
                        df_empty_chunk = pd.Series(data=None, name=col, dtype='object')
                        # push it to 'extracted_df'
                        df_extracted_from_file = pd.concat([df_extracted_from_file, df_current_chunk, df_empty_chunk], axis=1)

                        found_cols.clear()
                        df_current_chunk = None

            # After iterate over all column name in needed_columns, ...
            # if found_colnames is not empty then extract data and push to 'extracted_df'
            if len(found_cols) > 0:
                df_current_chunk = df_raw_imported[found_cols]
                df_extracted_from_file = pd.concat([df_extracted_from_file, df_current_chunk], axis=1)
                
                df_extracted_from_file = df_extracted_from_file.drop_duplicates()
                df_extracted_from_file = df_extracted_from_file.dropna(
                    axis=0, # drop rows which contain missing values
                    how='all', # if all values of checking columns are NA, drop that row or column
                    subset=None) # check all columns

                found_cols.clear()
                df_current_chunk = None

            # For later use when making plot, we need to categorize the dataset by its name,...
            # by adding extra column [DATA_FILENAME] with row value is the name of file we extract data from
            data_filename = pd.Series(
                data=filename,
                index=range(0, df_extracted_from_file.shape[0])) # range from 0 to number of rows of 'df_extracted_from_file'
        
            df_extracted_from_file.insert(
                loc=0, # insert new column as first (left-most) column
                column = CSV_Database.DATASET_ID_COLUMN_NAME,
                value=data_filename)

            # append the dataframe extracted from file to total list dataframe
            if not df_extracted_from_file.empty:
                total_df.append(df_extracted_from_file)
                imported_count += 1

        # Merging data frames into one frame
        # Abandon previous data in self._csv_data and hooked up to newly imported data
        if len(total_df) > 0:
            self._csv_data = pd.concat(total_df, axis=0, ignore_index=True)

        return imported_count


    def get_groupdata_at_column(
            self,
            groupby_columnname: str,
            need_data_columnname: str
    ) -> tuple[List[ndarray[Any]], List[str]]:
        """
        Function to extract dataframe from Pandas Groupby object with a specific column
        @param groupby_columnname: str
        @param need_data_columnname: str
        @return: tuple[List[str], List[ndarray[Any]]]
                 List[ndarray[Any]]: List of numpy array, each array contains float numbers
                 List[str]: List of labels, each label is name of corrensponding dataset in List[ndarray[Any]]
        """
        # Validation the column name to extract data exist in target database or not
        data_column_names = self._csv_data.columns
        if not need_data_columnname in data_column_names:
            return (None, None)
        
        if not groupby_columnname in data_column_names:
            return (None, None)
        
        # Extract data from CSV database
        df_needed_data = self._csv_data[[groupby_columnname, need_data_columnname]]
        df_grouped_plot_data = df_needed_data.groupby(by=groupby_columnname, sort=None)

        # Prepare data
        list_data_labels: List[str] = []
        list_dataset: List[ndarray] = []

        for group_name, group_data in df_grouped_plot_data:
            list_data_labels.append(group_name)
            list_dataset.append((group_data[need_data_columnname]).to_numpy(dtype='float')) # get data with type 'float' intentionally
            
        return (list_dataset, list_data_labels)