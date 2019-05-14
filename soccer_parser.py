from collections import namedtuple
import sys

SOCCER_DATA_FILE = "soccer.dat"

TEAM_INDEX = 1
GOALS_FOR_INDEX = 6
GOALS_AGAINST_INDEX = 8

TeamGoalDifference = namedtuple("TeamScoreSpread", "team goal_difference")


def parse_line(line_parts):
    # skip anything under GOALS_AGAINST_INDEX
    if len(line_parts) <= GOALS_AGAINST_INDEX:
        return
    team = line_parts[TEAM_INDEX]
    goals_for = line_parts[GOALS_FOR_INDEX]
    goals_against = line_parts[GOALS_AGAINST_INDEX]

    if not goals_for.isdigit():
        return
    goals_for = int(goals_for)

    if not goals_against.isdigit():
        return
    goals_against = int(goals_against)

    return TeamGoalDifference(team=team, goal_difference=abs(goals_for - goals_against))


least_goal_difference = TeamGoalDifference(
    team="Nobody", goal_difference=sys.float_info.max
)

# lazily read w_data line by line
with open(SOCCER_DATA_FILE) as f:
    for line in f:
        team_score_diff = parse_line(line.split())
        if not team_score_diff:
            continue
        if team_score_diff.goal_difference < least_goal_difference.goal_difference:
            least_goal_difference = team_score_diff
print(least_goal_difference)


# # functional approach, not lazy, loads entire file into memory
# f = open('soccer.dat')
# result = min(filter(lambda x: x != None, map(parse_line, map(lambda l: l.split(), f.readlines()))), key=lambda x: x.goal_difference)
# print(result)
