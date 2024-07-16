# notice other objects about the change of another object

from chart import Chart
from spread_sheet import SpreadSheet
from data_source import DataSource


if __name__ == '__main__':
    data_source = DataSource(0)
    chart = Chart(data_source=data_source)
    spread_sheet = SpreadSheet(data_source=data_source)

    data_source.add_observer(chart)
    data_source.add_observer(spread_sheet)

    data_source.set_val(1)
