import random
import typer

class Dice:
  MAX_NUMBER:int = 6
  __lastNumber:int = 0
  
  @property
  def __random(self) -> int:
    return random.randint(1, self.MAX_NUMBER)
  
  @property
  def LastNumber(self) -> int:
    return self.__lastNumber
  
  def RollTheDice(self) -> None:
    self.__lastNumber = self.__random

class Cup:
  AMT_DICE:int = 3
  __dice:list[Dice] = []
  
  def __init__(self) -> None:
    i = 0
    for i in range(0, self.AMT_DICE):
      self.__dice.append(Dice())
      i += 1
  
  def Shake(self) -> None:
    for dice in self.__dice:
      dice.RollTheDice()
  
  def GetNumbers(self, amt:int) -> list[int]:
    nums:list[int] = []
    for dice in self.__dice:
      nums.append(dice.LastNumber)
      
    return nums[:amt]

class Player:
  __chips:int = 3
  __name:str
  
  @property
  def Name(self) -> str:
    return self.__name

  @property
  def StillHasChips(self) -> bool:
    return True if self.__chips > 0 else False
  
  @property
  def AmountOfDice(self) -> int:
    return self.__chips if self.__chips < 3 else 3
  
  def __init__(self, name:str) -> None:
    self.__name = name
    
  def RecieveChip(self) -> None:
    self.__chips += 1

  def PassChip(self) -> None:
    self.__chips -= 1
  
  def PlayTurn(self, cup:Cup) -> list[int]:
    cup.Shake()
    numbers = cup.GetNumbers(self.AmountOfDice)
    print(self.PrintDice(numbers))
    return numbers

  def PrintNameAndChips(self) -> str:
    return self.__name + " has " + str(self.__chips) + " chips."
  
  def PrintDice(self, rolls:list[int]) -> str:
    return "Player " + self.__name + " has rolled: " + ", ".join(map(str, rolls))

class GUI:
  def AskPlayerInput(self) -> list[Player]:
    playerList:list[Player] = []

    while True:
      playerList.append(Player(typer.prompt("Name")))
      if not self.AskAnotherPlayer():
        break
    
    return playerList
  
  def AskAnotherPlayer(self) -> bool:
    choice = typer.prompt("Add another Player [Y/N]")
    return True if choice == "Y" else False
  
  def PrintRanks(self, players:list[Player]) -> None:
    print("###Points:###")
    for player in players:
      print(f"{player.PrintNameAndChips()}")
    print("### End of Round ##\n")
  
  def PrintWinner(self, players:list[Player]) -> None:
    print("###End result:###")
    for player in players:
      if player.StillHasChips:
        print(f"Player {player.Name} has won.")

class Game:
  __currentPlayer:Player
  __playerList:list[Player] = []
  __gui:GUI = GUI()
  __cup:Cup = Cup()
  
  def __init__(self) -> None:
    self.__playerList = self.__gui.AskPlayerInput()
  
  def Play(self) -> None:
    self.SetStartingPlayer()
    while self.MoreThanOnePlayerHasChips():
      if self.__currentPlayer.StillHasChips:
        rolledNumbers = self.__currentPlayer.PlayTurn(self.__cup)
        self.ProcessRolledNumbers(rolledNumbers)
        self.__currentPlayer = self.PlayerRightOfCurrentPlayer()
        self.__gui.PrintRanks(self.__playerList)
      else:
        self.__currentPlayer = self.PlayerRightOfCurrentPlayer()
    
    self.__gui.PrintWinner(self.__playerList)
  
  def ProcessRolledNumbers(self, nums:list[int]) -> None:
    for num in nums:
      if num == 4:
        self.PassChipLeft()
      elif num == 5:
        self.PassChipRight()
      elif num == 6:
        self.PutChipInMiddle()
  
  def SetStartingPlayer(self) -> None:
    self.__currentPlayer = self.__playerList[random.randint(0, len(self.__playerList) - 1)]
  
  def PlayerRightOfCurrentPlayer(self) -> Player:
    currentPos = self.__playerList.index(self.__currentPlayer)
    nextPos = currentPos + 1 if currentPos < len(self.__playerList)-1 else 0
    
    return self.__playerList[nextPos]
    
  
  def PlayerLeftOfCurrentPlayer(self) -> Player:
    currentPos = self.__playerList.index(self.__currentPlayer)
    nextPos = currentPos - 1 if currentPos > 0 else -1
    
    return self.__playerList[nextPos]
  
  def MoreThanOnePlayerHasChips(self) -> bool:
    playersWithChips = 0
    for player in self.__playerList:
      if player.StillHasChips:
        playersWithChips += 1
    return True if playersWithChips >= 2 else False
  
  def PassChipLeft(self) -> None:
    self.__currentPlayer.PassChip()
    self.PlayerLeftOfCurrentPlayer().RecieveChip()
  
  def PassChipRight(self) -> None:
    self.__currentPlayer.PassChip()
    self.PlayerRightOfCurrentPlayer().RecieveChip()
  
  def PutChipInMiddle(self) -> None:
    self.__currentPlayer.PassChip()

if __name__ == "__main__":
  typer.run(Game().Play)
  typer.Exit