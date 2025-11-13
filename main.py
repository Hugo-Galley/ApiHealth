import argparse
import requests

parser = argparse.ArgumentParser(description="CLI for API test")
parser.add_argument("file", help="Your file contains API link")
args = parser.parse_args()

def create_list_from_file(file):
    api_list = []
    with open(file, "r") as f:
        for lines in f:
            api_list.append(lines.strip())
    return api_list

def is_functional(response):
    return response.ok

def test_battery(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        print(f"✅ Votre Api {link} est fonctionnelle,"
              f" elle à pris {response.elapsed.total_seconds()} secondes "
              f"et à répondu avec le code {response.status_code}"
              f" avec une taille de {len(response.text.encode('utf-8'))} octets")
    except requests.exceptions.RequestException:
        print(f"❌ Api {link} non fonctionnelle")
if __name__ == "__main__":
    api_list = create_list_from_file(args.file)
    for api_link in api_list:
        test_battery(api_link)