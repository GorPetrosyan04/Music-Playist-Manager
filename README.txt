COMP 282 – Project: Music Playlist Manager
Author: Gor Petrosyan
Date: October 4, 2025


Node and Link Design:
---------------------
Each song is represented by a Node object containing:
- title (string)
- artist (string)
- duration (int, in seconds)
- next (reference to the next Node)
- prev (reference to the previous Node)


Nodes are connected in a circular doubly linked list, meaning:
- The last node’s next pointer references the head.
- The head’s prev pointer references the last node.
- The playlist always maintains valid next/prev links between all nodes.
- The cursor points to the "current" node at all times (or None if empty).


Invariant: When size > 0, cursor is never None and all nodes form one closed circular chain.


How to Run:


> python main.py
(Type commands manually)
OR
> python main.py < commands.txt


Commands Implemented:


ADD "title" artist duration  - Adds a new song after the cursor and moves cursor to it.
REMOVE                       - Deletes the current song, cursor moves to the next song.
NEXT                         - Moves the cursor to the next song (wraps around).
PREV                         - Moves the cursor to the previous song (wraps around).
CURRENT                      - Displays the song currently at the cursor.
PRINT                        - Prints all songs in the playlist (with -> marking the cursor).
LEN                          - Prints the total number of songs in the playlist.
CLEAR                        - Removes all songs, making the playlist empty.
QUIT                         - Exits the program.


Data Structure Summary:


Implemented using a circular doubly linked list for O(1) navigation and updates.