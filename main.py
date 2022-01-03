import math
import pandas
import sys

class Player:
    def __init__(self, name, isPlaying, position, qa):
        self.name = name
        self.isPlaying = isPlaying
        self.position = position
        self.qa = qa

def chargeData():
    data = None
    try:
        data = pandas.read_csv('players.csv', sep="[,]", engine='python')
    except:
        sys.exit("No se encontró el archivo 'players.csv' en esta carpeta")
    try:
        names = data.nombre
        isPlaying = data.juega
        position = data.posicion
        qa = data.QA
        i = 0
        for name in names:
            # print(name)
            if name != name:
                continue
            isPlayingThis = isPlaying[i] == 1 or isPlaying[i] == "1" or isPlaying[i] == "si" or isPlaying[i] == "SI" or isPlaying[i] == "Si" or isPlaying[i] == "sí" or isPlaying[i] == "Sí" or isPlaying[i] == "SÍ"
            newPlayer = Player(name, isPlayingThis, position[i], qa[i])
            players.append(newPlayer)
            # print(newPlayer.name)
            # print(newPlayer.isPlaying)
            # print(newPlayer.position)
            # print(newPlayer.qa)
            # print('\n\n')
            i += 1
    except Exception as e:
        sys.exit("Alguna de las columnas está mal: " + str(e))

def requestTeamsNumber():
    while True:
        teamsSizeStr = input("Introducir cantidad (mínima) de jugadores por equipo (un número + enter): ")
        try:
            teamsSize = int(teamsSizeStr)
            break
        except:
            print("NO")
    print("Cantidad de jugadores por equipo: " + str(teamsSize))
    return teamsSize

def createTeams(teamsSize):
    teams = []
    attackers = []
    mediums = []
    defenders = []
    playersNumber = 0
    teamsNumber = 0
    for player in players:
        #print(player.isPlaying)
        if player.isPlaying == True:
            playersNumber += 1
            if player.position == "a":
                attackers.append(player)
            elif player.position == "m":
                mediums.append(player)
            else:
                defenders.append(player)
    print("Number of players: " + str(playersNumber))
    teamsNumber = math.floor(playersNumber / teamsSize)
    print("Number of teams: " + str(teamsNumber))
    
    def getMean(list):
        teamSum = 0
        for player in list:
            teamSum += player.qa
        mean = teamSum/len(list)
        return mean
    
    attackersMean = getMean(attackers)
    mediumsMean = getMean(mediums)
    defendersMean = getMean(defenders)
    
    print("Attackers mean: " + str(attackersMean))
    print("Mediums mean: " + str(mediumsMean))
    print("Defenders mean: " + str(defendersMean))
    
    for team in range(0, teamsNumber):
        team = [players[0], players[1], players[2], players[3], players[4], players[5]]
        teams.append(team)
        
    j = 1
    for team in teams:
        #print("\n\nTEAM " + str(j))
        j += 1
        for player in team:
            #print(player.name)
            z = 0
            
    for attacker in attackers:
        #print(attacker.name)
        z = 0
        

players = []
teamsSize = 0
chargeData()
while (teamsSize < 2):
    teamsSize = requestTeamsNumber()
createTeams(teamsSize)
