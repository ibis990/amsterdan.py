import socket

def get_ip_info(ip):
    try:
        data = socket.gethostbyaddr(ip)
        hostname, aliases, addresses = data
        print('Hostname :', hostname)
        print('Aliases  :', aliases)
        print('Addresses:', addresses)
    except socket.herror:
        print('O IP {} não foi encontrado'.format(ip))

# obtém informações de um IP
get_ip_info('8.8.8.8')

# obtém o país, estado, cidade, rua e bairro
import requests

def get_ip_geo_info(ip):
    url = 'http://ip-api.com/json/' + ip
    r = requests.get(url)
    data = r.json()
    if data['status'] == 'success':
        print('País   :', data['country'])
        print('Estado :', data['regionName'])
        print('Cidade :', data['city'])
        print('Rua    :', data['query'])
        print('Bairro :', data['isp'])
    else:
        print('O IP {} não foi encontrado'.format(ip))

# obtém informações geográficas de um IP
get_ip_geo_info('8.8.8.8')