from datetime import datetime
from MetaTrader5 import *
import pytz
import matplotlib.pyplot as plt
import pandas as pd

# timezone = pytz.timezone('America/Sao_Paulo')

utc = pytz.timezone('UTC')

# connect to MetaTrader 5
MT5Initialize()
# wait till MetaTrader 5 establishes connection to the trade server and synchronizes the environment
MT5WaitForTerminal()

# request connection status and parameters
print(MT5TerminalInfo())
# get data on MetaTrader 5 version
print(MT5Version())

# request 1000 ticks from series continues of future contract of IBOV index (WIN$N)
win_ticks = MT5CopyTicksFrom("WIN$N", datetime(day=20, month=1, year=2020, hour=9, minute=10, tzinfo=utc), 10000, MT5_COPY_TICKS_ALL)
# request ticks from series continues of future contract of dollar within 2019.04.01 09:00 - 2019.04.02 18:00
wdo_ticks = MT5CopyTicksRange("WDO$N", datetime(2019, 4, 1, 9, tzinfo = utc), datetime(2019, 4, 2, 18, tzinfo = utc), MT5_COPY_TICKS_ALL)

# get bars from different symbols in a number of ways
petr4_rates = MT5CopyRatesFrom("PETR4", MT5_TIMEFRAME_H1, datetime(2019, 4, 5, 15, tzinfo = utc), 1000)
radl3_rates = MT5CopyRatesFromPos("RADL3", MT5_TIMEFRAME_H1, 0, 1000)
ibov_rates = MT5CopyRatesRange("IBOV", MT5_TIMEFRAME_H1, datetime(2019, 4, 1, 13, tzinfo = utc), datetime(2019, 4, 2, 13, tzinfo = utc))
# shut down connection to MetaTrader 5
MT5Shutdown()

# DATA
print('win_ticks(', len(win_ticks), ')')
for val in win_ticks[:10]:
    print(val)

print('wdo_ticks(', len(wdo_ticks), ')')
for val in wdo_ticks[:10]:
    print(val)

print('petr4_rates(', len(petr4_rates), ')')
for val in petr4_rates[:10]:
    print(val)

print('radl3_rates(', len(radl3_rates), ')')
for val in radl3_rates[:10]:
    print(val)

print('ibov_rates(', len(ibov_rates), ')')
for val in ibov_rates[:10]:
    print(val)

win_ticks_frame = pd.DataFrame(win_ticks)

print(win_ticks_frame)

# PLOTTING
x_time = [x for x in win_ticks_frame[0]]
# prepare Bid and Ask arrays
bid = [y.bid for y in win_ticks]
ask = [y.ask for y in win_ticks]

# draw ticks on the chart
plt.plot(x_time, ask, 'r-', label='ask')
plt.plot(x_time, bid, 'g-', label='bid')
# display legends
plt.legend(loc='upper left')
# display header
plt.title('WIN$N ticks')
# display the chart
plt.show()
