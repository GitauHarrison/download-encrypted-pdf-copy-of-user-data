from fpdf import FPDF
from app.models import User

users = User.query.all()

def download_users_data():
    PDF()


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('app/static/images/logo.jpg', 180, 8, 12)
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(50, 10, 'Fake Users Demo', 1, 0, 'C')
        # Line break
        self.ln(20)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', '', 8)
        self.set_text_color(128)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def table(self):
        # Colors, line width and bold font
        self.set_font('Arial', 'B', 16)
        self.set_fill_color(255, 0, 0)
        self.set_text_color(255)
        self.set_draw_color(128, 0, 0)
        self.set_line_width(.3)
        self.set_font('', 'B')
        # Header
        self.cell(25, 10, 'Name', 1, 0, 'C', 1)
        self.cell(10, 10, 'Age', 1, 0, 'C', 1)
        self.cell(75, 10, 'Address', 1, 0, 'C', 1)
        self.cell(40, 10, 'Phone', 1, 0, 'C', 1)
        self.cell(45, 10, 'Email', 1, 0, 'C', 1)
        self.ln()
        # Data
        self.set_text_color(0)
        self.set_font('Arial', '', 8)
        for user in users:
            self.cell(25, 10, user.name, 1, 0, 'C')
            self.cell(10, 10, str(user.age), 1, 0, 'C')
            self.cell(75, 10, user.address, 1, 0, 'C')
            self.cell(40, 10, user.phone, 1, 0, 'C')
            self.cell(45, 10, user.email, 1, 1, 'C')
        # Closing line
        self.cell(0, 10, '', 0, 1)

    def __init__(self):
        super().__init__(format='A4')
        self.alias_nb_pages()
        self.add_page()
        self.set_font('Arial', '', 12)
        self.table()
        self.output('app/static/files/users.pdf', 'F')
