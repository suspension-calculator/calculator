# src/suspension/ui/plots/suspension_plots.py
class SuspensionPlot(PlotContainer):
    """Specialized plot for suspension visualization"""

    def setup_axes(self):
        """Configure axes for suspension plots"""
        pass

    def draw_linkage(self, geometry: LinkGeometry):
        """Draw suspension linkage"""
        pass


class AnalysisPlot(PlotContainer):
    """Plot for analysis results"""

    def plot_results(self, results: AnalysisResults):
        """Plot analysis results"""
        pass
