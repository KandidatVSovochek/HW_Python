from address import address
from mailing import Mailing

to_address = address(123456, 'NYX', '5th Avenue', 8, 15)
from_address = address(147258, 'LA', 'Main street', 6, 78)
track = 159357789123
cost = 25
Mail = Mailing(to_address, from_address, track, cost)

print(f"Отправление {Mail.track} из {Mail.from_address}"
      f"в {Mail.to_address}. Стоимость {Mail.cost}")
