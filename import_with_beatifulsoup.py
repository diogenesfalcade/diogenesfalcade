import requests
from bs4 import BeautifulSoup


# Function to extract html data
def getdata(url):
    r=requests.get(url)
    return r.text

data = getdata('https://economia.uol.com.br/cotacoes/cambio/')
soup = BeautifulSoup(data, 'html.parser')
for span in soup.find_all('input', class_='field normal'):
    print(span.get('value'))

# investing = getdata('https://br.investing.com/currencies/usd-brl')
# sopinha = BeautifulSoup(investing, 'html.parser')
# for div in sopinha.find_all('span', class_='text-2xl'):
#     print(div.text)
# for time in sopinha.find_all('time', class_= 'instrument-metadata_text__2iS5i font-bold'):
#     print(time.text)
# for pintos in sopinha.find_all('div', class_='text-xl flex items-end flex-wrap'):
#     print(pintos.text)


#<span class="instrument-price_change-value__jkuml ml-2.5 text-positive-main" data-test="instrument-price-change">+0,0005</span>
#<div class="text-xl flex items-end flex-wrap"><span class="instrument-price_change-value__jkuml ml-2.5 text-positive-main" data-test="instrument-price-change">+0,0005</span><span class="instrument-price_change-percent__19cas ml-2.5 text-positive-main" data-test="instrument-price-change-percent">(<!-- -->+0,01<!-- -->%)</span></div>

# data = getdata('https://www.google.com/search?q=dolar&oq=dolar&aqs=edge.0.69i59l3j0i131i433i512l6.777j0j4&sourceid=chrome&ie=UTF-8')
# soup = BeautifulSoup(data, 'html.parser')
# for span in soup.find_all('div', class_='BNeawe iBp4i AP7Wnd'):
#     print(span.text)

#print(soup.prettify())

#<span class="DFlfde SwHCTb" data-precision="2" data-value="5.266">5,27</span>
#<div class="dDoNo ikb4Bb gsrt"><span class="DFlfde SwHCTb" data-precision="2" data-value="5.266">5,27</span> <span class="MWvIVe" data-mid="/m/03385m" data-name="Real">Real</span></div>

#<div class="mr-2.5 text-xl self-center text-negative-main" data-test="header-dir"><svg viewBox="0 0 24 24" width="1em" fill="none" style="height:auto" class="text-negative-main text-lg" aria-hidden="true" data-test="arrow-down"><path fill-rule="evenodd" clip-rule="evenodd" d="M6 1V10.2632H1L12 23L23 10.2632H17.9V1H6Z" fill="currentColor"></path></svg></div>
#<span class="text-2xl" data-test="instrument-price-last">5,2660</span>
#<time class="instrument-metadata_text__2iS5i font-bold" datetime="2022-02-01T21:30:01.000Z">18:30:01</time>