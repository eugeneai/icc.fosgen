from docx import Document
from docx.shared import Inches


class Generator(object):

    def __init__(self, comps, table9):
        self.comps = comps
        self.table9 = table9
        self.doc = Document()

    def header(self, text, level):
        self.doc.add_heading(text, level)

    def add_results(self, header=False):
        if header:
            self.header("Результаты освоения дисциплины", 2)
        vals = list(self.table9.items())
        vals.sort()
        p = self.doc.add_paragraph(
            "В результате изучения дисциплины студенты должны:")
        for sect in ["знать", "уметь", "владеть"]:
            p = self.doc.add_paragraph("")
            r = p.add_run(sect + ":")
            r.bold = True
            r.italic = True
            for zun in vals:
                s = zun[1][0][1].strip()
                # ListNumber IntenseQuote
                if s.startswith(sect):
                    s = s.replace(sect, s, 1)
                    self.doc.add_paragraph(s, style='ListBullet')

    def save(self, filename):
        return self.doc.save(filename)
"""

table = document.add_table(rows=1, cols=3)
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Qty'
hdr_cells[1].text = 'Id'
hdr_cells[2].text = 'Desc'
for item in recordset:
    row_cells = table.add_row().cells
    row_cells[0].text = str(item.qty)
    row_cells[1].text = str(item.id)
    row_cells[2].text = item.desc

document.add_page_break()

document.save('demo.docx')
"""
