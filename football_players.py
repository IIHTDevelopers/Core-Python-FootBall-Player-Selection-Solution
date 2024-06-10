def count_players(file_path):
    with open(file_path, 'r') as file:
        player_count = 0
        for line in file:
            if line.startswith("Name:"):
                player_count += 1
    return player_count

# Test the function
file_path = "football_players.txt"
total_players = count_players(file_path)
print("Total number of players:", total_players)

def find_youngest_player(file_path):
    with open(file_path, 'r') as file:
        youngest_player = None
        youngest_age = float('inf')  # Initialize with a large number
        current_player = {}

        for line in file:
            line = line.strip()
            if line.startswith("Name:"):
                current_player['Name'] = line.split(": ")[1]
            elif line.startswith("Age:"):
                current_player['Age'] = int(line.split(": ")[1])
                if current_player['Age'] < youngest_age:
                    youngest_age = current_player['Age']
                    youngest_player = current_player.copy()
            elif line == "":  # Empty line indicates the end of a player's data
                current_player = {}

    return youngest_player

# Test the function
file_path = "football_players.txt"
youngest_player = find_youngest_player(file_path)
print("Youngest player:")
print(youngest_player)

def find_goals_by_messi(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Name: Lionel Messi"):
                for line in file:  # Continue reading lines for Messi's details
                    line = line.strip()
                    if line.startswith("Goals:"):
                        goals = int(line.split(": ")[1])
                        return goals

# Test the function
file_path = "football_players.txt"
messi_goals = find_goals_by_messi(file_path)
print("Goals scored by Lionel Messi:", messi_goals)

def find_country_of_ronaldo(file_path):
    with open(file_path, 'r') as file:
        ronaldo_details = {}
        for line in file:
            line = line.strip()
            if line.startswith("Name: Cristiano Ronaldo"):
                ronaldo_details['Name'] = "Cristiano Ronaldo"
                for line in file:
                    line = line.strip()
                    if line.startswith("Origin:"):
                        origin = line.split(": ")[1]
                        return origin

# Test the function
file_path = "football_players.txt"
ronaldo_country = find_country_of_ronaldo(file_path)
print("Cristiano Ronaldo's country:", ronaldo_country)

def count_zero_goal_players(file_path):
    zero_goal_count = 0
    with open(file_path, 'r') as file:
        current_player = {}

        for line in file:
            line = line.strip()
            if line.startswith("Name:"):
                current_player = {'Name': line.split(": ")[1]}
            elif line.startswith("Goals:"):
                goals = int(line.split(": ")[1])
                current_player['Goals'] = goals
                if goals == 0:
                    zero_goal_count += 1
            elif line == "":  # Empty line indicates the end of a player's data
                current_player = {}

    return zero_goal_count

# Test the function
file_path = "football_players.txt"
zero_goal_players = count_zero_goal_players(file_path)
print("Number of players who scored 0 goals:", zero_goal_players)
def find_brand_for_ramos(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Name: Sergio Ramos"):
                for line in file:  # Continue reading lines for Ramos's details
                    line = line.strip()
                    if line.startswith("Sponsor Brand:"):
                        brand = line.split(": ")[1]
                        return brand

# Test the function
file_path = "football_players.txt"
ramos_brand = find_brand_for_ramos(file_path)
print("Sergio Ramos's sponsor brand:", ramos_brand)

def find_player_type_for_modric(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Name: Luka Modric"):
                for line in file:  # Continue reading lines for Modric's details
                    line = line.strip()
                    if line.startswith("Player Type:"):
                        player_type = line.split(": ")[1]
                        return player_type

# Test the function
file_path = "football_players.txt"
modric_player_type = find_player_type_for_modric(file_path)
print("Luka Modric's player type:", modric_player_type)

def count_experienced_players(file_path):
    experienced_count = 0
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Experience:"):
                experience_years = int(line.split(": ")[1].split()[0])
                if experience_years > 10:
                    experienced_count += 1

    return experienced_count

# Test the function
file_path = "football_players.txt"
experienced_players = count_experienced_players(file_path)
print("Number of players with more than 10 years of experience:", experienced_players)
