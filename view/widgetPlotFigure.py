from typing import List
# from cProfile import label
from PyQt6 import QtGui
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout

import matplotlib as mpl # for customize matplotlib plot style
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

mpl.rcParams['lines.linewidth'] = 1
mpl.rcParams['boxplot.flierprops.markersize'] = 3
mpl.rcParams['boxplot.flierprops.linewidth'] = 0.5
mpl.rcParams['boxplot.flierprops.marker'] = 'x'
mpl.rcParams['boxplot.flierprops.color'] = 'grey'
mpl.rcParams['boxplot.boxprops.color'] = 'black'
mpl.rcParams['boxplot.boxprops.linewidth'] = 0.5
mpl.rcParams['boxplot.whiskerprops.linewidth'] = 0.5
mpl.rcParams['boxplot.medianprops.color'] = 'black'


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
        
        # Add vertical Tab docker widget
        self.figures: List[Figure] = []
        self.viewtabs = VerticalTabWidget()
        self.ui.layoutMain.addWidget(self.viewtabs)
        # need to check if layoutMain stretches to full Widget successufully yet?
        # 
        # need to check the viewtabs Widget stretchs to full layoutMain yet?


    def add_page(
            self,
            add_figure: Figure,
            title: str
            ) -> None:
        layout = QFormLayout()
        layout.addWidget(FigureCanvas(add_figure))
        new_page = QWidget()
        new_page.setLayout(layout)

        self.figures.append(new_page)
        self.viewtabs.addTab(new_page, title)
        
        return new_page


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

        for plot in figure_config.subplot_list:
            if not plot.to_plot:
                continue
        
            list_dataset, list_data_label = plot_dataset.get_groupdata_at_column(
                groupby_columnname=CSV_Database.DATASET_ID_COLUMN_NAME,
                need_data_columnname=plot.item_name)
            
            if list_data_label is None or list_dataset is None:
                continue
            
            axs.flat[plot_idx].boxplot(
                x=list_dataset,
                labels=list_data_label,
                showcaps=False,
                sym='x')
            axs.flat[plot_idx].set_title(
                label=plot.title,
                fontsize=9,
                fontweight='bold')

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










    # @classmethod
    # def make_boxplot():
    #     """
    #     Draw plot via Matplotlib module
    #     """
    #     df_plot_setting_group = df_plot_setting.groupby('Figure', sort=False)
    #     figname_now = "A arbitrary text. Just to make sure the next figure name is different with this"

    #     # Iterate through list boxplot names from user setting
    #     # At each boxplot name, using Plotly to draw boxplot from df_base dataframe
    #     # df_user_setting_boxplot.shape[0]: rows q'ty of df_user_setting_boxplot

    #     for i in range(0, df_plot_setting.shape[0]):
            
    #         df_plotitem = df_plot_setting.iloc[i]
    #         plotname = str(df_plotitem['Item'])  # name of plot contained in figure
    #         lowerspec = str(df_plotitem['LSL'])
    #         upperspec = str(df_plotitem['USL'])
    #         to_plot = str(df_plotitem['To Plot'])
    #         figname = str(df_plotitem['Figure']) # name of figure

    #         # Skip empty boxplot name
    #         if (not plotname) or (not figname) or to_plot != 'Yes':
    #             continue
            
    #         # Create new subplot for each visualization page
    #         if figname != figname_now:
    #             try:
    #                 # get quantity of how many boxplot items in the this Figure
    #                 fig_setting_size = df_plot_setting_group.get_group(name=figname).shape[0]
    #                 [fig_rowsize, fig_colsize] =  get_figure_gridsize(fig_setting_size)
    #                 total_plot = min(fig_setting_size, (fig_rowsize * fig_colsize))                                                                             

    #                 # make subplots grid with rowsize, colsize get from above
    #                 # subplot_titles arg is set as placeholder
    #                 # each subplot title will be update later
    #                 fig = make_subplots(rows=fig_rowsize,
    #                                     cols=fig_colsize, 
    #                                     subplot_titles=["Subplot Title"] * fig_rowsize * fig_colsize)
    #                 plot_idx = 0  # reset counting plot
    #                 row_pos, col_pos = 1, 1 # reset plot position in Figure grid
    #                 figname_now = figname # update the figname to the most recent one

    #             except Exception as groupby_err:
    #                 print("\n")
    #                 print("Error occurred: ")
    #                 print("File: " + plot_setting_filename + ": column 'Figure': Row " + plotname + " : is " + str(groupby_err))
    #                 print("\n")
    #                 continue

    #         # make plot and add it to current figure
    #         plot = go.Box(x=df_base['NEST_ID'], # this should be sent from Model to View class
    #                     y=df_base[plotname ], # this should be sent from Model to View class
    #                     fillcolor='steelblue',
    #                     text=plotname,
    #                     marker={"symbol":"x-thin-open"})
    #         # add plot to the figure if figure plot slot available
    #         if plot_idx < total_plot:
    #             fig.add_trace(plot, row=row_pos, col=col_pos)

    #             # add horizontal line as reference line to plot
    #             if lowerspec != 'nan':
    #                 try:
    #                     lsl = float(lowerspec)
    #                     fig.add_hline(y=lsl, row=row_pos, col=col_pos, line_dash="dot", line_width=1, line_color="red")
    #                 except:
    #                     pass

    #             if upperspec != 'nan':
    #                 try:
    #                     usl = float(upperspec)
    #                     fig.add_hline(y=usl, row=row_pos, col=col_pos, line_dash="dot", line_width=1, line_color="red")
    #                 except:
    #                     pass

    #             # update subplot title
    #             fig.layout.annotations[plot_idx].text = plotname
    #             plot_idx += 1

    #             # Adjust row_pos, col_pos for next plot on subplot grid
    #             col_pos += 1 # set next subplot pos at next cell in Figure grid
    #             if col_pos > fig_colsize:
    #                 row_pos += 1 # jump to next row in subplot grid
    #                 col_pos = 1 # move back to first column in subplot grid

    #         # if all plots have been placed to Figure grid, then update, show, export it
    #         if plot_idx == total_plot:
    #             # fig.update_traces(line_color='black', 
    #             #                   line_width=0.5)
                
    #             fig.update_layout(title=("<b>" + figname + "</b>"), # font bold
    #                             font_family="Times New Roman",
    #                             font_color='black',
    #                             title_x=0.5,
    #                             title_font_size=20,
    #                             title_font_color='blue',
    #                             showlegend=False,
    #                             plot_bgcolor='white', 
    #                             paper_bgcolor = 'lightgrey')

    #             fig.write_html(figname + ".html", auto_open=True, include_plotlyjs='directory')