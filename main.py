from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from tictactoe import TicTacToe

class TicTacToeApp(App):
    def build(self):
        self.game = TicTacToe()
        layout = GridLayout(cols=3)
        self.buttons = []

        for i in range(9):
            button = Button()
            button.bind(on_release=self.on_button_click)
            self.buttons.append(button)
            layout.add_widget(button)

        return layout

    def on_button_click(self, button):
        position = self.buttons.index(button)
        self.game.make_move(position)
        button.text = self.game.board[position]
        winner = self.game.check_winner()

        if winner:
            if winner == "Tie":
                self.root.parent.parent.ids.status_label.text = "It's a Tie!"
            else:
                self.root.parent.parent.ids.status_label.text = f"{winner} wins!"
            for b in self.buttons:
                b.disabled = True

if __name__ == "__main__":
    TicTacToeApp().run()
