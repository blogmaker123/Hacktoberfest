#two ways to download Instagram profile picture of any instagram user (Works even if your blocked by that instagram user)

USER_ID = input("Enter USer_id of any instagram user : ")
try:#first way mentioned in try block 
    import requests
    import json
    import shutil

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    }

    INSTA_URL = "https://www.instagram.com/"
    
    TAIL = "/?__a=1"
    URL = INSTA_URL + USER_ID + TAIL
    response = requests.get(url=URL,headers=header).json()
    hd_image_location = response["graphql"]["user"]["profile_pic_url_hd"]
    hd_image_response = requests.get(hd_image_location, stream=True)
    with open("hd_img.jpg", "wb") as out_file:
        shutil.copyfileobj(hd_image_response.raw, out_file)
        
except :# Second way mentioned in Except block 
    import instaloader
    mod=instaloader.Instaloader()
    mod.download_profile(USER_ID,profile_pic_only=True)
   
