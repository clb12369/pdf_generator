from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, text="Hello There!", align="L", ln=1, border=1) # Course
pdf.cell(w=0, h=12, text="Hello There!", align="L", new_x="LMARGIN", new_y="NEXT", border=0)
pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, text="Hi There!", align="L", new_x="LMARGIN", new_y="NEXT", border=0)

pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
# pdf.cell(w=0, h=12, text="Hello There!", align="L", ln=1, border=1) # Course
pdf.cell(w=0, h=12, text="Hello There!", align="L", new_x="LMARGIN", new_y="NEXT", border=0)
pdf.set_font(family="Times", size=10)
pdf.cell(w=0, h=12, text="Hi There!", align="L", new_x="LMARGIN", new_y="NEXT", border=0)
pdf.output("output.pdf")