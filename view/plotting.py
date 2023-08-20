import sys
import matplotlib
matplotlib.use('QtAgg')

from PyQt6 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class FigureCanVas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=500):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(FigureCanVas, self).__init__(fig)





class Plotting():

    # deliberately set for easy view when embedded plot to MS PPT file
    _maxrow = 2; # maximum row of subplots
    _maxcol = 4; # maximum col of subplots
    _rowsize = 0
    _colsize = 0


    ''' function to get number of row and column from subplotsize
    @param: subplotsize: type int. Quantity of subplots contained inside a subplot
    @return: rowsize: type int. Number of row of subplot grid. Max is 2
             colsize: type int. Number of column of subplot grid. Max is 4
    '''
    def get_subplot_size(self, totalplot) -> tuple[int, int]:

        if totalplot < 4: # subplotsize in [1, 2, 3]
            rowsize = 1
            colsize = totalplot
        elif totalplot == 4:
            rowsize = 2
            colsize = 2
        elif totalplot < 7: # subplotsize in [5, 6]
            rowsize = 2
            colsize = 3
        else: # subplotsize > 7
            rowsize = self._maxrow
            colsize = self._maxcol

        return [rowsize, colsize]
    

    
    """
    Draw plot via Matplotlib module
    """
    @classmethod
    def make_boxplot():

        df_plot_setting_group = df_plot_setting.groupby('Figure', sort=False)
        figname_now = "A arbitrary text. Just to make sure the next figure name is different with this"

        # Iterate through list boxplot names from user setting
        # At each boxplot name, using Plotly to draw boxplot from df_base dataframe
        # df_user_setting_boxplot.shape[0]: rows q'ty of df_user_setting_boxplot

        for i in range(0, df_plot_setting.shape[0]):
            
            df_plotitem = df_plot_setting.iloc[i]
            plotname = str(df_plotitem['Item'])  # name of plot contained in figure
            lowerspec = str(df_plotitem['LSL'])
            upperspec = str(df_plotitem['USL'])
            to_plot = str(df_plotitem['To Plot'])
            figname = str(df_plotitem['Figure']) # name of figure

            # Skip empty boxplot name
            if (not plotname) or (not figname) or to_plot != 'Yes':
                continue
            
            # Create new subplot for each visualization page
            if figname != figname_now:
                try:
                    # get quantity of how many boxplot items in the this Figure
                    fig_setting_size = df_plot_setting_group.get_group(name=figname).shape[0]
                    [fig_rowsize, fig_colsize] =  get_figure_gridsize(fig_setting_size)
                    total_plot = min(fig_setting_size, (fig_rowsize * fig_colsize))                                                                             

                    # make subplots grid with rowsize, colsize get from above
                    # subplot_titles arg is set as placeholder
                    # each subplot title will be update later
                    fig = make_subplots(rows=fig_rowsize,
                                        cols=fig_colsize, 
                                        subplot_titles=["Subplot Title"] * fig_rowsize * fig_colsize)
                    plot_idx = 0  # reset counting plot
                    row_pos, col_pos = 1, 1 # reset plot position in Figure grid
                    figname_now = figname # update the figname to the most recent one

                except Exception as groupby_err:
                    print("\n")
                    print("Error occurred: ")
                    print("File: " + plot_setting_filename + ": column 'Figure': Row " + plotname + " : is " + str(groupby_err))
                    print("\n")
                    continue

            # make plot and add it to current figure
            plot = go.Box(x=df_base['NEST_ID'], # this should be sent from Model to View class
                        y=df_base[plotname ], # this should be sent from Model to View class
                        fillcolor='steelblue',
                        text=plotname,
                        marker={"symbol":"x-thin-open"})
            # add plot to the figure if figure plot slot available
            if plot_idx < total_plot:
                fig.add_trace(plot, row=row_pos, col=col_pos)

                # add horizontal line as reference line to plot
                if lowerspec != 'nan':
                    try:
                        lsl = float(lowerspec)
                        fig.add_hline(y=lsl, row=row_pos, col=col_pos, line_dash="dot", line_width=1, line_color="red")
                    except:
                        pass

                if upperspec != 'nan':
                    try:
                        usl = float(upperspec)
                        fig.add_hline(y=usl, row=row_pos, col=col_pos, line_dash="dot", line_width=1, line_color="red")
                    except:
                        pass

                # update subplot title
                fig.layout.annotations[plot_idx].text = plotname
                plot_idx += 1

                # Adjust row_pos, col_pos for next plot on subplot grid
                col_pos += 1 # set next subplot pos at next cell in Figure grid
                if col_pos > fig_colsize:
                    row_pos += 1 # jump to next row in subplot grid
                    col_pos = 1 # move back to first column in subplot grid

            # if all plots have been placed to Figure grid, then update, show, export it
            if plot_idx == total_plot:
                # fig.update_traces(line_color='black', 
                #                   line_width=0.5)
                
                fig.update_layout(title=("<b>" + figname + "</b>"), # font bold
                                font_family="Times New Roman",
                                font_color='black',
                                title_x=0.5,
                                title_font_size=20,
                                title_font_color='blue',
                                showlegend=False,
                                plot_bgcolor='white', 
                                paper_bgcolor = 'lightgrey')

                fig.write_html(figname + ".html", auto_open=True, include_plotlyjs='directory')