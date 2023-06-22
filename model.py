from nba_api.stats.static import players
from nba_api.stats.library.parameters import SeasonAll
from nba_api.stats.endpoints import playergamelog, leaguedashptteamdefend, boxscoredefensive, leaguegamefinder, boxscorematchups
from nba_api.stats.endpoints import defensehub, draftboard, drafthistory, playerawards, playercareerstats, gamerotation
import pandas as pd
import numpy as np

# MOST ADVANCED STATS API ENDPOINTS ARE NOT FUNCTIONAL ATM.

# Get game-by-game stats for every single player. 

bron = playergamelog.PlayerGameLog(player_id = '2544', season = '2018-19', season_type_all_star='Regular Season')
bron_df = bron.get_data_frames()[0]
bron_df['AVG_PTS'] = bron_df['PTS'].expanding().mean().shift(1)
bron_df['AVG_REB'] = bron_df['REB'].expanding().mean().shift(1)
bron_df['AVG_AST'] = bron_df['AST'].expanding().mean().shift(1)

# Replace with career avg down the line.
bron_df['AVG_PTS'] = bron_df['AVG_PTS'].fillna(bron_df['PTS'])
bron_df['AVG_REB'] = bron_df['AVG_REB'].fillna(bron_df['REB'])
bron_df['AVG_AST'] = bron_df['AVG_AST'].fillna(bron_df['AST'])
print(bron_df)

# Fetch team defensive stats for a season

#team_defense = leaguedashptteamdefend.LeagueDashPtTeamDefend(season='2022-23')
#team_defense_df = team_defense.get_data_frames()[0]
#print(team_defense_df)

# BOX SCORE DEFENSE NOT WORKING FOR NOW.
# box_defense = boxscoredefensive.BoxScoreDefensive(game_id = '0022201228')
# box_defense_df = box_defense.get_data_frames()[0]
# print(box_defense_df)

# Find a specific game.
# game = leaguegamefinder.LeagueGameFinder(player_or_team_abbreviation='P', team_id_nullable = '1612709932').get_data_frames()[0]
# print(game)

#stats = playercareerstats.PlayerCareerStats(per_mode36='PerGame', player_id='2544').get_data_frames()[0]
#print(stats)

#nba_guys = players.get_players()
#sorted_players = sorted(nba_guys, key=lambda player: player['id'])
#print(sorted_players)

#roto = gamerotation.GameRotation(game_id='0022201228').get_data_frames()[0]
#print(roto)