@python pacman.py -p MinimaxAgent -l minimaxClassic -f -a depth=4 -q  | find   "Scores" 
@python pacman.py -p MinimaxAgent -l minimaxClassic -f -a depth=3 -q | find   "Scores" 
@python pacman.py -p MinimaxAgent -l minimaxClassic -f -a depth=2 -q | find   "Scores" 
@python pacman.py -p MinimaxAgent -l minimaxClassic -f -a depth=1 -q | find   "Scores" 

@python pacman.py -p MinimaxAgent -l mediumClassic -f -a depth=2 -q | find   "Scores" 
@python pacman.py -p MinimaxAgent -l mediumClassic -f -a depth=1 -q | find   "Scores" 

@python pacman.py -p MinimaxAgent -l trappedClassic -f -a depth=4 -q | find   "Scores" 
@python pacman.py -p MinimaxAgent -l trappedClassic -f -a depth=3 -q | find   "Scores"
@python pacman.py -p MinimaxAgent -l trappedClassic -f -a depth=2 -q | find   "Scores"
@python pacman.py -p MinimaxAgent -l trappedClassic -f -a depth=1 -q | find   "Scores"

@python pacman.py -p MinimaxAgent -l smallClassic -f -a depth=2 -q | find   "Scores" 
@python pacman.py -p MinimaxAgent -l smallClassic -f -a depth=1 -q | find   "Scores" 