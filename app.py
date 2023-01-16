import random
import typer

class Dice:
  MAX_NUMBER:int = 6
  __random:int = random.randint(1, MAX_NUMBER)
  __lastNumber:int
  
  @property
  def lastNumber(self) -> int:
    return self.__lastNumber
  
  def rollTheDice(self) -> None:
    self.__lastNumber = self.__random
    
class Cup:
  COUNT_DICE:int
  __dice:list[Dice]
  
  def __init__(self) -> None:
    pass
  
  def shake(self) -> None:
    for dice in self.__dice:
      dice.rollTheDice()
  
  def getNumbers(self, amount:int) -> list[int]:
    numbers:list[int] = []
    
    for index, dice in enumerate(self.__dice):
      if(index <= amount):
        numbers.append(self.__dice[index].lastNumber)
        
    return numbers
      
  
class Player:
  __chips:int
  __name:str
  def __init__(self, name:str) -> None:
    self.__name:str = name
  
  @property
  def name(self) -> str:
    return self.__name
  
  @property
  def stillHasChips(self) -> bool:
    return True if self.__chips > 0 else False
  
  @property
  def amountOfDice(self) -> int:
    return 1
  
  def recieveChip(self) -> None:
    self.__chips += 1
  
  def passChip(self) -> None:
    self.__chips -= 1
  
  #unclear
  def playTurn(self, cup:Cup) -> list[int]:
    return []
  
  def printNameAndChips(self) -> str:
    return self.name + str(self.__chips)
  
  #unclear
  def printDice(self) -> str:
    return ""
  
class Gui(): 
  
  def askPlayerInput(self) -> list[Player]:
    playerList:list[Player] = []
    def askPlayer(self, name: str = typer.Option(..., prompt=True)) -> None:
      playerList.append(Player(name))
      def askPlayerAdd(self, choice: str = typer.Option("[Y/N]",prompt=True)):
        if choice == "Y":
          typer.run(askPlayer)
        else: typer.Exit
      typer.run(askPlayerAdd)
    typer.run(askPlayer)
    return playerList

    
      
  
  def askAnotherGame(self) -> bool:
    return True
  
  def printRanks(self, players: list[Player]) -> None:
    pass
  
  def printWinner(self, players:list[Player]) -> None:
    pass
  
class Game:
  __currentPlayer:Player
  __playerList:list[Player]
  __gui:Gui
  __cup:Cup
  
  def __init__(self) -> None:
    pass
  
  def play(self) -> None:
    pass
  
  def processRolledNumbers(self, numbers:list[int]) -> None:
    pass
  
  def setStartPlayer(self) -> None:
    self.__currentPlayer = random.choice(self.__playerList)
  
  def playerRightOfCurrentPlayer(self) -> Player:
    return self.__playerList[self.__playerList.index(self.__currentPlayer) + 1]
  
  def playerLeftOfCurrentPlayer(self) -> Player:
    return self.__playerList[self.__playerList.index(self.__currentPlayer) - 1]

  
  def moreThanOnePlayerHasChips(self) -> bool:
    counter = 0
    for player in self.__playerList:
      if(player.__chips > 0):
        counter += 1
    return True if counter >= 2 else False
  
  def giveChipToLeft(self) -> None:
    pass
  
  def giveChipToRight(self) -> None:
    pass
  
  def putChipInMiddle(self) -> None:
    pass
  
    