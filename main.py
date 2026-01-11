from file import run


def premier(n):
    if n <= 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def build(ui):
    ui.set_title("verifier les nombres premiers")
    ui.set_heading("verifier qu'un nombre soit premier.")
    ui.set_description("tapper un nombre pour verifier")
    ui.set_input_label("nombre:")
    ui.set_placeholder("exemple: 17")
    ui.set_button_text("valider")

    def on_click():
        text = ui.input_box.text().strip()

        if not text.isdigit():
            ui.set_output("Error: enter a positive integer.")
            return

        n = int(text)
        ui.set_output(
            "C'est un nombre premier."
            if premier(n)
            else "ce n'est pas un nombre premier."
        )

    ui.button.clicked.connect(on_click)


run(build)
