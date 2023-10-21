def compose(notes, moves, start):
    song = []
    current_position = start
    song.append(notes[current_position])
    for move in moves:
        current_position = (current_position + move) % len(notes) #pt a nu depasi lungimea listei
        song.append(notes[current_position])
    return song

def main():
    musical_notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    start_position = 2
    result = compose(musical_notes, moves, start_position)
    print(result)


if __name__ == "__main__":
    main()