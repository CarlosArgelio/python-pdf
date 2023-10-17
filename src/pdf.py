from datetime import datetime

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
        date = self._soup.find_all("div")
        date_now = datetime.today()

        # Transform date format ISO
        date_iso = date_now.strftime("%Y-%m-%d")

        for div in date:
            if div["class"] == ["fecha"]:
                p_tag = div.find("p")
                p_tag.string.replace_with(date_iso)

        html = self._soup.prettify()

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

    def build_date(self):
        self.report.produce_date()


if __name__ == '__main__':

    # Create director
    director = Director()

    # Create builder
    builder = ConcreteReport()

    director.report = builder

    # Build pdf

    director.build_logo()
    director.build_date()

    html = builder.soup

    with open('/tmp/file.html', 'w') as f:
        file = f.write(html.prettify())

    pdfkit.from_file('/tmp/file.html', 'micro.pdf')
