from __future__ import annotations
from typing import List
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QFormLayout
import numpy as np

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # for embedded plot to PyQt
import matplotlib.pyplot as mpl
from matplotlib import patches, ticker
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from matplotlib.axis import Axis

from view.ui.PlotFigure_ui import Ui_PlotFigure
from controller.setting import Setting
from model.csv_database import CSV_Database
from model.figureconfig import FigureConfig
from util.image_embed_pptx import ImageEmbedPPTX


"""
Customize Matplotlib style with rcParams
"""
# CONFIGURE LINE STYLE (Ref LINE of BOX PLOT)
mpl.rcParams['lines.linewidth'] = 0.5
mpl.rcParams['lines.color'] = 'red'
mpl.rcParams['lines.linestyle'] = '--'

# CONFIGURE COLOR OF OUTLIERS
mpl.rcParams['boxplot.flierprops.linewidth'] = 0.3
mpl.rcParams['boxplot.flierprops.marker'] = 'x'
mpl.rcParams['boxplot.flierprops.markersize'] = 2.5
mpl.rcParams['boxplot.flierprops.markeredgewidth'] = 0.3
mpl.rcParams['boxplot.flierprops.markerfacecolor'] = 'grey'
mpl.rcParams['boxplot.showcaps'] = False
mpl.rcParams['boxplot.whiskerprops.linewidth'] = 0.4

# CONFIGURE COLOR OF BOX BODY
mpl.rcParams['boxplot.boxprops.linewidth'] = 0.4
mpl.rcParams['boxplot.boxprops.color'] = 'black'
mpl.rcParams['boxplot.patchartist'] = True
mpl.rcParams['patch.facecolor'] = 'lightgray'
mpl.rcParams['boxplot.medianprops.color'] = 'black'
mpl.rcParams['boxplot.medianprops.linewidth'] = 0.4

# CONFIGURE SUBPLOT TITLE
mpl.rcParams['axes.edgecolor'] = 'gray'
mpl.rcParams['axes.linewidth'] = 0.3
mpl.rcParams['axes.labelpad'] = 4               # space between label and axis
mpl.rcParams['axes.titlecolor'] = 'black'       # Set color for subplot title
# mpl.rcParams['axes.titleweight'] = 'bold'     # Set font weight for subplot title
mpl.rcParams['axes.titlesize'] = 8              # Set font size for subplot title
mpl.rcParams['axes.titlepad'] = 4               # pad between axes and title in points
mpl.rcParams['axes.grid'] = True                

mpl.rcParams['polaraxes.grid'] = True
mpl.rcParams['xtick.labelcolor'] = 'black'      # set boxplot x-axis label color
mpl.rcParams['xtick.labelsize'] = 7             # set boxplot x-axis label font size
mpl.rcParams['xtick.bottom'] = False
mpl.rcParams['xtick.major.pad'] = 0             # distance to major tick label in points

mpl.rcParams['ytick.labelsize'] = 7             # set boxplot y-axis label font size
mpl.rcParams['ytick.major.width'] = 0.2         # major tick width in points
mpl.rcParams['ytick.major.size'] = 1.5          # major tick width in points

# CONFIGURE BOXPLOT TITLE AND LABEL
mpl.rcParams['figure.titlesize'] = '8'
mpl.rcParams['figure.autolayout'] = True
mpl.rcParams['figure.constrained_layout.h_pad'] =  0.8
mpl.rcParams['figure.constrained_layout.w_pad'] =  0.5
mpl.rcParams['figure.dpi'] = 200                # fit full-screen viewing
mpl.rcParams['font.family'] = 'tahoma'

mpl.rcParams['grid.color'] = 'lightgray'        # grid color
mpl.rcParams['grid.linestyle'] = 'solid'
mpl.rcParams['grid.linewidth'] = 0.1            # in points

## ***************************************************************************
## * SAVING FIGURES                                                          *
## ***************************************************************************
## The default savefig parameters can be different from the display parameters
## e.g., you may want a higher resolution, or to make the figure
## background white
mpl.rcParams['savefig.dpi'] = 300                   # figure dots per inch or 'figure'
mpl.rcParams['savefig.facecolor'] = 'auto'          # figure face color when saving
mpl.rcParams['savefig.edgecolor'] = 'auto'          # figure edge color when saving
mpl.rcParams['savefig.format'] = 'png'         # {png, ps, pdf, svg}
mpl.rcParams['savefig.bbox'] = 'tight'
mpl.rcParams['savefig.transparent'] = False         # whether figures are saved with a transparent background by default
mpl.rcParams['savefig.orientation'] = 'portrait'    # orientation of saved figure, for PostScript output only

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
        self.bindingSignal2Slot()
        self.list_figures: List[tuple[str, Figure]] = []


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


    def build_figure_pages(
            self,
            figureconfig_list: List[FigureConfig],
            plot_dataset: CSV_Database,
            userset_label_list: List[str]
            ) -> None:

        for figureconfig in figureconfig_list:
            new_fig = self.build_figure(
                dataset=plot_dataset,
                figure_config=figureconfig,
                userset_label_list=userset_label_list)
            self.add_page(add_figure=new_fig, title=figureconfig.title)
            self.list_figures.append((figureconfig.name, new_fig))


    def build_figure(
            self, 
            figure_config: FigureConfig,
            dataset: CSV_Database,
            userset_label_list: List[str]
            ) -> Figure:
        # Validate the subplot size
        row_size, col_size = figure_config.size
        if col_size <= 0:
            return None

        fig, axs = mpl.subplots(nrows=row_size, ncols=col_size)
        plot_idx: int = 0

        # Decide how we should make plot with user set data label list or not
        if userset_label_list is None or len(userset_label_list) == 0:
            use_userset_label_list = False
        else:
            use_userset_label_list = True

        for plot in figure_config.plotconfig_list:
            if plot.to_plot is False:
                continue

            ax = axs.flat[plot_idx]
            dataset_list, datalabel_list = dataset.get_groupdata_at_column(
                groupby_columnname=CSV_Database.DATASET_ID_COLUMN_NAME,
                need_data_columnname=plot.item_name)

            if datalabel_list is None or dataset_list is None:
                continue

            # Compare user set data label list and dataset label list
            # if 'user set' data label list have same list elements with 'dataset' label list
            # then use 'user set' data label list when making plot (as user expect data label order in result Plot)
            if use_userset_label_list:
                if set(userset_label_list) == set(datalabel_list):
                    datalabel_list = userset_label_list
                else:
                    pass

            # Remove NaN values from each dataset
            # otherwise the Matplotlib boxplot will draw blank figure
            dataset_list = [array[~np.isnan(array)] for array in dataset_list]

            # Create the boxplot
            bp = ax.boxplot(x=dataset_list, labels=datalabel_list)
            ax.set_title(label=plot.title)
            
            # rotate x-axis label if user specify
            ax.tick_params(axis='x', labelrotation=45)

            # set title and add reference line (USL/LSL)
            # set y-axis label tick format (float to 2 decimal places)
            if (plot.lowerspec != None and isinstance(plot.lowerspec, (int, float))):
                ax.axhline(y=plot.lowerspec, linewidth=0.4)

            if (plot.upperspec != None and isinstance(plot.upperspec, (int, float))):
                ax.axhline(y=plot.upperspec, linewidth=0.4)
                yticklabel_format = "{{x:.{0}f}}".format(len(str(plot.upperspec).split('.')[1]))
                ax.yaxis.set_major_formatter(ticker.StrMethodFormatter(yticklabel_format))

            # add annotation for Boxplot median values
            plot_idx += 1

        # Standardize the figure size to fit MS PPT report
        WidgetPlotFigure.figure_sizefit(
            figure=fig,
            nrows=row_size,
            ncols=col_size,
            width_height_ratio= Setting.WIDTH_HEIGHT_RATIO,
            max_width= Setting.MAX_WIDTH,
            max_height=Setting.MAX_HEIGHT)

        # Add bounding box to figure
        # WidgetPlotFigure.drawFigureBbox(figure=fig, axes=axs)

        return fig


    def closeEvent(self, a0: QtGui.QCloseEvent | None) -> None:
        # intentionally close all current existing matplotlib.pyplot figures explicitly
        # to save memory and prevent Matplotlib module from warning about unclosed figures
        mpl.close('all')
        return super().closeEvent(a0)


    """
    EXTRA FUNCTION
    """
    def exportFigure2Image(self) -> None:
        for figname, fig in self.list_figures:
            figname = Setting.OUTPUT_DIR + "\\" + figname + ".png"
            fig.savefig(fname=figname, pad_inches=0.05)
            # save figure name to list for future use
            Setting.LIST_FIGURE_IMAGES.append(figname)


    def exportFigure2PPTX(self) -> None:
        print('Exporting figure to PPTX...')
        img2pptx = ImageEmbedPPTX()
        img2pptx.clearAllShapes()
        img2pptx.exportImages2PPTX()


    @staticmethod
    def figure_sizefit(
            figure: Figure,
            nrows: int,
            ncols: int,
            width_height_ratio: float, # width/height ratio
            max_width: float,
            max_height: float
            ) -> Figure:
        if max_width <= 0 or max_height <= 0:
            # raise ValueError("max_width and max_height should be greater than 0")
            return

        # get current figure width and height
        figwidth = figure.get_figwidth()
        figheight = figure.get_figheight()

        # STANDARDIZE SUBPLOT/FIGURE WIDTH PER HEIGHT PROPORTION
        # calculate size of single subplot
        subplot_width = figwidth / ncols
        # subplot_height = figheight / nrows

        # adjust figure height to comply with specified Ratio
        subplot_height = subplot_width / width_height_ratio

        # calculate figure width and height from subplot size
        figheight = subplot_height * nrows
        figwidth = subplot_width * ncols

        # scale figure size to max fit with max_width and max_height
        width_scale = max_width / figwidth
        height_scale = max_height / figheight
        scale = min(width_scale, height_scale)

        new_figwidth = figwidth * scale
        new_figheight = figheight * scale

        # resize the figure to new size fit with max_width, max_height
        figure.set_figwidth(new_figwidth)
        figure.set_figheight(new_figheight)

        return


    @staticmethod
    def drawFigureBbox(figure: Figure, axes: Axes) -> None:
        # Get the bounding boxes of the axes including text decorations
        axes_shape = np.atleast_2d(axes).shape
        renderer = figure.canvas.get_renderer()
        get_bbox = lambda ax: ax.get_tightbbox(renderer).transformed(figure.transFigure.inverted())
        bboxes = list(map(get_bbox, axes.flat))

        #Get the minimum and maximum extent, get the coordinate half-way between those
        ymax = np.array(list(map(lambda b: b.y1, bboxes))).reshape(axes_shape).max(axis=1)
        ymin = np.array(list(map(lambda b: b.y0, bboxes))).reshape(axes_shape).min(axis=1)
        ys = np.c_[ymax[1:], ymin[:-1]].mean(axis=1)

        # Draw a horizontal lines at those coordinates
        for y in ys:
            line = mpl.Line2D(
                [0,1],[y,y],
                linestyle = 'solid',
                linewidth = 0.1,
                transform = figure.transFigure, 
                color = 'black')
            figure.add_artist(line)

        return None


    @staticmethod
    def drawAxisBbox(figure: Figure, axis: Axis) -> None:
        # Get the bounding boxes of the axes including text decorations
        renderer = figure.canvas.get_renderer()
        bbox = axis.get_tightbbox(renderer).transformed(figure.transFigure.inverted())
        rec = patches.Rectangle(
            xy=(bbox.x0, bbox.y0),
            width=bbox.width,
            height=bbox.height,
            lw=1,
            edgecolor="red",
            facecolor="none",
            fill=False)
        axis.add_patch(rec)

        return None


    @staticmethod
    def __removeArrayNAN(in_array: np.ndarray) -> np.ndarray:
        """
        Remove NaN values from the input numpy array and return the cleaned array.

        Parameters:
            in_array (np.ndarray): The input numpy array with NaN values.

        Returns:
            np.ndarray: The cleaned numpy array with NaN values removed.
        """
        return in_array[~np.isnan(in_array)]


    # binding Action to function
    def bindingSignal2Slot(self) -> None:
        self.ui.btn_exportPPTX.clicked.connect(self.ui.actionExportGraph2PPTX.trigger)
        self.ui.actionExportGraph2PPTX.triggered.connect(self.exportFigure2PPTX)