from __future__ import annotations
from typing import List
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QFormLayout

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # for embedded plot to PyQt
import matplotlib.pyplot as plt # for rendering plot
from matplotlib.figure import Figure
from view.pyqt6_verticalTabWidget import VerticalTabWidget

from view.ui.PlotFigure_ui import Ui_PlotFigure
from controller.setting import FigureConfig, Setting
from model.csv_database import CSV_Database


"""
Customize Matplotlib style with rcParams
"""
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['boxplot.flierprops.linewidth'] = 0.3
plt.rcParams['boxplot.flierprops.marker'] = 'x'
plt.rcParams['boxplot.flierprops.markersize'] = 1.5
plt.rcParams['boxplot.flierprops.markeredgewidth'] = 0.2
plt.rcParams['boxplot.flierprops.markerfacecolor'] = 'grey'
plt.rcParams['boxplot.showcaps'] = False
plt.rcParams['boxplot.whiskerprops.linewidth'] = 0.3

# CONFIGURE COLOR OF BOX BODY
plt.rcParams['boxplot.boxprops.linewidth'] = 0.3
plt.rcParams['boxplot.boxprops.color'] = 'black'
plt.rcParams['boxplot.patchartist'] = True
plt.rcParams['patch.facecolor'] = 'lightgray'
plt.rcParams['boxplot.medianprops.color'] = 'black'
plt.rcParams['boxplot.medianprops.linewidth'] = 0.3

# CONFIGURE SUBPLOT TITLE
plt.rcParams['axes.titlecolor'] = 'black'       # Set color for subplot title
plt.rcParams['axes.titleweight'] = 'normal'       # Set font weight for subplot title
plt.rcParams['axes.titlesize'] = 6              # Set font size for subplot title
plt.rcParams['axes.titlepad'] = 2.0             # pad between axes and title in points
plt.rcParams['xtick.labelcolor'] = 'black'      # set boxplot x-axis label color
plt.rcParams['xtick.labelsize'] = 5             # set boxplot x-axis label font size
plt.rcParams['ytick.labelsize'] = 5             # set boxplot y-axis label font size
plt.rcParams['xtick.bottom'] = False
plt.rcParams['xtick.major.pad'] = 0             # distance to major tick label in points
plt.rcParams['ytick.major.width'] = 0.2         # major tick width in points
plt.rcParams['ytick.major.size'] = 1.5          # major tick width in points
# plt.rcParams['xtick.minor.width:'] = 0.6      # minor tick width in points
#ytick.minor.size:    2       # minor tick size in points
#ytick.minor.width:   0.6     # minor tick width in points

# plt.rcParams['figure.labelsize'] = '3'
# plt.rcParams['figure.labelweight'] = 'bold'
# CONFIGURE BOXPLOT TITLE AND LABEL
plt.rcParams['figure.titlesize'] = '7'
plt.rcParams['figure.titleweight'] = 'bold'
# plt.rcParams['figure.figsize'] = [300, 230]
# plt.rcParams['figure.figsize'] = [10.5, 4.5]
plt.rcParams['figure.dpi'] = 200                # fit full-screen viewing
plt.rcParams['figure.edgecolor'] = 'red'
plt.rcParams['figure.subplot.wspace'] = 0.3     # set subplot width-space
plt.rcParams['figure.subplot.hspace'] = 0.4     # set subplot height-space
plt.rcParams['figure.subplot.bottom'] = 0.05    # set subplot bottom margin
plt.rcParams['figure.subplot.left'] = 0.08      # set subplot left margin

# CONFIGURE THE LINE WIDTH OF SUBPLOT FRAME LINE
# plt.rcParams['patch.linewidth'] = 0.5
# plt.rcParams['patch.edgecolor'] = 'red'
# plt.rcParams['patch.force_edgecolor'] = True
plt.rcParams['axes.edgecolor'] = 'lightgray'
plt.rcParams['axes.linewidth'] = 0.5
plt.rcParams['axes.labelpad'] = 2.0             # space between label and axis


## ***************************************************************************
## * SAVING FIGURES                                                          *
## ***************************************************************************
## The default savefig parameters can be different from the display parameters
## e.g., you may want a higher resolution, or to make the figure
## background white
plt.rcParams['savefig.dpi'] = 300                   # figure dots per inch or 'figure'
plt.rcParams['savefig.facecolor'] = 'auto'          # figure face color when saving
plt.rcParams['savefig.edgecolor'] = 'auto'          # figure edge color when saving
plt.rcParams['savefig.format'] = 'png'         # {png, ps, pdf, svg}
# savefig.pad_inches:  0.1       # padding to be used, when bbox is set to 'tight'
# default directory in savefig dialog, gets updated after
# interactive saves, unless set to the empty string (i.e.
# the current directory); use '.' to start at the current
# directory but update after interactive saves
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['savefig.transparent'] = False         # whether figures are saved with a transparent background by default
plt.rcParams['savefig.orientation'] = 'portrait'    # orientation of saved figure, for PostScript output only


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
        self.figures: List[tuple[str, Figure]] = []
        
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

        return fig


    def build_plot_pages(
            self,
            pages_config: List[FigureConfig],
            plot_dataset: CSV_Database
    ) -> None:
        for page_config in pages_config:
            new_fig = self.build_subplot_figure(plot_dataset=plot_dataset, figure_config=page_config)
            self.add_page(add_figure=new_fig, title=page_config.title)
            self.figures.append((page_config.name, new_fig))


    def closeEvent(self, a0: QtGui.QCloseEvent | None) -> None:
        # intentionally close all current existing matplotlib.pyplot figures explicitly
        # to save memory and prevent Matplotlib module from warning about unclosed figures
        plt.close('all')

        return super().closeEvent(a0)
    

    # def exportFigures(self) -> None:
    #     for fig in self.figures:
    #         print(fig.get

    """
    EXTRA FUNCTION
    """
    def exportFigure(self) -> None:
        for figname, fig in self.figures:
            fig.savefig(
                fname=Setting.OUTPUT_DIR + "\\" + figname,
                pad_inches=0.05)





