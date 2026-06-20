from fpdf import FPDF


def main():
    name = input("Name: ")
    create_shirtificate(name)


def create_shirtificate(name):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.set_auto_page_break(auto=False)
    pdf.add_page()

    pdf.set_font("Arial", "B", 35)
    pdf.cell(w=0, h = 10, txt="CS50 Shirtificate", border=0, align='C')
    pdf.image("shirtificate.png", x=25, y=50, w=160)
    pdf.set_text_color(255,255,255)

    pdf.set_font("Arial", "B", 20)
    pdf.set_text_color(255,255,255)
    pdf.text(x= 75, y = 125, txt = f"{name} took CS50")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()