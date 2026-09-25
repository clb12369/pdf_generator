from fpdf import FPDF
import pandas as pd

# Create PDF instance
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

# Read in data
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    for i in range(row['Pages']):
        pdf.add_page()

        # Add heading
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, text=row['Topic'], align="L", new_x="LMARGIN", new_y="NEXT", border=0)
        pdf.line(x1=10, y1=21, x2=200, y2=21)

        # Add footer
        #pdf.ln(265)
        pdf.set_y(-10)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, text=row['Topic'], align="R")

pdf.output("output.pdf")