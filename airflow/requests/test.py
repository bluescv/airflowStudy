import requests


class HTTPPost:
    def doPost(self):
        payload = {'key1': 'value1', 'key2': 'value2'}
        r = requests.post("http://localhost:8000", data=payload)
        print(r.text)


if __name__ == '__main__':
    try:
        http = HTTPPost
        http.doPost(http)

    except KeyboardInterrupt:
        print("Quit!")
    pass
