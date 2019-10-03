import requests
import html
class Util:
    def get_uuid_from_name(self, player_name):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36'}
        page = requests.get('https://mcuuid.net/?q=' + player_name, headers=headers)
        doc = html.fromstring(page.content)
        xpath_full_uuid = '/html/body/div/div[2]/ul/li/div/div[2]/table/tbody/tr[1]/td[2]/input/@value'
        raw_uuid = doc.xpath(xpath_full_uuid)
        uuid = ''.join(raw_uuid)
        return uuid if uuid != '' else None
