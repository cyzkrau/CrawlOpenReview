import requests
from bs4 import BeautifulSoup
import argparse

def pdf_bib(id, path):
    proxies = {
        "http": "127.0.0.1:7890",
        "https": "127.0.0.1:7890",
    }
    _abs = f'https://arxiv.org/abs/{id}'
    _pdf = f'https://arxiv.org/pdf/{id}'
    print(f"searching for {_abs}")
    
    soup = BeautifulSoup(requests.get(_abs, proxies=proxies).text, "html.parser")
    authors = [link.get_text() for link in soup.find("div", {"class": "authors"}).find_all('a')]
    title = soup.find('meta', property='og:title')['content'].split(' ')
    lastname1 = authors[0].split(' ')[-1].lower()
    _id = f'{lastname1}20{id[:2]}' + (title[0].lower() if len(title[0]) > 1 else title[1].lower())
    print(_id)

    _bib = f'''@article{{{_id},
        title={' '.join(title)},
        author={' and '.join([author.split(' ')[-1] + ', ' + ' '.join(author.split(' ')[:-1]) for author in authors])},
        journal={f'arXiv preprint arXiv:{id}'},
        year={_id[-4:]}
    }}'''

    req = requests.get(_pdf, proxies=proxies)
    if req.status_code != 200:
        print('fail downloading')
        return
    try:
        with open(f'{path}{_id}.pdf', 'wb') as f:
            f.write(req.content)
            print(f'sucessfully downloaded\n\n{_bib}')
    except Exception as e:
        print(e)
 
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Arxiv downloader")
    parser.add_argument('--id', type=str, help='arxiv id')
    parser.add_argument('--path', type=str, default='./', help='where to download')
    args = parser.parse_args()
    pdf_bib(args.id, args.path)
        
