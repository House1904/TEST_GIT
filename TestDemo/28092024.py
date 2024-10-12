class Label:
    def __init__(self, text, font):
        self._text = text
        # hoặc self.set_text(text)
        self._font = font

    def get_text(self):
        return self._text

    def set_text(self, value):
        self._text = value.upper() # Attached behavior

    def get_font(self):
        return self._font

    def set_font(self, value):
        self._font = value

label = Label("Fruits", "Drinks")
print(label.get_text())

label.set_text("Vegetables")
print(label.get_text())