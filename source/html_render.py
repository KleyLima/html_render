# -*- coding: utf-8 -*-

from jinja2 import Environment, PackageLoader, select_autoescape

class HtmlRender:
    def __init__(self):
        self.env = Environment(loader=PackageLoader('html_render', 'pages'), autoescape=select_autoescape(['html']))

        page = self.env.get_template('resposta.html')
        out = page.render(resp=['1','2','3'], sample = 'AMOSTRA')
        print(out)

if __name__ == '__main__':
    HtmlRender()

