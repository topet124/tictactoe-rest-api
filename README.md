SSH CODING ASSIGNMENT
------------

Tic Tac Toe
------------

The aim of the coding assignment is to implement a REST backend for a game of tic-tac-toe.

Features
------------

- The player starts a game by making a POST request to /games.
  The POST request contains a representation of a game board, either empty
  (computer starts) or with the first move made (player starts).
  The player/computer can choose either noughts or crosses.

- The backend responds with the location URL of the started game.

- Client GETs the board state from the URL.

- Client PUTs the board state with a new move to the URL.

- Backend validates the move, makes it's own move and updates the game state.
  The updated game state is returned in the PUT response.

- The game is over once the computer or the player gets 3 noughts
  or crosses, horizontally, vertically or diagonally or there are no moves to
  be made.

Tech
------------

* [KnockoutJS] - standalone JavaScript implementation of the Model-View-ViewModel pattern!
* [Django] - Python Web framework
* [Python] - programming language
* [jQuery] - JavaScript library

Installation
------------
* Download and install python (https://www.python.org/ftp/python/3.9.0/python-3.9.0-macosx10.9.pkg)
  
* Download the Pip (Python package installer) bootstrap script
  [get-pip.py](https://bootstrap.pypa.io/get-pip.py).

  * install `virtualenv`.
   using (pip install virtualenv) in your command prompt


### Installation in Ubuntu

Python 3 is preinstalled in Ubuntu. Virtualenv and pip necessarily aren't, so:

* `sudo apt-get install python-virtualenv python-pip`

### Creating and activating a virtualenv

Go to the project root directory and run:

Windows:

```
c:\location_of_project>venv\Scripts\activate
```

Ubuntu:

```
source venv/bin/activate
```

MAC
´´´´´
source bin/activate
´´´´´´

-------------------------
starting the project
-------------------------

```sh
$ cd src/tictactoe/
$ pip3 install -r requirements.txt  (for mac and linux)
$ pip install requirements.txt      (windows)
```

### Running the application

```sh
$ cd src/tictactoe/
$ python manage.py runserver
$ Open browser http://127.0.0.1:8000/game
```




