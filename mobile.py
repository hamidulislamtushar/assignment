mobile_data = \
    {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

for mobile in mobile_data.get("data"):
    mobile_name = mobile.get("name")
    mobile_price = mobile.get("price")
    # convert into integer
    int_mobile_p = mobile_price.split(" ")
    int_mp = float(int_mobile_p[0])
    convert_bdt = round(int_mp * 103.25)

    mobile_origin = mobile.get("made")
    sentence = f"{mobile_name}  is made in {mobile_origin}. The price is {mobile_price} USD which is almost equal to {convert_bdt} BDT"
    print(sentence)

