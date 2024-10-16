from tkinter import Canvas, Button, Frame
import chess
import chess.pgn
from PIL import Image, ImageTk
import io


class ChessGUI:
    BOARD_SIZE = 600
    SQUARE_SIZE = BOARD_SIZE // 8
    WHITE = "#F0D9B5"
    BLACK = "#B58863"

    def __init__(self, root, moves):
        self.root = root
        self.root.title("Replayer de Partie d'Échecs")
        self.canvas = Canvas(root, width=ChessGUI.BOARD_SIZE, height=ChessGUI.BOARD_SIZE)
        self.canvas.pack()

        self.board = chess.Board()
        self.moves = moves
        self.current_move = -1

        # Charger les images des pièces
        self.piece_images = self.load_piece_images()

        # Ajouter les boutons
        button_frame = Frame(root)
        button_frame.pack()

        prev_button = Button(button_frame, text="<< Précédent", command=self.prev_move)
        prev_button.grid(row=0, column=0)

        next_button = Button(button_frame, text="Suivant >>", command=self.next_move)
        next_button.grid(row=0, column=1)

        self.draw_board()
        self.load_pgn()

    def load_piece_images(self):
        pieces = {}
        piece_names = {
            'P': 'white_pawn.png', 'N': 'white_knight.png', 'B': 'white_bishop.png',
            'R': 'white_rook.png', 'Q': 'white_queen.png', 'K': 'white_king.png',
            'p': 'black_pawn.png', 'n': 'black_knight.png', 'b': 'black_bishop.png',
            'r': 'black_rook.png', 'q': 'black_queen.png', 'k': 'black_king.png'
        }

        for piece, filename in piece_names.items():
            image = Image.open(f"Interfaces/chess_pieces/{filename}")
            image = image.resize((ChessGUI.SQUARE_SIZE, ChessGUI.SQUARE_SIZE))
            pieces[piece] = ImageTk.PhotoImage(image)

        return pieces

    def draw_board(self):  # Fait par ChatGPT
        self.canvas.delete("all")
        colors = [ChessGUI.WHITE, ChessGUI.BLACK]
        for row in range(8):
            for col in range(8):
                color = colors[(row + col) % 2]
                x1 = col * ChessGUI.SQUARE_SIZE
                y1 = row * ChessGUI.SQUARE_SIZE
                x2 = x1 + ChessGUI.SQUARE_SIZE
                y2 = y1 + ChessGUI.SQUARE_SIZE
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                x = chess.square_file(square) * ChessGUI.SQUARE_SIZE
                y = (7 - chess.square_rank(square)) * ChessGUI.SQUARE_SIZE
                piece_image = self.piece_images[piece.symbol()]
                self.canvas.create_image(x, y, anchor='nw', image=piece_image)

    def load_pgn(self):
        # Create a PGN stream from the moves
        pgn_stream = io.StringIO(self.moves)

        # Read the game using python-chess's PGN parser
        game = chess.pgn.read_game(pgn_stream)

        # Start with an empty board
        self.board = chess.Board()

        # Collect all moves from the game and reset the move counter
        self.moves = list(game.mainline_moves())
        self.current_move = -1

        # Redraw the board
        self.draw_board()

    def next_move(self):
        if self.current_move < len(self.moves) - 1:
            self.current_move += 1
            self.board.push(self.moves[self.current_move])
            self.draw_board()

    def prev_move(self):
        if self.current_move >= 0:
            self.board.pop()
            self.current_move -= 1
            self.draw_board()