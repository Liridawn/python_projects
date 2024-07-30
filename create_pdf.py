from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font("Helvetica", "B", 16)

pdf.cell(200, 10, "Bash commands cheat sheet", ln=True, align="C")

pdf.set_font("Helvetica", size=12)

content = """

"""

pdf.multi_cell(0, 10, content)

pdf.output("bash_commands_cheat_sheet.pdf")