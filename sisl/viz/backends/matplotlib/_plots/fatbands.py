from ....plots import FatbandsPlot
from .bands import MatplotlibBandsBackend
from ...templates import FatbandsBackend


class MatplotlibFatbandsBackend(MatplotlibBandsBackend, FatbandsBackend):

    def _draw_band_weights(self, x, y, weights, name, color, is_group_first):

        self.axes.fill_between(
            x, y + weights, y - weights,
            color=color, label=name
        )

FatbandsPlot.backends.register("matplotlib", MatplotlibFatbandsBackend)