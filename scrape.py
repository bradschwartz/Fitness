from urllib import request
import bs4


def get_html(site_url):
    html_object = request.urlopen(site_url)
    data = html_object.read()
    return data


def get_class_summary(soup):
    summary = soup.find(name='div', attrs={'class':'summary-excerpt'})
    raw_html = summary.decode_contents()
    return raw_html


def main(site='http://www.wdfitness.com/drivex/'):
    html = get_html(site)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    summary = get_class_summary(soup)

    return summary

if __name__ == '__main__':
    main()
