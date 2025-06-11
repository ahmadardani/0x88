import sys
from PySide6 import QtWidgets
from programui_ui import Ui_MainWindow  # Pastikan file ini sudah dihasilkan dari Qt Designer

class MyProgram(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Hubungkan tombol btnFill dengan fungsi
        self.ui.btnFill.clicked.connect(self.fill_code)

    def fill_code(self):
        # Ambil teks dari plainText
        input_text = self.ui.plainText.toPlainText()
        lines = input_text.strip().splitlines()

        # Mulai membentuk HTML
        html_output = [
            "<!DOCTYPE html>",
            "<html>",
            '    <link href="/styles.css" rel="stylesheet" type="text/css" />',
            "<head>",
            '    <meta charset="UTF-8">',
            "    <title>Anki 200 Part 1</title>",
            "</head>",
            '<div class="container">',
            '    <div class="blog-post">',
            "        <h2>Anki Kaishi 1.5 K</h2>",
            "        <h3>200 Part 1</h3>",
            "            <p>"
        ]

        # Tambahkan baris-baris kalimat Jepang ke dalam tag <br>
        for i, line in enumerate(lines, start=1):
            html_output.append(f"            <br>{i}. {line}")

        html_output.append("            <br>")
        html_output.append('            <br><b>[ 1 ]</b>')

        # Tambahkan link ke halaman 2 hingga 10
        for i in range(2, 11):
            html_output.append(f'                <a href="{i}.html">[ {i} ]</a>')

        html_output.append("            </p>")
        html_output.append('            <p><a href="/index.html">[ Back ]</a></p>')
        html_output.append("    </div>")
        html_output.append("</div>")
        html_output.append("</html>")

        # Gabungkan jadi satu string dan tampilkan di plainCode
        self.ui.plainCode.setPlainText("\n".join(html_output))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyProgram()
    window.show()
    sys.exit(app.exec())
