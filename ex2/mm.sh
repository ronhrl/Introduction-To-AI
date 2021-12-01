python3 pacman.py -p MinimaxAgent -l minimaxClassic -f -a depth=4 -q | grep "Scores" 
python3 pacman.py -p MinimaxAgent -l minimaxClassic -f -a depth=3 -q | grep "Scores" 
python3 pacman.py -p MinimaxAgent -l minimaxClassic -f -a depth=2 -q | grep "Scores" 
python3 pacman.py -p MinimaxAgent -l minimaxClassic -f -a depth=1 -q | grep "Scores" 

python3 pacman.py -p MinimaxAgent -l mediumClassic -f -a depth=2 -q | grep "Scores" 
python3 pacman.py -p MinimaxAgent -l mediumClassic -f -a depth=1 -q | grep "Scores" 

python3 pacman.py -p MinimaxAgent -l trappedClassic -f -a depth=4 -q | grep "Scores" 
python3 pacman.py -p MinimaxAgent -l trappedClassic -f -a depth=3 -q | grep "Scores" 
python3 pacman.py -p MinimaxAgent -l trappedClassic -f -a depth=2 -q | grep "Scores" 
python3 pacman.py -p MinimaxAgent -l trappedClassic -f -a depth=1 -q | grep "Scores" 

python3 pacman.py -p MinimaxAgent -l smallClassic -f -a depth=2 -q | grep "Scores" 
python3 pacman.py -p MinimaxAgent -l smallClassic -f -a depth=1 -q | grep "Scores" 
