from datetime import datetime
from uuid import uuid4

import pdfkit
import bs4

from config import config


class BuilderReport():

    @property
    def produce_logo(self) -> None:
        pass

    @property
    def produce_date(self) -> None:
        pass

    @property
    def produce_front_page(self) -> None:
        pass

    @property
    def produce_contact_information(self) -> None:
        pass

    @property
    def produce_paginate(self) -> None:
        pass

    @property
    def produce_watermark(self) -> None:
        pass

    @property
    def produce_report_information(self) -> None:
        pass


class Report():

    def __init__(self) -> None:

        with open(f'{config.get("route")}/src/templates/reports/index.html', 'r') as f:
            file = f.read()

        self.report = file

    def add(self, release) -> None:
        self.report = release

    def __str__(self) -> None:
        return str()


class ConcreteReport(BuilderReport):

    def __init__(self) -> None:
        # self.reset()
        self.loads = {}

        self._report = Report()

        with open(f'{config.get("route")}/src/index.html', 'r') as f:
            report = f.read()

        self._soup = bs4.BeautifulSoup(report, "html.parser")

    # def reset(self) -> None:
    #     self._report = Report()

    #     with open(f'{config.get("route")}/src/index.html', 'r') as f:
    #         report = f.read()


    @property
    def soup(self):
        return self._soup

    @soup.setter
    def soup(self, soup):
        self._soup = soup

    @property
    def report(self) -> Report:

        report = self._report
        # self.reset()
        return report

    # @classmethod
    def load_file_tmp(self, type_file: str, route):

        # base_route = f'/tmp/{str(uuid4())}'
        # filename = route.split('/')[-1]

        # filename_tmp = f'{base_route}/{filename}'

        # with open(route, 'rb') as f:
        #     file = f.read()

        # with open(filename_tmp, 'wb') as f:
        #     f.write(file)

        self.loads['route'] = route

    def produce_logo(self, image: str = None) -> None:
        img = self._soup.find_all("img")
        if image is not None:
            img[0]['src'] = image

        try:
            img[0]['src'] = self.loads['route']
        except KeyError as e:
            raise Exception('Add route image')

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

    def produce_front_page(self, title) -> None:
        front_page = self._soup.find_all("h1")
        for h1 in front_page:
            if h1["class"] == ["title"]:
                h1.string.replace_with(title)

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

    def build_test_report(self, logo: str = None):
        self.report.produce_logo(logo)
        self.report.produce_date()
        self.report.produce_front_page('Titulo 1')


if __name__ == '__main__':

    # Create director
    director = Director()

    # Create builder
    builder = ConcreteReport()

    director.report = builder

    # Build pdf
    builder.load_file_tmp('type', f'{config.get("route")}/assets/logo.avif')
    director.build_test_report()

    html = builder.soup

    # print(html.prettify())

    with open('/tmp/file.html', 'w') as f:
        file = f.write(html.prettify())

    with open('/tmp/file.html', 'r') as f:
        f.read()

    pdfkit.from_file('/tmp/file.html', 'micro.pdf')
