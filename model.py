from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats, commonplayerinfo, playergamelog, leaguedashptteamdefend
import pandas as pd
import numpy as np

# Get game-by-game stats for every single player. 
# bron = playergamelog.PlayerGameLog(player_id = '2544', season = '2020')
# bron_df = bron.get_data_frames()[0]
# print(bron_df)

# Fetch team defensive stats for a season
team_defense = leaguedashptteamdefend.LeagueDashPtTeamDefend(season='2022-23', league_id = '00')

# Get the data as a dataframe
team_defense_df = team_defense.get_data_frames()[0]

# Display dataframe
print(team_defense_df)