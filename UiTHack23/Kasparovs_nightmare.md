# Kasparovs nightmare

## Challenge description

>Kasparov is sick and tired of overused cryptographic techniques and has decided to invent his own technique using a simple chess puzzle. A chess board is a 8x8 square represented by letters going from left to right and numbers up and down. Force the checkmate as white.
>
>Run python3 chess.py to start the challenge!
>
>Example: Moving any piece from d2 to d4  
From: 2d  
To: 4d

## Solution

Ok, where to start (I should probably try to get better at taking notes)...So we'll probably have to play some chess in this challenge, but let's first have a look at the code of chess.py. Near the bottom we have this line:

```python
flagg = [chr((ord(a) ^ ord(b))) for a, b in zip(encrypted_flag, moves)]
```

So, what happens here is that the zip() function placec every letter in the flag in a tuple together with the corresponding letter from the moves(you can try the zip function here: https://www.w3schools.com/python/trypython.asp?filename=demo_ref_zip2). Then for each tuple it's taken XOR between the numbers representing the two letters in the tuple. The result from the XOR is then converted back into the corresponding letter and put into the new list called flagg. This means that just forcing the checkmate as white is not enough, we have to use the correct sequence of moves. After trying to play a couple of times (or less, if you're quicker than me) we find out that we make the moves for both white an black.

So there's several ways to go on from here, we could for example try every possible combination of moves manually until we find the right one, but that would take way too long and wouldn't be any fun. We could also write a script to try every possible or, to make the script easier to write, also every impssible combination of moves for us, and decide which results contains valid strings. Yep, we could do that, but that's not the way I chose.

What I did do was that I made this short python script for testing:

```python
encrypted_flag = ['m', '\n', 'g', '+', 'T', '\x07', '^', 'W', '\x00', '\x18', '@', '\x10', 'Z',
                  '\x06', '_', '\x00', 'Z', '\x17', '[', ':', ']', '\x15', 'j', '\x13', 'A', '\x04', 'F', '\r', 'H']
encrypted_flag = "".join(encrypted_flag)

moves = "flag{example_flag"       #used for the flag
#moves =  "8c3c5d5e3c3d5e4f3"     #used for the moves
flagg = [chr((ord(a) ^ ord(b))) for a, b in zip(encrypted_flag, moves)]
print(flagg)
```
As you can see "moves" for the flag I'm testing and one for the moves I'm testing where I comment out the one that I don't want to test right now. Since we know the flag starts with "UiTHack23{" we start with inputting that as the "moves" which gives us the moves ```['8', 'c', '3', 'c', '5', 'd', '5', 'e', '3', 'c']```. As it happens, this game of chess did not start at the beginning and black only has the king left, so we know that each move for black has to start from the square where the last move ended, so the moves will be ```8c3c5d5e3c**5e``` which makes the flag ```UiTHack{**oc```.

To be continued (I need a break from writing)
