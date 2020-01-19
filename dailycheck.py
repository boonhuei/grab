# in crontab use cd /<path to script> && /<path to python>/python3 /<path to script>/script.py
#
import subprocess
from random import randint
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
#http://tardis.tiny-vps.com/aarm/packages/g/geckodriver/geckodriver-0.23.0-1-aarch64.pkg.tar.xz
USER_AGENTS = [
"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
 "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
"Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
"Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
"Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
"Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]


subprocess.run(['pkill','geckodriver'])
subprocess.run(['pkill','firefox-esr'])


#headless for Firefox
from selenium.webdriver.firefox.options import Options
options = Options()
options.headless = True
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)

IMI='https://eservices.imi.gov.my/myimms/myPermit.semak?type=46&lang=en&appType=p'
#XE='https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=MYR'
FX='https://finance.yahoo.com/quote/MYR%3DX'
GEG='https://finance.yahoo.com/quote/0027.HK'
SC='https://finance.yahoo.com/quote/1383.HK'

random_agent = USER_AGENTS[randint(0, len(USER_AGENTS)-1)]
headers = {'User-Agent':random_agent,}
driver.get(IMI)
APPLICATIONID = "EPJQ15000734"
INPUT_FIELD = (By.XPATH, "//input[@id='noRuj']")
PREVIEW_BTN = (By.XPATH, "//input[@id='carian']")
WebDriverWait(driver,20).until(EC.element_to_be_clickable(INPUT_FIELD)).send_keys(APPLICATIONID)
WebDriverWait(driver,20).until(EC.element_to_be_clickable(PREVIEW_BTN)).click()
MPR = 'Malaysia PR: '+driver.find_element_by_xpath("//table[@class='warning tblwidth']").text


random_agent = USER_AGENTS[randint(0, len(USER_AGENTS)-1)]
headers = {'User-Agent':random_agent,}
driver.get(SC)
STK = driver.find_element_by_xpath("//h1[@class='D(ib) Fz(18px)']").text
PRICE = driver.find_element_by_xpath("//span[@class='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']").text
RESOLUTION = driver.find_element_by_xpath("//span[@class='Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($dataRed)']").text
PC = driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/table[1]/tbody[1]/tr[1]/td[2]/span[1]").text
B = driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/table[1]/tbody[1]/tr[3]/td[2]").text
A = driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/table[1]/tbody[1]/tr[3]/td[2]").text
DRANGE = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[2]").text
YRANGE = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[6]/td[2]").text
MSG = STK + '\nPrice: ' + PRICE +'\t\t\t' + RESOLUTION + '\nPrevious Close: ' + PC + '\nBid: ' + B + '\nAsk: ' + A + '\nDay Range: ' + DRANGE + '\nYear Range: ' + YRANGE


random_agent = USER_AGENTS[randint(0, len(USER_AGENTS)-1)]
headers = {'User-Agent':random_agent,}
driver.get(GEG)
STK = driver.find_element_by_xpath("//h1[@class='D(ib) Fz(18px)']").text
PRICE = driver.find_element_by_xpath("//span[@class='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']").text
RESOLUTION = driver.find_element_by_xpath("//span[@class='Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($dataRed)']").text
PC = driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/table[1]/tbody[1]/tr[1]/td[2]/span[1]").text
B = driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/table[1]/tbody[1]/tr[3]/td[2]").text
A = driver.find_element_by_xpath("//body/div/div/div/div/div/div/div/div/div/div/div/div/div/div[1]/table[1]/tbody[1]/tr[3]/td[2]").text
DRANGE = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[2]").text
YRANGE = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[6]/td[2]").text
MSG = MSG+'\n\n'+STK + '\nPrice: ' + PRICE +'\t\t\t' + RESOLUTION + '\nPrevious Close: ' + PC + '\nBid: ' + B + '\nAsk: ' + A + '\nDay Range: ' + DRANGE + '\nYear Range: ' + YRANGE

#subprocess.run(['signal-cli','-u','+8613128550603','send,'-m',MSG,'+84961031144'])


random_agent = USER_AGENTS[randint(0, len(USER_AGENTS)-1)]
headers = {'User-Agent':random_agent,}
driver.get(FX)
FXRATE = driver.find_element_by_xpath("//span[@class='Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)']").text
#FXRATE = (By.XPATH,"//span[@class='converterresult-toAmount']")
WebDriverWait(driver,20).until(EC.element_to_be_clickable(FXRATE))
XERATE='USD1 = MYR'+WebDriverWait(driver,20).until(EC.element_to_be_clickable(FXRATE)).text
driver.close()

#signal-cli -u USERNAME updateGroup -n "Group name" -m [MEMBER [MEMBER  ^`  ^`^k]]

subprocess.run(['/usr/bin/signal-cli', '-u','+8613128550603','--config','/home/boonhuei_low/.local/share/signal-cli/', 'send','-m',MPR+'\n\n'+XERATE+'\n\n'+MSG, '+84961031144'])
#subprocess.run(['/usr/bin/signal-cli', '-u','+8613128550603', 'send','-m',MPR+'\n\n'+XERATE+'\n\n'+MSG, '-g' ,'Daily Update'])

subprocess.run(['pkill','geckodriver'])
subprocess.run(['pkill','firefox-esr'])
