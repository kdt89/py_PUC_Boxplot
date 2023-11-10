from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QDateEdit
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from view.ui.PlotFigure_ui import Ui_PlotFigure
from view.pyqt6_verticalTabWidget import VerticalTabWidget

from typing import List
from controller.setting import FigureConfig
from model.csv_database import CSV_Database


"""
- UI components struture of Plot Figure widget:
- Main widget
    - Tabview object (dtype: QTabview)
        - Tab object (dtype: Qwidget)
            - Layout object (dtype: QFormLayout | QVBoxlayout)
                - Figure object (dtype: figure returned by matplotlib.pyplot.subplot)
                    - Box plot object (dtype: figure returned by matplotlib.pyplot.boxplot)
"""

class WidgetPlotFigure(QWidget):

    def __init__(self):
        super(WidgetPlotFigure, self).__init__()
        self.ui = Ui_PlotFigure()
        self.ui.setupUi(self)
        
        # Add vertical Tab docker widget
        self.pages = List[QWidget]
        self.viewtabs = VerticalTabWidget()
        self.ui.layoutMain.addWidget(self.viewtabs)

        """
        Test only
        """
        # contact pane
        # contact_page = QWidget(self)
        # layout = QFormLayout()
        # layout.addRow('Phone Number:', QLineEdit(self))
        # layout.addRow('Email Address:', QLineEdit(self))
        # contact_page.setLayout(layout)

        # # personal page
        # personal_page = QWidget(self)
        # layout = QFormLayout()
        # layout.addRow('First Name:', QLineEdit(self))
        # layout.addRow('Last Name:', QLineEdit(self))
        # layout.addRow('DOB:', QDateEdit(self))
        # personal_page.setLayout(layout)

        # Add Matplotlib figure object to the Widget
        # Figure object is the container for the PyQt graph object
        # test_page = QWidget()
        # figure = plt.figure()
        # canvas = FigureCanvas(figure)
        # # adding canvas to the layout
        # layout = QVBoxLayout()
        # # layout.addWidget(self.canvas)
        # layout.addWidget(canvas)
        # test_page.setLayout(layout)

        # # Add vertical tab view widget
        # viewtabs = VerticalTabWidget()
        # viewtabs.addTab(personal_page, "First Tab")
        # viewtabs.addTab(contact_page, "First Tab")
        # viewtabs.addTab(test_page, "First Tab")

        # mainLayout = QFormLayout()
        # # mainLayout.addWidget(viewtabs)
        # self.ui.layoutMain.addWidget(viewtabs)

    def add_page(
            self,
            figure: Figure | FigureCanvas,
            title: str
            ) -> None:
        
        layout = QFormLayout()
        layout.addWidget(figure)

        new_page = QWidget()
        new_page.setLayout(layout)

        self.viewtabs.addTab(new_page, title)
        self.pages.append(new_page)
        
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
        
        # Create the subplot figure
        fig, axs = plt.subplots(row_size, col_size)
            
        plot_idx: int = 0
        
        for plot in figure_config.subplot_list:
            if not plot.to_plot:
                continue
        
            dataset_labels, dataset_list = plot_dataset.get_groupdata_at_column(
                groupby_columnname=CSV_Database.DATASET_NAME_HEADER,
                need_data_columnname=plot.subplotname)
            
            if dataset_list is None or dataset_labels is None:
                continue
            axs[plot_idx].boxplot(
                x=dataset_list,
                labels=dataset_labels
            )
            
            plot_idx += 1
        
        return fig
    

    def build_plot_pages(
            self,
            pages_config: List[FigureConfig],
            plot_dataset: CSV_Database
    ) -> None:       
            
        for page_config in pages_config:
            new_page = FigureCanvas(self.build_subplot_figure(
                figure_config=page_config,
                plot_dataset=plot_dataset
            ))

            self.add_page(
                figure=new_page,
                title=page_config.title
            )
            
            # get data from database to make box plot















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