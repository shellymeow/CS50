from fpdf import FPDF

class PDF(FPDF):
    def header(self):

        # 1. Rendering picture:
        self.image("./shirtificate.png", 30, 100, 150, 150)

        # 2. Adding title
        # Setting font: helvetica bold 40
        self.set_font("helvetica", "B", 40)
        self.title = "CS50 shirtificate"
        # setting position of title
        width = self.get_string_width(self.title) + 6
        x_pos = (210 - width) / 2
        self.set_xy(x_pos,50)
        # creating title on top of the page
        self.cell(w = width, h = 20, txt=self.title, border=0, align="C")

    # adding user name
    def user_name(self):
        #
        self.add_page()
        name = input("Name: ")
        text = name + " " + "took CS50"

        # 2. add txt on shirt
        # setting font and color
        self.set_font("helvetica", "", 28)
        self.set_text_color(255,255,255)

        # center the name text
        width = self.get_string_width(text) + 6
        x_pos = (210 - width) / 2
        self.set_xy(x_pos,150)

        # Printing user name:
        self.cell(w=width, h=28, txt=text, border=0, align="C")


def main():
    pdf = PDF()
    pdf.user_name()
    # save
    pdf.output("shirtificate.pdf")




if __name__ == "__main__":
    main()
