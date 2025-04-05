import tkinter as tk
import chess
import chess.svg
from PIL import Image, ImageTk
import cairosvg
import io

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = chess.Board()
        self.selected_square = None  # Store selected piece
        self.canvas = tk.Canvas(root, width=500, height=500)
        self.canvas.pack()
        self.update_board()
        self.canvas.bind("<Button-1>", self.on_click)

    def update_board(self):
        board_svg = chess.svg.board(self.board, size=400)
        board_png = self.svg_to_png(board_svg)
        self.image = ImageTk.PhotoImage(board_png)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

    def svg_to_png(self, svg_data):
        png_data = cairosvg.svg2png(bytestring=svg_data.encode('utf-8'))
        return Image.open(io.BytesIO(png_data))

    def on_click(self, event):
        square_size = 400 // 8
        col = event.x // square_size
        row = 7 - (event.y // square_size)  # Convert to chess row index
        clicked_square = chess.square(col, row)

        if self.selected_square is None:
            # Select a piece
            if self.board.piece_at(clicked_square):
                self.selected_square = clicked_square
        else:
            # Attempt to move
            move = chess.Move(self.selected_square, clicked_square)
            if move in self.board.legal_moves:
                self.board.push(move)  # Make move if legal
            self.selected_square = None  # Reset selection
            self.update_board()

if __name__ == "__main__":
    root = tk.Tk()
    ChessGUI(root)
    root.mainloop()

