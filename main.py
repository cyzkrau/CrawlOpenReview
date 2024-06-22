import json
import requests
from requests.exceptions import RequestException
import argparse

def get_page_index(parameter, url):
    for i in parameter:
        url = url + f'{i}={parameter[i]}&'
    try:
        response=requests.get(url[:-1])
        return response.text
    except RequestException:
        print("Error request")

def main(path, url, parameter):
    data = []
    for offset in range(10000):
        parameter['offset'] = 25 * offset
        html = json.loads(get_page_index(parameter, url))
        if html['notes'] == []:
            break
        for item in html['notes']:
            data.append({})
            for key in ['title', 'authorids', 'keywords', 'abstract', '_bibtex']:
                if key in item['content'].keys():
                    data[-1][key] = item['content'][key]['value']
    if data == []:
        print('failed')
    else:
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f'succeed load into {path}')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A simple calculator")
    parser.add_argument('--year', type=str, help='which year')
    parser.add_argument('--name', type=str, help='which conference')
    parser.add_argument('--type', type=str, help='oral or spotlight or poster')
    args = parser.parse_args()

    domain = {
        'UAI': f'auai.org%2FUAI%2F{args.year}%2FConference',
        'ICLR': f'ICLR.cc%2F{args.year}%2FConference',
        'ICML': f'ICML.cc%2F{args.year}%2FConference&invitation=ICML.cc%2F{args.year}%2FConference%2F-%2FSubmission',
        'NeurIPS': f'NeurIPS.cc%2F{args.year}%2FConference',
    }

    print(f"Begin loading data in {args.name}{args.year}{args.type}")
    main(
        f'./data/{args.year}{args.name}{args.type}.json',
        'https://api2.openreview.net/notes?',
        {
            'content.venue': f'{args.name}%20{args.year}%20{args.type}',
            'details': 'replyCount%2Cpresentation',
            'domain': domain[args.name],
            'limit': 25,
            'offset': 0,
        }
    )
