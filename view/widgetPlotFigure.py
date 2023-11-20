from __future__ import annotations
from typing import List
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QSizePolicy, QTabWidget

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # for embedded plot to PyQt
import matplotlib.pyplot as plt # for rendering plot
from matplotlib.figure import Figure
from test_only.Test3 import replace_special_characters # for rendering plot
from view.pyqt6_verticalTabWidget import VerticalTabWidget

from view.ui.PlotFigure_ui import Ui_PlotFigure
from controller.setting import FigureConfig
from model.csv_database import CSV_Database


"""
Customize Matplotlib style with rcParams
"""
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['boxplot.flierprops.linewidth'] = 0.5
plt.rcParams['boxplot.flierprops.marker'] = 'x'
plt.rcParams['boxplot.flierprops.markersize'] = 2
plt.rcParams['boxplot.flierprops.markeredgewidth'] = 0.3
plt.rcParams['boxplot.flierprops.markerfacecolor'] = 'grey'
plt.rcParams['boxplot.whiskerprops.linewidth'] = 0.5
plt.rcParams['boxplot.showcaps'] = False

# CONFIGURE COLOR OF BOX BODY
plt.rcParams['boxplot.boxprops.linewidth'] = 0.5
plt.rcParams['boxplot.boxprops.color'] = 'black'
plt.rcParams['boxplot.patchartist'] = True
plt.rcParams['patch.facecolor'] = 'cornflowerblue'
plt.rcParams['boxplot.medianprops.color'] = 'black'
plt.rcParams['boxplot.medianprops.linewidth'] = 0.5

# CONFIGURE SUBPLOT TITLE
plt.rcParams['axes.titlecolor'] = 'black'       # Set color for subplot title
plt.rcParams['axes.titleweight'] = 'normal'     # Set font weight for subplot title
plt.rcParams['axes.titlesize'] = 6              # Set font size for subplot title
plt.rcParams['xtick.labelcolor'] = 'black'      # set boxplot x-axis label color
plt.rcParams['xtick.labelsize'] = 5             # set boxplot x-axis label font size
plt.rcParams['ytick.labelsize'] = 5             # set boxplot y-axis label font size
# plt.rcParams['figure.labelsize'] = '4'
# plt.rcParams['figure.labelweight'] = 'bold'

# CONFIGURE BOXPLOT TITLE AND LABEL
plt.rcParams['figure.titlesize'] = '10'
plt.rcParams['figure.titleweight'] = 'bold'
# plt.rcParams['figure.figsize'] = [300, 230]
plt.rcParams['figure.figsize'] = [10.5, 4.5]
plt.rcParams['figure.dpi'] = 200                # fit full-screen viewing
plt.rcParams['figure.edgecolor'] = 'red'
plt.rcParams['figure.subplot.wspace'] = 0.5     # set subplot width-space
plt.rcParams['figure.subplot.hspace'] = 0.4     # set subplot height-space
plt.rcParams['figure.subplot.bottom'] = 0.05    # set subplot bottom margin
plt.rcParams['figure.subplot.left'] = 0.08      # set subplot left margin

# CONFIGURE THE LINE WIDTH OF SUBPLOT FRAME LINE
# plt.rcParams['patch.linewidth'] = 0.5
# plt.rcParams['patch.edgecolor'] = 'red'
# plt.rcParams['patch.force_edgecolor'] = True
plt.rcParams['axes.edgecolor'] = 'lightgray'
plt.rcParams['axes.linewidth'] = 0.5


# plt.rcParams['figure.subplot.right'] = 0.1        # set subplot right margin


"""
- UI components struture of Plot Figure widget:
- Main widget
    - Tabview object (dtype: QTabview)
        - Tab object (dtype: Qwidget)
            - Layout object (dtype: QFormLayout | QVBoxlayout)
                - Figure object (dtype: figure returned by matplotlib.pyplot.subplot)
                    - Box plot object (dtype: figure returned by matplotlib.pyplot.boxplot)

* Embedding matplotlib figure object to PyQt Widget form
- Make 'figure' = Figure object, returned by matplotlib.pyplot.boxplot() and matplotlib.pyplot.subplots()
- Make canvas = FigureCanvasQTAgg object, returned by FigureCanvasQTAgg(figure)
- Make 'layout' = QFormLayout object, returned by layout.addWidget()
- Make main_widget UI = QWidget, returned by 'main_widget'.setLayout(layout)
"""

class WidgetPlotFigure(QWidget):

    def __init__(self):
        super(WidgetPlotFigure, self).__init__()
        self.ui = Ui_PlotFigure()
        self.ui.setupUi(self)
        self.setLayout(self.ui.gridLayout_main)
        self.ui.tab_plotFigureHolder        
        self.figures: List[Figure] = []
        
        #debug
        # self.vTabs = VerticalTabWidget
        # self.vTabs.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # self.ui.layoutMain.addWidget(self.ui.tabWidget)


    def add_page(
            self,
            add_figure: Figure,
            title: str
            ) -> None:
        canvas = FigureCanvas(add_figure)
        
        layout = QFormLayout()
        layout.addWidget(canvas)
        
        new_page = QWidget()
        new_page.setLayout(layout)
        self.figures.append(new_page)
        self.ui.tab_plotFigureHolder.addTab(new_page, title)


    def build_subplot_figure(
            self, 
            figure_config: FigureConfig,
            plot_dataset: CSV_Database
            ) -> Figure:
        # Validate the subplot size
        row_size, col_size = figure_config.size
        if col_size <= 0:
            return None

        fig, axs = plt.subplots(nrows=row_size, ncols=col_size)
        plot_idx: int = 0
        fig.suptitle(figure_config.title)

        for plot in figure_config.subplot_list:
            if not plot.to_plot:
                continue
        
            list_dataset, list_data_label = plot_dataset.get_groupdata_at_column(
                groupby_columnname=CSV_Database.DATASET_ID_COLUMN_NAME,
                need_data_columnname=plot.item_name)
            
            if list_data_label is None or list_dataset is None:
                continue
            
            axs.flat[plot_idx].boxplot(x=list_dataset, labels=list_data_label)
            axs.flat[plot_idx].set_title(label=plot.title)
            plot_idx += 1
        
        #debug
        print(fig.get_size_inches())
        savefigname = '.\\Output\\' + figure_config.name + '.png'
        print(savefigname)
        fig.savefig(savefigname, transparent=True)

        return fig
    

    def build_plot_pages(
            self,
            pages_config: List[FigureConfig],
            plot_dataset: CSV_Database
    ) -> None:
        for page_config in pages_config:
            new_fig = self.build_subplot_figure(plot_dataset=plot_dataset, figure_config=page_config)
            self.add_page(add_figure=new_fig, title=page_config.title)
            self.figures.append(new_fig)


    def closeEvent(self, a0: QtGui.QCloseEvent | None) -> None:
        # intentionally close all current existing matplotlib.pyplot figures explicitly
        # to save memory and prevent Matplotlib module from warning about unclosed figures
        plt.close('all')

        return super().closeEvent(a0)
    



    """
    EXTRA FUNCTION
    """




