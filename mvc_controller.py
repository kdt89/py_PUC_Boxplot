from __future__ import annotations
import mvc_model
import mvc_view
from controller.setting import Setting
from controller.workstatus import Status


class Controller():  # Controller in MVC pattern

    def __init__(self, model: mvc_model.Model, view: mvc_view.View):
        self.model = model
        self.view = view
        self.setting = Setting()
        self.bindSignalAndSlot()
        # Show initial message to UI
        self.view.Main.updateUI_messagebox(f"<b>Program initialized at: </b> \
                                  <font color='blue'>{self.setting.ROOTDIR}\
                                  </font>")

    def export_database(self) -> None:
        self.model.database.export_to_local(Setting.OUTPUT_DIR)

    def build_boxplot(self) -> None:
        self.view.wxPlotFigure_newWidget()
        if self.view.PlotFigure == None:
            return

        self.view.PlotFigure.callbackMessageThrower = self.view.Main.updateUI_messagebox
        self.view.PlotFigure.build_figure_pages(
            figureconfig_list=self.model.figureconfig_list.list,
            plot_dataset=self.model.database,
            userset_label_list=Setting.PLOTCONFIG_DATASET_NAME_LIST,
            userset_label_rotation=Setting.OPTS_PLOTCONFIG_DATASET_LABEL_ROTATION)

        self.view.PlotFigure.exportFigure2Image()
        self.view.PlotFigure.showMaximized()

    """ Grab matched files in Input folder and pass to Model object to import to database """

    def import_input_data(self) -> None:
        # update Setting from user
        self.view.Main.updateUI_messagebox("- User setting loaded")
        input_status_files_count = len(Status.DATA_INPUT_FILE_LIST)

        if input_status_files_count > 0:
            self.view.Main.updateUI_messagebox(
                f"- Found {input_status_files_count} data files to be input")
            Status.INPUT_READY = True
        else:
            Status.INPUT_READY = False
            self.view.Main.updateUI_messagebox(
                "There are no data files in Input directory")
            return None

        # Import data from input folder to Database of Model
        self.model.database.import_csv_files(
            filepaths=Status.DATA_INPUT_FILE_LIST,
            reading_cols=self.model.figureconfig_list.DATA_IMPORT_COLUMN_LIST,
            skip_rows=Setting.OPTS_DATACONFIG_IMPORT_SKIP_ROW,
            callbackMessage=self.view.Main.updateUI_statusbar)

        rows, columns = self.model.database.size
        self.view.Main.updateUI_messagebox(
            f"- Input data imported successfully: {rows} rows - {columns} columns")

        # Define methods execute when occuring Event from View
    def actionMakePlot_procedure(self):
        """
        Action for making a plot from data files in the Input directory. 
        This function updates the message on the UI, updates the figure configuration list, and updates the status. 
        It then imports input data, checks if the input is ready, and updates the status bar. 
        Finally, it exports the database and builds a boxplot.
        """
        # Notice to UI
        self.view.Main.updateUI_messagebox(
            f"\n <b>Making Plot from data files in Input directory</b>...")
        self.model.figureconfig_list.update()
        Status.update()
        Status.LIST_FIGURE_IMAGES.clear()
        Setting.PLOTCONFIG_DATASET_NAME_LIST = self.view.Main.getfromUI_datasetNameList_txtEdit()

        self.import_input_data()
        if not Status.INPUT_READY:
            self.view.Main.updateUI_messagebox(
                "There are no data files in Input directory")  # status bar
            return None

        self.export_database()
        self.build_boxplot()

    def actionLoadDatasetName_procedure(self) -> None:
        # Load detected dataset name (from Input folder) to UI (main window)
        Status.update()
        self.view.Main.updateUI_datasetNameList_txtEdit(
            Status.DETECTED_DATASET_NAME_LIST)

    def actionShowPreference_procedure(self) -> None:
        self.view.Preference.setUI_preference(
            Setting.OPTS_PLOTCONFIG_DATASET_LABEL_ROTATION,
            Setting.OPTS_PLOTCONFIG_SHOW_MEDIAN,
            Setting.OPTS_DATACONFIG_IMPORT_SKIP_ROW)
        self.view.Preference.show()

    # Save user preference
    def actionSavePreference_procedure(self) -> None:
        [rotation, showMedian, rowskip] = self.view.Preference.getUI_preference()
        self.setting.saveSetting(rotation, showMedian, rowskip)

    """
    Binding PyQt signal & slot
    """

    def bindSignalAndSlot(self):
        self.view.Main.ui.actionMakePlot.triggered.connect(
            self.actionMakePlot_procedure)
        self.view.Main.ui.actionLoadDatasetName.triggered.connect(
            self.actionLoadDatasetName_procedure)
        self.view.Main.ui.actionShowPreference.triggered.connect(
            self.actionShowPreference_procedure)
        self.view.Preference.ui.actionSavePreference.triggered.connect(
            self.actionSavePreference_procedure)
