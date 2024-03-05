

class PlotConfig:

    def __init__(
        self, 
        name: str = "",
        title: str = "",
        lowerspec: float = -1.0,
        upperspec: float = -1.0,
        to_plot: bool = False) -> None:

        self.item_name = name
        self.title = title
        self.to_plot = to_plot

        # validate lowerspec is 'nan'? If it is 'nan' then pass 'None' to constructor
        if lowerspec != lowerspec: # Nan will return true at comparison to itself
            self.lowerspec = None
        else:
            self.lowerspec = lowerspec

        if upperspec != upperspec: # Nan will return true at comparison to itself
            self.upperspec = None
        else:
            self.upperspec = upperspec