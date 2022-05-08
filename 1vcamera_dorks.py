# This is Camera Dorks for your default browser by 1vere$k.
# In the future I plan to support multiple browsers + TOR for user's anonymization
# Example#1: python3 1vcamera_dorks.py <camera_manufacturer> [OPTIONAL] <region of search>
# Example#2: python3 1vcamera_dorks.py - quick dork option.
# Camera Manufacturer will stick to default Other option.
# ------------------------------------------------------------------------------------
# Important! JSON file should be crafted with attribute 'first_tab' in a case of multiple values for dorks.
# Example:
# "Sony" : {
#     "first_tab": "intitle:”sony network camera snc-p",
#     "second_tab": "intitle:sony network camera snc-m1"
#   }


import json
import sys
import webbrowser

if __name__ == "__main__":
    # Greetings from 1vere$k. This is a simple Google Dorks demonstration.
    # It will auto open a known cameras dorks in your default browser.
    # In the future I plan to support multiple browsers + TOR for user's anonymization
    print("This is Camera Dorks for Chromium browser by 1vere$k.\n")

    # I am assuming that region will be mentioned by default.
    is_region = True

    # Setting up basic variables to exclude some logic faults.
    camera_name = ""
    region = ""

    # Checking if camera manufacturer is in the parameters plus printing small instructions.
    try:
        camera_name = sys.argv[1]
    except:
        camera_name = "--help"

    if camera_name == "-h" or camera_name == "--help":
        print("Example#1: python3 1vcamera_dorks.py <camera_manufacturer> [OPTIONAL] <region of search>\n")
        print("Region is optional. In the future I plan to add a search by GEO location.\n")
        print("Important! JSON file should be crafted with attribute 'first_tab' in a case of multiple values for dorks.\n")
        print("Example:\n")
        print("'Sony' : {\n")
        print(" 'first_tab': 'intitle:'sony network camera snc-p',\n")
        print(" 'second_tab': 'intitle:'sony network camera snc-mq',\n" + "}\n")
        exit(0)

    # Checking if region was specified in the command line.
    try:
        region = " loc:'" + sys.argv[2] + "'"
    except:
        is_region = False

    # Opening JSON file. Checking if it's exists and has the right format.
    f = open("dorks.json", 'r')
    if not f:
        print("\n Please make sure dorks.json is present and formatted as JSON correctly.")
        exit(0)
    dorks_json = json.load(f)

    # Working with browser block.
    # Basic google search link.
    search_url = 'https://www.google.com/search?q='
    try:
        dorks = dorks_json[camera_name]

        # Checking are there multiple dorks for the camera manufacturer.
        if 'first_tab' in dorks:
            # Multiple dorks case.
            for key, value in dorks.items():
                if is_region:
                    webbrowser.open_new_tab(search_url + str(value) + region)
                else:
                    webbrowser.open_new_tab(search_url + str(value))
        else:
            # One dork case.
            if is_region:
                webbrowser.open_new_tab(search_url + str(dorks) + region)
            else:
                webbrowser.open_new_tab(search_url + str(dorks))
    except KeyError:
        print(str(KeyError.__traceback__) + "\nCheck please if these Camera Manufacturer does exist.")
        print("\nWe don't have it in our JSON")
        webbrowser.open_new_tab(search_url)
