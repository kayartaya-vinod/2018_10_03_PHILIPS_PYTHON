import requests
import json

def main():
    url = 'https://randomuser.me/api/'
    proxy_addresses = {'http': '165.225.96.34:9480'}
    resp = requests.get(url, proxies=proxy_addresses)
    # resp = requests.get(url)

    # print(dir(resp))
    print(resp.json())


if __name__=='__main__':
    main()
