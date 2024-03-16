Update 1) 3/16/24
Because of the emoji problem, I have added colors to make it easier to see the Xs and Os.
Added formatting to the history, and cleaned up the code


The EXE file was made with auto-py-to-exe

My first project, basic console-only tic tac toe game
includes: vs. computer mode
          vs. friend mode
          previous game history 
          customizable game board size

The X and O symbols used to emojis but unfortunately that can't be displayed in CMD so that explains the weird symbols

Let me explain every part of the script

First import all the resources I kind of need, OS for clearing out the terminal, random for obvious reasons, and colorama.

I needed to use colorama because my original version used large x&o emojis but that doesn't show up on cmd, so I needed to figure out a way where the X's and O's see incredibly easy to see for the viewer



The errorcheck_input() function is just something quick I made up to cross my t's and dot my i's, just ensure nothing ends the script prematurely




Then onto the main function;

I had to global basically all my main starting variables because the original version of this script was not within a main function cuz I was being an idiot, and I won't rewrite this whole thing to fix that.

The gameSelection() function is pretty obvious, it has input correction as well

The required asset part are just variables that I absolutely need to make the entire thing work in the first place

The symbols are defined, the wind conditions are defined, and then resources based off the game size are generated after that

The before10 variable is needed to because of the nature of how I generate the array that the game is built inside of




The graphics () function is to generate an array based off the game size chosen by the player, it works by first initializing a list within a list, and a variable called counts with zero.
Then it goes through the number variable initialize before the function is called, number is basically the game size times itself to give the actual number of cells needed. If the specific number called "num" in the list called numbers is divisible by the game size then that means it's the end of that specific row, which needs to move to next row. If num is less than nine than it needs to append zero string to the number while making the row. This is needed because there needs to be at least two digits in order to achieve a square size. If not then the graphics get ugly.



I then call that function in a variable called grid





The next function is called drawGrid(); This one is fun. Inside this function I make another function called colored cell, this takes a element from grid and checks if it's x or o and then gives it a color and symbol, If not it just takes that element and adds spaces to format it correctly.

Next goes to the loop which actually draws the game. In order to fix the formatting issues I was having, I made a function called first row and for cell, first row is outside the actual loop, first cell is made when each row is being iterated. Loop runs and it basically draws The first line which is only if firstRow is true. Then starts a loop within that first row after that, That loop goes to each cell, draws the cell with the coloredCell function called, then after that's done it draws a line, after the last element is iterated, finally it draws the last line.




The next function is called userpick(), it takes the arguments playerSymbol, playerType, and computerCell. 

I know I keep using the global variables thing but I'm sorry, I just kind of need to do this to make it work. The first checks what type of player is using the function with the playerType argument, it could either be a player or the computer. If it's the computer the user cell is automatically the computer cell. If it's a player then it asks for an input which type of cell The player wants to pick. It then changes that input with some error correcting into an integer, and saves it in a variable called userCell. It also checks if the cell is even available to pick in the first place. I did this which I think in a clever way where if the cell is picked then it removes that specific cell number from the numbers list. 

I then add one to the turns variable, and I computes the actual coordinate of that cell. I realized if I take the userCell, divided by the size variable, The remainder will be the actual x value on the row. Doing this operation again but instead of the remainder the actual divided value gives the y value on grid. Then the x and y values are plugged in into the grid index and that specific cell is equal to the playerSymbol argument. The function then returns the userCell. This is needed for the computer.





The next function is called winCheck(), This is used to dynamically check who won. Because the nature of this game and how there could be any number of game sizes, I couldn't hardcode this in any way, just a lot of loops.
The code is honestly really bad in this one, it was kind of tough to deal with. I don't have the energy to make it more efficient or fix it anymore

Again sorry about the global variables, the required variables for this one are empty list for each way you could win the game.


In order to be more efficient and not waste resources, this function is only activated when the turns value is a specific amount, that amount is two times the number of the game board, This is because there's no possible way to win without making That specific number of moves/turns. For example if you have a 3x3 board, in order to win you must have 3 turns. When two players are involved 6. 

If the turns value reach that specific number, then I continue with the function, I then convert every element in the numbers list into a string version of itself and then added into another list called str_numbers. 
Then goes on to check the top left bottom right diagonal and the top right to bottom left diagonal, the first checks if the very first element in that diagonal is either an x or o, and then it checks the last element. If both are true then it starts going in a stair step direction down. It starts appending that cell to the either one of the two diagonal lists If at any point, It encounters a cell in the grid that is not either an x or o, it breaks the loop.

And then checks if there is a specific amount of elements in the diagonals lists, which is just the number of the game size (I already explained that before) and then it checks if there is an odd one out in the list.

For example, If the program knows that there are three elements in the diagonal list, and that the only possible way those elements could have been appended inside the list was if it's an either an X or O, by checking there is no Xs in the list then by reasoning 0 won. I hope that made sense and I'm just not rambling.

The horizontal check uses basically the same logic but instead of using a loop it just uses .count() method. 

The vertical one is a little different. At first starts at the first element in the first row, It then starts another loop with the range function starting from 0 to the size of the game board. Then a variable called vertical next check is equal to that specific cell in the grid. With the nested loop value Y variable as it's y, and The index of that starting cell in the outside loop as the x value. And then check is If the cell is an x or an o, appends it if so, and then counts the number of elements in the list called vertical, basically the same logic and reasoning as the diagonal checking algorithm.

If any win conditions are activated then it tells what type of win was achieved with the winType as a string, and sets either x_win_game or O_win_game as true.











The next function is called computer(), which takes the return value from user pick and calls it player as an argument. 
This function is basically the algorithm which lets the computer pick a move, this algorithm isn't amazing, and on a normal 3x3 board honestly half the time it's a stupid as hell, often losing. But as the board sizes increase it gets more effective. It works mostly by trying to stop the player rather than winning anything. I could probably rewrite this function to make it win but honestly I don't care now and I'm done with this project.


I've made four functions to check each possible line type that the player is on, basically meaning the possible ways a player can win on that specific cell that they picked. The code is honestly really similar to the winCheck() and I could have probably made it a lot more efficient by incorporating it together but like I said I don't care anymore. 

(X's are important because they're going to be what the player is if it's player versus computer. The player will always be x, the computer will always be o. This made it a bit easier for me)

It basically works like this, it counts the number of x's on the cell that it's iterating on either diagonally horizontally or vertically, and then adds one if it counts as an x. If it ends up encountering a O, then it sets count variable to an absurdly low number as it's impossible for the player to win and the computer can focus on winning itself. If it does not encounter an x or an o, then it appends the cell number as it's an available place to move inside a list with a name respective to the actual line type
Then it ends up returning the count variable, the possible cells on that line inside a list, and then the type of line it is as a string (needed this for debugging)

It then puts all the different checks, diagonal vertical horizontal inside one list called fullCheck, basically giving the computer full "vision" on the board. 

Full check is then sorted by the count number, and then reversed to put the highest account number first.

I then implemented away for the function to be a little bit more efficient, basically deleting any lines if there's no available cells to pick for the computer. This doesn't work amazingly and I have to use this loop twice for it to be effective but It is what it is. 

I then made a function called computerPick(), basically a way for the computer to actually pick a cell calling the userPick() function but modified. It works by again deleting any non-available lines, then checking if there's any remaining lines left in the full check list, if not that means basically the board is filling up and it needs to pick something randomly, if there are remaining lines available then it first finds to the critical number
 
The critical number is basically a flag I made to notify the computer that it needs to impede the player. The critical number is basically just the game size divided by two, it basically means the player has made enough moves where any more moves and it's a certain win.

If there are any lines available in the list fullCheck, The computerPick() function then extract the count value from the very first line of the fullCheck list, compares it to the critical number, and if the count value is at or greater than the critical value then it picks the first value from the list of available cells from that line, and then calls the userPick() function, with that specific cell number as an argument. 

Continuing in the computer() function, after defining computerPick(), and then checks if the game board is odd, I did this because odd size boards have a center cell, that's center cell is usually a great starting point to toe or win the game, If the game board is odd then it checks if the center cell is still available to pick, and then the computer () function calls userPick with the center cell as the argument. If not then the computerPick() function is called, usually in every turn the computerPick() function is called when the computer is making a move

Finally it returns the player value and full checklist for debugging.






The final function is called endGame(), This function is basically the end of the game, it clears out anything from the terminal first, draws the game board with drawGrid() function, and then checks either if x or o won and then displays the representative win text. And then adds that text to the gameHistory list first defined in the beginning of the program



The game loop is basically just first checking if there's any cells remaining, then checking if anybody won the game then proceeding to let the x player to make a move and then draws the grid, and then checks if there's any remaining cells again (If not ends the loop) then it precedes for the o player to make a move and then draws a grid again but cleared everything first. It does this until either x or o wine 

