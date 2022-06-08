from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

document = Document()
grid_t_style = document.styles["Table Grid"]
table = document.add_table(12, 7)
table.style = grid_t_style

# 1. 부동산의 표시
table.cell(0, 0).merge(table.cell(0, 6))
table.cell(1, 1).merge(table.cell(1, 6))
table.cell(2, 2).merge(table.cell(2, 4))

table.rows[0].cells[0].text = '임대인과 임차인 쌍방은 아래 표시 부동산에 관하여 다음 계약내용과 같이 임대차계약을 체결한다.'

# for r in range(len(table.rows)):
#     row = table.rows[r]
#     for c in range(len(row.cells)):
#         cell = row.cells[c]
#         cell.text = str.format("{0},{1}",r,c)

# 2.계약 내용
table.cell(3, 0).merge(table.cell(3, 6))
table.cell(4, 1).merge(table.cell(4, 3))


document.save("table4.docx")
