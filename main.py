import requests
from bs4 import BeautifulSoup
import smtplib
from config import MY_MAIL, APP_PASSWORD, SMTP_ADDRESS
from email.message import EmailMessage



URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
# URL = "https://www.amazon.com/dp/B0F9B9R5J9/ref=sspa_dk_detail_1?pd_rd_i=B0F9B9R5J9&pd_rd_w=ZmAlg&content-id=amzn1.sym.85ceacba-39b1-4243-8f28-2e014f9512c7&pf_rd_p=85ceacba-39b1-4243-8f28-2e014f9512c7&pf_rd_r=5X7YNZNF9S2W8711RKHQ&pd_rd_wg=uYJ1Y&pd_rd_r=473e1c8e-d28d-43b1-9be3-aca4e00ef0f0&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWxfdGhlbWF0aWM&th=1"
headers = {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
"Accept-Encoding": "gzip, deflate, br, zstd",
"Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
"Priority": "u=0, i",
"Sec-Ch-Ua-Mobile": "?0",
"Sec-Ch-Ua-Platform": "Windows",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "none",
"Sec-Fetch-User": "?1",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
}

response = requests.get(url=URL, headers=headers)
print("status code:", response.status_code)
soup = BeautifulSoup(response.text, "html.parser")

target_price = 100000


def send_email():
    msg = EmailMessage()
    msg["Subject"] = "🔥 Price Drop Alert!"
    msg["From"] = MY_MAIL
    msg["To"] = MY_MAIL

    html_content = f"""
                <html>
                    <body>
                        <h2>Price Alert 🚀</h2>
                        <p><b>{title_element_value}</b></p>
                        <p>Now available at <b>₹{price_element_value}</b></p>
                        <p>
                            👉 <a href="{URL}">Click here to view product</a>
                        </p>
                    </body>
                </html>
"""
    msg.add_alternative(html_content, subtype="html")
    with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
        connection.starttls()
        connection.login(user=MY_MAIL, password=APP_PASSWORD)
        connection.send_message(msg)


price_element = soup.find(name="span", class_="a-price-whole")
price_element_value = float(price_element.getText().replace(",", ""))

title_element = soup.find(name="span", id="productTitle")
title_element_value = title_element.getText().split(",")[0]

if price_element_value < target_price:
    send_email()
    print("email sent!")
else:
    print("code compiled")

# print(item_price)
# print(soup)
