import pygame
import sys

# Inisialisasi pygame
pygame.init()

# Definisikan konstanta
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Warna
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)
TEXT_COLOR = (255, 255, 255)

# Inisialisasi layar
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Papan permainan
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def draw_lines():
    # Garis horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Garis vertikal
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                                 CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                                 (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    # Periksa kemenangan horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True

    # Periksa kemenangan vertikal
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Periksa kemenangan diagonal
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


def draw_winner_line(player):
    if player == 1:
        color = CIRCLE_COLOR
    else:
        color = CROSS_COLOR
    
    if board[0][0] == board[1][1] == board[2][2] == player:
        pygame.draw.line(screen, color, (0, 0), (WIDTH, HEIGHT), LINE_WIDTH)
    elif board[0][2] == board[1][1] == board[2][0] == player:
        pygame.draw.line(screen, color, (0, HEIGHT), (WIDTH, 0), LINE_WIDTH)
    elif board[0][0] == board[0][1] == board[0][2] == player:
        pygame.draw.line(screen, color, (SQUARE_SIZE // 2, 0), (SQUARE_SIZE // 2, HEIGHT), LINE_WIDTH)
    elif board[1][0] == board[1][1] == board[1][2] == player:
        pygame.draw.line(screen, color, (SQUARE_SIZE + SQUARE_SIZE // 2, 0), (SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT), LINE_WIDTH)
    elif board[2][0] == board[2][1] == board[2][2] == player:
        pygame.draw.line(screen, color, (2 * SQUARE_SIZE + SQUARE_SIZE // 2, 0), (2 * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT), LINE_WIDTH)
    elif board[0][0] == board[1][0] == board[2][0] == player:
        pygame.draw.line(screen, color, (0, SQUARE_SIZE // 2), (WIDTH, SQUARE_SIZE // 2), LINE_WIDTH)
    elif board[0][1] == board[1][1] == board[2][1] == player:
        pygame.draw.line(screen, color, (0, SQUARE_SIZE + SQUARE_SIZE // 2), (WIDTH, SQUARE_SIZE + SQUARE_SIZE // 2), LINE_WIDTH)
    elif board[0][2] == board[1][2] == board[2][2] == player:
        pygame.draw.line(screen, color, (0, 2 * SQUARE_SIZE + SQUARE_SIZE // 2), (WIDTH, 2 * SQUARE_SIZE + SQUARE_SIZE // 2), LINE_WIDTH)


def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0


draw_lines()

# Variabel utama
player = 1
game_over = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # X
            mouseY = event.pos[1]  # Y

            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True

                draw_figures()
                player = 1 if player == 2 else 2

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    if game_over:
        if check_win(player):
            if player == 1:
                winner_text = "Player X Menang!"
            else:
                winner_text = "Player O Menang!"

            font = pygame.font.Font(None, 36)  # Tentukan font dan ukuran teks
            text = font.render(winner_text, True, TEXT_COLOR)  # Buat teks yang akan ditampilkan
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))  # Tentukan posisi teks
            screen.blit(text, text_rect)  # Tampilkan teks di layar
        else:
            draw_winner_line(player)

    pygame.display.update()
