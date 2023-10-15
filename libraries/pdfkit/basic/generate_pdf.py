import pdfkit

class GenerateReport:
    def __init__(self, watermark: bool, logo, name, info, html) -> None:
        self.watermark = watermark
        self.logo = logo
        self.info = info
        self.name = name
        self.html = html

    def watermark(self):
        pass

    def logo(self):
        pass

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

        pages = len(self.info)

    def create_pdf(self):
        if self.html is not None:
            pdf = pdfkit.from_string(self.html, f'{self.name}.pdf')
            return pdf
        else:
            raise Exception('variable html cannot be type None')


if __name__ == '__main__':

    with open('/home/carlos/work/projects/python/pdf/templates/static/informe.html', 'r') as f:
        html = f.read()
    
    report = GenerateReport(False, 'logo', 'name', '', html)
    report.create_pdf()