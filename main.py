# main.py
# COMP282 - Project: Music Playlist Manager
import shlex
import sys

class Node:
    __slots__ = ("title", "artist", "duration", "next", "prev")
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = self
        self.prev = self

class Playlist:
    def __init__(self):
        self.head = None
        self.cursor = None
        self.size = 0

    def add_after_cursor(self, title, artist, duration):
        new_node = Node(title, artist, duration)
        if self.head is None:
            self.head = new_node
            self.cursor = new_node
        else:
            new_node.prev = self.cursor
            new_node.next = self.cursor.next
            self.cursor.next.prev = new_node
            self.cursor.next = new_node
            self.cursor = new_node
        self.size += 1

    def remove_at_cursor(self):
        if self.head is None:
            return
        if self.size == 1:
            self.head = None
            self.cursor = None
        else:
            self.cursor.prev.next = self.cursor.next
            self.cursor.next.prev = self.cursor.prev
            if self.cursor == self.head:
                self.head = self.cursor.next
            self.cursor = self.cursor.next
        self.size -= 1

    def next_song(self):
        if self.cursor:
            self.cursor = self.cursor.next

    def prev_song(self):
        if self.cursor:
            self.cursor = self.cursor.prev

    def current_song(self):
        if self.cursor:
            return (self.cursor.title, self.cursor.artist, self.cursor.duration)
        return None

    def length(self):
        return self.size

    def clear(self):
        self.head = None
        self.cursor = None
        self.size = 0

    def display_all(self):
        if self.head is None:
            print("EMPTY")
            return
        current = self.head
        for _ in range(self.size):
            marker = "-> " if current == self.cursor else "   "
            print(f"{marker}{current.title} | {current.artist} | {current.duration}(s)")
            current = current.next


def main():
    pl = Playlist()

    for raw in sys.stdin:
        line = raw.strip()
        if not line:
            continue

        try:
            parts = shlex.split(line)
        except ValueError:
            continue

        if not parts:
            continue

        cmd = parts[0].upper()

        if cmd == "ADD":
            if len(parts) < 4:
                continue
            title = parts[1]
            artist = parts[2]
            try:
                duration = int(parts[3])
            except ValueError:
                continue
            pl.add_after_cursor(title, artist, duration)

        elif cmd == "REMOVE":
            pl.remove_at_cursor()

        elif cmd == "NEXT":
            if pl.cursor is None:
                print("EMPTY")
            else:
                pl.next_song()

        elif cmd == "PREV":
            if pl.cursor is None:
                print("EMPTY")
            else:
                pl.prev_song()

        elif cmd == "CURRENT":
            cur = pl.current_song()
            if cur is None:
                print("EMPTY")
            else:
                title, artist, duration = cur
                print(f"-> {title} | {artist} | {duration}(s)")

        elif cmd == "PRINT":
            pl.display_all()

        elif cmd == "LEN":
            print(pl.length())

        elif cmd == "CLEAR":
            pl.clear()

        elif cmd == "QUIT":
            sys.exit(0)


if __name__ == "__main__":
    main()

