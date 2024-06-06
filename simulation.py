import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chess Simulation")

# Load images
def load_chess_piece_images():
    piece_names = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    piece_images = {}
    for name in piece_names:
        piece_images[name] = pygame.image.load(f"images/{name}.png")
    return piece_images

# Draw chessboard
def draw_chessboard(screen):
    light_green = pygame.Color(238,238,210)  # Light green
    dark_green = pygame.Color(105,146,62)    # Dark green
    colors = [light_green, dark_green]
    for row in range(8):
        for col in range(8):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, pygame.Rect(col * 100, row * 100, 100, 100))

# Draw chess pieces
def draw_chess_pieces(screen, chessboard, piece_images):
    for row in range(8):
        for col in range(8):
            piece = chessboard[row][col]
            if piece != "--":
                screen.blit(piece_images[piece], pygame.Rect(col * 100, row * 100, 100, 100))

# Convert mouse position to board coordinates
def get_board_position(mouse_pos):
    x, y = mouse_pos
    row = y // 100
    col = x // 100
    return row, col

# Main function
def main():
    piece_images = load_chess_piece_images()
    chessboard = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    ]

    current_turn = "white"
    selected_square = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and current_turn == "white":
                mouse_pos = pygame.mouse.get_pos()
                row, col = get_board_position(mouse_pos)
                if selected_square:
                    # Move the piece
                    target_row, target_col = row, col
                    chessboard[target_row][target_col] = chessboard[selected_square[0]][selected_square[1]]
                    chessboard[selected_square[0]][selected_square[1]] = "--"
                    selected_square = None
                    current_turn = "black"  # Switch turn to black after white moves
                else:
                    # Select the piece
                    selected_square = (row, col)

        draw_chessboard(screen)
        draw_chess_pieces(screen, chessboard, piece_images)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

