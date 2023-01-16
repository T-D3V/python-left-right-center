import typer

def main():
    playerList:list[str] = []
    def askPlayer(self, name: str = typer.Option(..., prompt=True)) -> None:
      playerList.append(name)
      def askPlayerAdd(self, choice: str = typer.Option("[Y/N]",prompt=True)):
        if choice == "Y":
          typer.run(askPlayer)
        else: print(playerList)
        typer.Exit
      typer.run(askPlayerAdd)
    typer.run(askPlayer)
    
    
  
if __name__ == "__main__":
  main()