from src.pacman import Pacman

def main() -> None:
    pacman: Pacman = Pacman()
    try:
        pacman.run()
    except KeyboardInterrupt:
        pacman.stop()

if __name__ == "__main__":
    main()
