"""
==============================================
 DISCLAIMER
 I do not take the full responsibility for 
 all the written codes in this python file
 i have used resources like Stackoverflow 
 and Github to complete this exercise

==============================================

"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from django.http import HttpRequest
from django.http import JsonResponse
import json
import random


def game(request):
   return render(request,'game.html',{})

def tic(request):
   # Getting the board from post
   if request.method == 'POST':
      body_unicode = request.body.decode('utf-8')
      # loading  as json
      body = json.loads(body_unicode)
      # querying from the json
      input_str = body['value']
      # converting into integers
      input = int(input_str)
      #  extracting again
      board = body['x']

      if board[input] != 'x' and board[input] != 'o':
         board[input] = 'x'
      else:
         return JsonResponse({'taken': 'place already taken'})

      if check_match(board,'x') == True:
         winner = 'x'
         return JsonResponse({'input': input, 'board': board, 'winner': winner})


      if check_match(board,'o') == True:
         print('o wins')
         winner = 'o'
         return JsonResponse({'input': input, 'board': board, 'winner': winner})
      board = opponent_fun(board)

      winner = 0
      return JsonResponse({'input': input, 'board': board, 'winner': winner})

def opponent_fun(board):
      while True:

         random.seed()
         opponent = random.randint(0, 8)

         if board[opponent] != 'o' and board[opponent] != 'x':
          board[opponent] = 'o'
          return board

def check(board, char, cell1, cell2, cell3):
    if board[cell1]  == char and board[cell2] == char and board[cell3] == char:
        return True
    else:
       return False

def check_match(board,char):
    if check(board,char, 0,1,2):
        return True
    if check(board,char, 3,4,5):
        return True
    if check(board,char, 6,7,8):
        return True
    if check(board,char, 2,4,6):
        return True
    if check(board,char, 0,4,8):
        return True
    if check(board,char, 1,4,7):
        return True
    if check(board,char, 2,5,8):
        return True
    if check(board,char, 6,7,8):
        return True
