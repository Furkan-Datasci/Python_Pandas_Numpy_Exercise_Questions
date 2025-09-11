message = 'Hello There. my name is Sadık Turan'

# message = message.upper()         <<Bütün harfleri büyük yazar
# message = message.lower()         <<Bütün harfleri küçük yazar
# message = message.title()         <<Kelimelerin baş harflerini büyük yazar
# message = message.capitalize()    <<dizenin ilk karakterini büyük harfe ve kalan karakterleri küçük harfe dönüştürmek için kullanılır.
# message = message.strip()         <<dizenin başındaki ve sonundaki boşlukları kaldırmaktır.
# message = message.split(' ')      <<parantezde belittiğimiz yeri cümlede kelime kelime ayırır.   
# message = message.split('.')      
# message = '...'.join(message)     <<mesajda her bir ayrılan yere ... koyar.

index = message.find('Sadık')
# index = message.find('Sadıkk')  << Böyle bir kelime olmadığından '-1' değerini okuruz.

# isFound = message.startswith('B')
isFound = message.endswith('B')

# print(isFound)

# message = message.replace('Sadık','Çınar')
# message = message.replace('ç','c')
#                  .replace('ö','o')
#                  .replace(' ','-')   

message = message.center(100,'*')

print(message)
# print(message[0])

######## Python strings metodlarını internete yaz w3school.com python sitesine bak 
