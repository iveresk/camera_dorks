# Camera Dorks by 1vere$k
This is Camera Dorks for your default browser by 1vere$k.  
In the future I plan to support multiple browsers + TOR for user's anonymization.

# Usage
Example#1: `python3 1vcamera_dorks.py <camera_manufacturer> [OPTIONAL] <region of search>`.
Region is optional. In the future I plan to add a search by GEO location.  
With a quick launch like `python3 1vcamera_dorks.py` - you'll see a `--help or -h` variant.  
Small set of instructions, the same as in the README.md.

**Important!**  
JSON file should be crafted with attribute 'first_tab' in a case of multiple values for dorks.  
Example:
```
"Sony" : {
    "first_tab": "intitle:”sony network camera snc-p",
    "second_tab": "intitle:sony network camera snc-m1"
}
```