from PyQt6.QtWidgets import (QMainWindow, QApplication, QTabWidget, QToolBar,
                             QPushButton, QFileDialog)
from PyQt6.QtGui import QIcon
from pdf_functions import merge_pdfs, split_pdf, add_text
import sys

class PDFTool(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced PDF Tool")
        self.setGeometry(100, 100, 1000, 700)

        # Tabs for multiple PDFs
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Toolbar
        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)
        self.add_toolbar_buttons()

    def add_toolbar_buttons(self):
        merge_btn = QPushButton(QIcon("icons/merge.png"), "Merge PDFs")
        merge_btn.clicked.connect(self.merge_pdfs_action)
        self.toolbar.addWidget(merge_btn)

        split_btn = QPushButton(QIcon("icons/split.png"), "Split PDF")
        split_btn.clicked.connect(self.split_pdf_action)
        self.toolbar.addWidget(split_btn)

        text_btn = QPushButton(QIcon("icons/text.png"), "Add Text")
        text_btn.clicked.connect(self.add_text_action)
        self.toolbar.addWidget(text_btn)

        # More buttons can be added: highlight, image, rotate, extract pages

    def merge_pdfs_action(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select PDFs to merge", "", "PDF Files (*.pdf)")
        if files:
            output, _ = QFileDialog.getSaveFileName(self, "Save Merged PDF As", "", "PDF Files (*.pdf)")
            if output:
                merge_pdfs(files, output)

    def split_pdf_action(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select PDF to split", "", "PDF Files (*.pdf)")
        folder = QFileDialog.getExistingDirectory(self, "Select output folder")
        if file and folder:
            split_pdf(file, folder)

    def add_text_action(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select PDF", "", "PDF Files (*.pdf)")
        output, _ = QFileDialog.getSaveFileName(self, "Save PDF As", "", "PDF Files (*.pdf)")
        if file and output:
            add_text(file, output, "Sample Text", x=50, y=50, fontsize=14)

def main():
    app = QApplication(sys.argv)
    window = PDFTool()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
