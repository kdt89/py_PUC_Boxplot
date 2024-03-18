from __future__ import annotations
from typing import List, Callable
from collections import OrderedDict
import pandas as pd
import numpy as np
from pandas import DataFrame
from os import path


# Module to store database
class CSV_Database():

    DATASET_ID_COLUMN_NAME: str = "DATA_FILENAME"

    # Attributes
    def __init__(self) -> None:
        self._csv_data: DataFrame = DataFrame(data=None)

    @property
    def size(self) -> tuple[int, int]:
        return len(self._csv_data.index), len(self._csv_data.columns)

    @property
    def data(self) -> DataFrame:
        return self._csv_data

    @property
    def groupnames(self) -> List[str]:
        return self._csv_data[self.DATASET_ID_COLUMN_NAME].unique()

    def export_to_local(self, output_dir) -> None:
        if self._csv_data.empty:
            return
        else:
            try:
                self._csv_data.to_csv(output_dir + "\\" + "merged data.csv",
                                      header=True,
                                      index=False,
                                      sep=",",
                                      compression=None)
            except Exception as e:
                print(str(e))

    def import_csv_files(
            self,
            filepaths: str,
            reading_cols: List[str],
            skip_rows: List[int],
            callbackMessage: Callable[[str], None]
    ) -> DataFrame:
        """
        Imports data from CSV files, processes the data, and returns the count of imported files. 

        Args:
            filepaths (str): The filepaths of the CSV files to be imported.
            reading_cols (List[str]): The list of columns to be read from the CSV files.
            skip_rows (List[int]): The list of rows to be skipped while reading the CSV files.
            callbackMessage (Callable[[str], None]): A callback function to send messages during the import process.

        Returns:
            DataFrame: The count of imported files.
        """

        if reading_cols is None:
            return

        total_df: List[DataFrame] = []
        imported_count: int = 0

        for filepath in filepaths:
            # splitext() return (filename, extension)
            filename = path.splitext(path.basename(filepath))[0]
            callbackMessage(f"Reading file: {path.basename(filepath)}")

            df_extracted_from_file = pd.DataFrame()
            df_current_chunk = pd.DataFrame()
            found_cols: List[str] = []

            try:
                df_raw_imported = pd.read_csv(
                    filepath, index_col=None, sep=',', header=0, skiprows=skip_rows)
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
                        df_empty_chunk = pd.Series(
                            data=None, name=col, dtype='object')
                        # push it to 'extracted_df'
                        df_extracted_from_file = pd.concat(
                            [df_extracted_from_file, df_current_chunk, df_empty_chunk], axis=1)
                        found_cols.clear()
                        df_current_chunk = None

            # After iterate over all column name in needed_columns, ...
            # if found_colnames is not empty then extract data and push to 'extracted_df'
            if len(found_cols) > 0:
                df_current_chunk = df_raw_imported[found_cols]
                df_extracted_from_file = pd.concat(
                    [df_extracted_from_file, df_current_chunk], axis=1)
                df_extracted_from_file = df_extracted_from_file.drop_duplicates()
                df_extracted_from_file = df_extracted_from_file.dropna(
                    axis=0,  # drop rows which contain missing values
                    how='all',  # if all values of checking columns are NA, drop that row or column
                    subset=None)  # check all columns
                found_cols.clear()
                df_current_chunk = None

            # For later use when making plot, we need to categorize the dataset by its name,...
            # by adding extra column [DATA_FILENAME] with row value is the name of file we extract data from
            df_series_asfilename = pd.Series(
                data=filename,
                dtype='string',
                # range from 0 to number of rows of 'df_extracted_from_file'
                index=range(0, df_extracted_from_file.shape[0]))

            df_extracted_from_file.insert(
                loc=0,  # insert new column as first (left-most) column
                column=CSV_Database.DATASET_ID_COLUMN_NAME,
                value=df_series_asfilename.values)

            # append the dataframe extracted from file to total list dataframe
            if not df_extracted_from_file.empty:
                total_df.append(df_extracted_from_file)
                imported_count += 1
        callbackMessage(f"")

        # Merging data frames into one frame
        # Abandon previous data in self._csv_data and hooked up to newly imported data
        if len(total_df) > 0:
            self._csv_data = pd.concat(total_df, axis=0, ignore_index=True)

        return imported_count

    def from_column(self,
                    column: str,
                    removeNaN: bool = False,
                    sort_data_order_by: List[str] = None
                    ) -> OrderedDict[str, np.ndarray]:
        # Validation the column name to extract data exist in target database or not
        groupby_column = self.DATASET_ID_COLUMN_NAME
        data_columns = self._csv_data.columns
        dataname_list: List[str] = []
        if not column in data_columns:
            return None
        if not groupby_column in data_columns:
            return None

        # Extract data from CSV database
        df_subset_data = self._csv_data[[groupby_column, column]]
        groups_data = df_subset_data.groupby(by=groupby_column, sort=None)

        # filter out the group_name of data by the order of sort_data_order_by
        if sort_data_order_by != None:
            dataname_list = [
                name for name in sort_data_order_by if name in groups_data.groups.keys()]
            if len(dataname_list) == 0:
                dataname_list = groups_data.groups.keys()
        else:
            dataname_list = groups_data.groups.keys()

        retVal = OrderedDict()
        for name in dataname_list:
            # get data with type 'float' intentionally
            key = name
            val = groups_data.get_group(name)[column].to_numpy(dtype='float')

            # remove NaN value in numpy array
            if removeNaN:
                retVal[key] = val[~np.isnan(val)]
            else:
                retVal[key] = val

        return retVal
