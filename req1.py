import requests

def check_status(sites, timeout=None):
    results = {}
    for site in sites:
        try:
            response = requests.get(url=site, timeout=timeout)
            if response.status_code != 200:
                results[site] = response.status_code
        except requests.exceptions.RequestException as e:
            results[site] = str(e)

    return results

if __name__ == "__main__":
    sites = [
        "https://google.com",
        "https://google.com/fdfsfs",
        "https://check.eva.ua/",
        "https://bebra.ru",
        "https://www.cloudflare.com/ru-ru/dghkdetgk/",
        "https://packages.ubuntu.com/bionic/libs/libguac-client-rdp0/45556",
        "http://localhost:3303"
    ]
    timeout = 5
    results = check_status(sites, timeout)
    for site, error_code in results.items():
        print(f"{site}: {error_code}")
