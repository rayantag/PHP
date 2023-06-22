from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo, playergamelog, leaguedashptteamdefend
import pandas as pd
import numpy as np

# Get game-by-game stats for every single player. 
bron = playergamelog.PlayerGameLog(player_id = '2544', season = '2020')
bron_df = bron.get_data_frames()[0]
print(bron_df)