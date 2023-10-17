import pdfkit
import bs4

class GenerateReport:
    def __init__(self, watermark: bool, logo, name, info) -> None:
        self.watermark = watermark
        self.logo = logo
        self.info = info
        self.name = name

        with open('/home/carlos/work/projects/python/pdf/templates/static/informe.html', 'r') as f:
            file = f.read()

        self.html = file
    
    def soup_parse(self):
        soup = bs4.BeautifulSoup(self.html, "html.parser")
        return soup
    
    def get_label(self, label, value):
        pass

    def front_page(self):
        pass

    def watermark(self):
        pass

    def add_logo(self):
        soup = self.soup_parse()

        img = soup.find_all("img")
        img[0]['src'] = "../../assets/logo.avif"

        html = soup.prettify()

        return html

    def info(self):
        pass

    def add_content(self):
        """
        Content:
        [
            {
                conten1 ==> ref page 1
            },
            {
                content2 ==> ref page 2
            }
        ]
        """

        # pages = len(self.info)

        content = [
            {
                'type': "front-page",
                'label': 'h1',
                'content': 'Report'
            }
        ]

        soup = self.soup_parse()

        h1_tags = soup.find_all("h1", text="Informe")

        if h1_tags:
            h1_tag = h1_tags[0]
        else:
            h1_tag = bs4.BeautifulSoup.new_tag(soup, "h1")
            h1_tag.string = "Informe"
            soup.body.insert(0, h1_tag)
        
        html = soup.prettify()

        return html

    def create_pdf(self):
        if self.html is not None:
            pdf = pdfkit.from_string(self.html, f'{self.name}.pdf')
            return pdf
        else:
            raise Exception('variable html cannot be type None')


if __name__ == '__main__':
    
    report = GenerateReport(False, 'logo', 'name', '')
    # my_report = report.add_content()

    logo = report.add_logo()

    print(logo)

    # report.create_pdf()