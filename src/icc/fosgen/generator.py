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
        lvals = len(vals)
        for sect in ["знать", "уметь", "владеть"]:
            p = self.doc.add_paragraph("")
            r = p.add_run(sect + ":")
            r.bold = True
            r.italic = True
            for row, zun in enumerate(vals):
                s = zun[1][0][1].strip()
                # ListNumber IntenseQuote
                if s.startswith(sect):
                    s = s.replace(sect, "", 1)
                    if row == lvals - 1:
                        end = '.'
                    else:
                        end = ";"
                    self.doc.add_paragraph(s + end, style='ListBullet')

    def add_table9_WP(self, header=True, page_breaks=True):
        # self.doc.add_paragraph(
        #    "(Таблица размещается на отдельном листе в Landscape)")
        if page_breaks:
            self.doc.add_page_break()
        if header:
            self.doc.add_paragraph(
                "Таблица 9 – Контролируемые элементы"
                "содержания дисциплины и виды учебных работ, "
                "по результатам выполнения которых и отчета"
                "по ним осуществляется текущий контроль")
        t9 = self.doc.add_table(rows=len(self.table9) + 3, cols=4 + 3 * 4)
        t9.style = 'TableGrid'
        cs = t9.rows[0].cells
        ls = t9.rows[2].cells
        cs[0].merge(ls[0])
        cs[0].text = "№\nп/п"
        cs[1].merge(ls[1])
        cs[1].text = "Контролируемые элементы содержания дисциплины"
        cs[2].merge(ls[2])
        cs[2].text = "Компетенции"
        cs[3].merge(ls[3])
        cs[3].text = "№ раздела, темы\nпо табл. 2"

        cs[4].merge(cs[-1])
        cs[4].text = "Текущий контроль успеваемости (ТК)"

        off = 4
        tk = t9.rows[2].cells
        tk2 = t9.rows[1].cells
        for i, iname in enumerate(["ЛР № по\nтабл. 3", "ПЗ/СЕМ №\nпо табл.4", "СРС № по\nтабл.5", "КП (КР) №\nпо табл.7"]):
            a = off + i * 3
            b = a + 2
            tk2[a].merge(tk2[b])
            tk2[a].text = iname
            for j in range(3):
                tk[off + i * 3 + j].text = "ТК № {}".format(j + 1)

        t9rows = list(self.table9.items())
        t9rows.sort()
        for k, t9row in t9rows:
            f5, rest = t9row[0], t9row[1:]

            comp = f5[2].strip().replace(" ", "\n")
            f5[2] = comp

            off = 0
            c = t9.rows[k + 2].cells
            for i, it in enumerate(f5):
                c[off + i].text = it
            off = 4
            x = off
            for i, ig in enumerate(rest):
                for j, jt in enumerate(ig):
                    c[x].text = jt
                    x += 1

        if page_breaks:
            self.doc.add_page_break()

    def save(self, filename):
        return self.doc.save(filename)
"""

table =
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
