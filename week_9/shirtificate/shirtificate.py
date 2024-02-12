# from fpdf import FPDF




















# class PDF():
#     def __init__(self, name):
#         self._pdf = FPDF()
#         self._pdf.add_page()
#         self._pdf.set_font("helvetica", "B" , 50)
#         self._pdf.cell(0,60, 'CS50 Shirticate', ln=1, align='C')
#         self._pdf.image("shirtificate.png", w=self._pdf.epw)
#         self._pdf.set_font_size(30)
#         self._pdf.set_text_color(255,255,255)
#         self._pdf.text(x=47.5,txt = f"{name} took CS50")

#         def save(self, name ):
#             self._pdf.output(name)




# name = input("Name: ")
# pdf = PDF(name)
# pdf.save("shirtificate.pdf")




from fpdf import FPDF



class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 10, 70, 190)
        self.set_font("helvetica", "", 48)
        self.cell(0, 57, "CS50 Shirtificate", align="C")
        self.ln(20)


def main():
    name = input("Name: ")
    shirt(name)


def shirt(s):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, 213, f"{s} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
