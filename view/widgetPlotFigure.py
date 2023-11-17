from typing import List
# from cProfile import label
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # for embedded plot to PyQt
import matplotlib.pyplot as plt # for rendering plot
from matplotlib.figure import Figure # for rendering plot
from view.pyqt6_verticalTabWidget import VerticalTabWidget

from view.ui.PlotFigure_ui import Ui_PlotFigure
from controller.setting import FigureConfig
from model.csv_database import CSV_Database


"""
Customize Matplotlib style with rcParams
"""
## ***************************************************************************
## * BOXPLOT                                                                 *
## ***************************************************************************
#boxplot.notch:       False
#boxplot.vertical:    True
#boxplot.whiskers:    1.5
#boxplot.bootstrap:   None
#boxplot.patchartist: False
#boxplot.showmeans:   False
#boxplot.showcaps:    True
#boxplot.showbox:     True
#boxplot.showfliers:  True
#boxplot.meanline:    False

#boxplot.flierprops.color:           black
#boxplot.flierprops.marker:          o
#boxplot.flierprops.markerfacecolor: none
#boxplot.flierprops.markeredgecolor: black
#boxplot.flierprops.markeredgewidth: 1.0
#boxplot.flierprops.markersize:      6
#boxplot.flierprops.linestyle:       none
#boxplot.flierprops.linewidth:       1.0

#boxplot.boxprops.color:     black
#boxplot.boxprops.linewidth: 1.0
#boxplot.boxprops.linestyle: -

#boxplot.whiskerprops.color:     black
#boxplot.whiskerprops.linewidth: 1.0
#boxplot.whiskerprops.linestyle: -

#boxplot.capprops.color:     black
#boxplot.capprops.linewidth: 1.0
#boxplot.capprops.linestyle: -

#boxplot.medianprops.color:     C1
#boxplot.medianprops.linewidth: 1.0
#boxplot.medianprops.linestyle: -

#boxplot.meanprops.color:           C2
#boxplot.meanprops.marker:          ^
#boxplot.meanprops.markerfacecolor: C2
#boxplot.meanprops.markeredgecolor: C2
#boxplot.meanprops.markersize:       6
#boxplot.meanprops.linestyle:       --
#boxplot.meanprops.linewidth:       1.0


## ***************************************************************************
## * FONT                                                                    *
## ***************************************************************************
## The font properties used by `text.Text`.
## See https://matplotlib.org/stable/api/font_manager_api.html for more information
## on font properties.  The 6 font properties used for font matching are
## given below with their default values.
##
## The font.family property can take either a single or multiple entries of any
## combination of concrete font names (not supported when rendering text with
## usetex) or the following five generic values:
##     - 'serif' (e.g., Times),
##     - 'sans-serif' (e.g., Helvetica),
##     - 'cursive' (e.g., Zapf-Chancery),
##     - 'fantasy' (e.g., Western), and
##     - 'monospace' (e.g., Courier).
## Each of these values has a corresponding default list of font names
## (font.serif, etc.); the first available font in the list is used.  Note that
## for font.serif, font.sans-serif, and font.monospace, the first element of
## the list (a DejaVu font) will always be used because DejaVu is shipped with
## Matplotlib and is thus guaranteed to be available; the other entries are
## left as examples of other possible values.
##
## The font.style property has three values: normal (or roman), italic
## or oblique.  The oblique style will be used for italic, if it is not
## present.
##
## The font.variant property has two values: normal or small-caps.  For
## TrueType fonts, which are scalable fonts, small-caps is equivalent
## to using a font size of 'smaller', or about 83 % of the current font
## size.
##
## The font.weight property has effectively 13 values: normal, bold,
## bolder, lighter, 100, 200, 300, ..., 900.  Normal is the same as
## 400, and bold is 700.  bolder and lighter are relative values with
## respect to the current weight.
##
## The font.stretch property has 11 values: ultra-condensed,
## extra-condensed, condensed, semi-condensed, normal, semi-expanded,
## expanded, extra-expanded, ultra-expanded, wider, and narrower.  This
## property is not currently implemented.
##
## The font.size property is the default font size for text, given in points.
## 10 pt is the standard value.
##
## Note that font.size controls default text sizes.  To configure
## special text sizes tick labels, axes, labels, title, etc., see the rc
## settings for axes and ticks.  Special text sizes can be defined
## relative to font.size, using the following values: xx-small, x-small,
## small, medium, large, x-large, xx-large, larger, or smaller

#font.family:  sans-serif
#font.style:   normal
#font.variant: normal
#font.weight:  normal
#font.stretch: normal
#font.size:    10.0

#font.serif:      DejaVu Serif, Bitstream Vera Serif, Computer Modern Roman, New Century Schoolbook, Century Schoolbook L, Utopia, ITC Bookman, Bookman, Nimbus Roman No9 L, Times New Roman, Times, Palatino, Charter, serif
#font.sans-serif: DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
#font.cursive:    Apple Chancery, Textile, Zapf Chancery, Sand, Script MT, Felipa, Comic Neue, Comic Sans MS, cursive
#font.fantasy:    Chicago, Charcoal, Impact, Western, Humor Sans, xkcd, fantasy
#font.monospace:  DejaVu Sans Mono, Bitstream Vera Sans Mono, Computer Modern Typewriter, Andale Mono, Nimbus Mono L, Courier New, Courier, Fixed, Terminal, monospace

plt.rcParams['lines.linewidth'] = 1
plt.rcParams['boxplot.flierprops.linewidth'] = 0.5
plt.rcParams['boxplot.flierprops.marker'] = 'x'
plt.rcParams['boxplot.flierprops.markersize'] = 3
plt.rcParams['boxplot.flierprops.markeredgewidth'] = 0.4
plt.rcParams['boxplot.flierprops.markerfacecolor'] = 'black'
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
plt.rcParams['figure.figsize'] = [400, 300]
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.edgecolor'] = 'red'
plt.rcParams['figure.subplot.wspace'] = 0.5     # set subplot width-space
plt.rcParams['figure.subplot.hspace'] = 0.4     # set subplot height-space
plt.rcParams['figure.subplot.bottom'] = 0.05       # set subplot bottom margin
plt.rcParams['figure.subplot.left'] = 0.08         # set subplot left margin

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
        self.figures: List[Figure] = []
        #debug
        # self.ui.layoutMain.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        # Add vertical Tab docker widget

        # self.viewtabs = VerticalTabWidget()
        # self.viewtabs.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.ui.layoutMain.addWidget(self.ui.tabWidget)
        self.ui.tabWidget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)


    def add_page(
            self,
            add_figure: Figure,
            title: str
            ) -> None:
        canvas = FigureCanvas(add_figure)
        # canvas.draw()
        
        layout = QFormLayout()
        layout.addWidget(canvas)
        
        new_page = QWidget()
        new_page.setLayout(layout)
        self.figures.append(new_page)
        
        # self.viewtabs.addTab(new_page, title) #debug commented out
        #debug only
        self.ui.tabWidget.addTab(new_page, title)


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
            self.figures.append(new_fig)


    def closeEvent(self, a0: QtGui.QCloseEvent | None) -> None:
        # intentionally close all current existing matplotlib.pyplot figures explicitly
        # to save memory and prevent Matplotlib module from warning about unclosed figures
        plt.close('all')

        return super().closeEvent(a0)



