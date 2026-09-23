def checkmate(board_str):
    if not board_str:
        return

    board = [list(row) for row in board_str.strip().split('\n') if row]
    rows = len(board)
    if rows == 0:
        return
    cols = len(board[0])

    king_pos = None
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break

    if not king_pos:
        print("Fail")
        return

    kr, kc = king_pos

    def is_threat_in_direction(dr, dc, valid_pieces):
        r, c = kr + dr, kc + dc
        while 0 <= r < rows and 0 <= c < cols:
            piece = board[r][c]
            if piece != '.':
                if piece in valid_pieces:
                    return True
                else:
                    return False
            r += dr
            c += dc
        return False

    pawn_threats = [(kr - 1, kc - 1), (kr - 1, kc + 1), (kr + 1, kc - 1), (kr + 1, kc + 1)]
    for pr, pc in pawn_threats:
        if 0 <= pr < rows and 0 <= pc < cols:
            if board[pr][pc] == 'P':
                print("Success")
                return

    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in straight_directions:
        if is_threat_in_direction(dr, dc, ['R', 'Q']):
            print("Success")
            return

    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in diagonal_directions:
        if is_threat_in_direction(dr, dc, ['B', 'Q']):
            print("Success")
            return

    print("Fail")