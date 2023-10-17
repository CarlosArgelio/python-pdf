import pdfkit
import bs4

class BuilderReport():

    @property
    def logo(self) -> None:
        pass

    @property
    def date(self) -> None:
        pass

    @property
    def contact_information(self) -> None:
        pass

    @property
    def paginate(self) -> None:
        pass

    @property
    def watermark(self) -> None:
        pass

    @property
    def report_information(self) -> None:
        pass


class Report():

    def __init__(self) -> None:

        with open('/home/carlos/work/projects/python/pdf/src/templates/reports/index.html', 'r') as f:
            file = f.read()

        self.report = file

    def add(self, release) -> None:
        self.report = release
        # print('REPORT')
        # print(self.report)

    def __str__(self) -> None:
        return str()


class ConcreteReport(BuilderReport):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._report = Report()

        with open('/home/carlos/work/projects/python/pdf/src/index.html', 'r') as f:
            report = f.read()

        self._soup = bs4.BeautifulSoup(report, "html.parser")

    @property
    def soup(self):
        return self._soup

    @soup.setter
    def soup(self, soup):
        self._soup = soup

    @property
    def report(self) -> Report:

        report = self._report
        self.reset()
        return report

    def produce_logo(self, image: str = None) -> None:
        img = self._soup.find_all("img")
        if image is not None:
            img[0]['src'] = image

        img[0]['src'] = "../../../assets/logo.avif"


        html = self._soup.prettify()

        self.report.add(html)

    def produce_date(self) -> None:
        pass

    def produce_contact_information(self) -> None:
        pass

    def produce_paginate(self) -> None:
        pass

    def produce_watermark(self) -> None:
        pass

    def produce_report_information(self) -> None:
        pass


class Director:

    def __init__(self) -> None:
        self._report = None

    @property
    def report(self) -> BuilderReport:
        return self._report

    @report.setter
    def report(self, builder: BuilderReport) -> None:
        self._report = builder

    def build_logo(self, logo: str = None):
        self.report.produce_logo(logo)


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

    # Create director
    director = Director()

    # Create builder
    builder = ConcreteReport()

    director.report = builder

    # Build pdf

    director.build_logo()

    print(builder.soup)



    # report = GenerateReport(False, 'logo', 'name', '')
    # # my_report = report.add_content()

    # logo = report.add_logo()

    # print(logo)

    # # report.create_pdf()
