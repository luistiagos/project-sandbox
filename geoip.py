import geoip2.database

def obter_localizacao_por_ip(ip):
    reader = geoip2.database.Reader('GeoLite2-City.mmdb')
    try:
        response = reader.city(ip)
        pais = response.country.name
        cidade = response.city.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        return pais, cidade, latitude, longitude
    except geoip2.errors.AddressNotFoundError:
        return None, None, None, None

# Exemplo de uso
ip = '186.206.45.225'  # Substitua pelo endereço IP desejado
pais, cidade, latitude, longitude = obter_localizacao_por_ip(ip)
if pais and cidade:
    print(f'Localização: {cidade}, {pais} ({latitude}, {longitude})')
else:
    print('Localização não encontrada.')
