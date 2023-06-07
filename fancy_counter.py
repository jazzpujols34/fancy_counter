import tkinter as tk
import colorsys

class CounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fancy Counter")
        self.root.geometry("300x200")

        self.count = 0

        self.label = tk.Label(root, text=self.count, font=("Helvetica", 24), bg="white")
        self.label.pack()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.increment_button = tk.Button(self.button_frame, text="Increment", command=self.increment)
        self.increment_button.pack(side="left", fill="both", expand=True)

        self.emoji_label = tk.Label(self.button_frame, text="😊", font=("Helvetica", 24), bg="white")
        self.emoji_label.pack(side="left")

        self.decrement_button = tk.Button(self.button_frame, text="Decrement", command=self.decrement)
        self.decrement_button.pack(side="left", fill="both", expand=True)

    def increment(self):
        self.count += 1
        self.label.config(text=self.count)
        self.emoji_label.config(text="😊")
        self.update_color()

    def decrement(self):
        self.count -= 1
        self.label.config(text=self.count)
        self.emoji_label.config(text="😞")
        self.update_color()

    def update_color(self):
        hue = 0.33 if self.count < 0 else 0  # green for negative, red for positive
        abs_count = abs(self.count)
        lightness = max(1 - abs_count * 0.01, 0)  # decrease lightness with count
        r, g, b = colorsys.hls_to_rgb(hue, lightness, 1)
        color = '#%02x%02x%02x' % (int(r*255), int(g*255), int(b*255))

        self.root.config(bg=color)
        self.label.config(bg=color)
        self.emoji_label.config(bg=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = CounterApp(root)
    root.mainloop()
