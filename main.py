import requests
from bs4 import BeautifulSoup
import json

# List of URLs and corresponding keys
url_key_pairs = [
    ("https://en.wikipedia.org/wiki/Copper", "Copper"),
    ("https://en.wikipedia.org/wiki/Aluminium", "Aluminium"),
    ("https://en.wikipedia.org/wiki/Gold", "Gold"),
    ("https://en.wikipedia.org/wiki/Iron", "Iron"),
    ("https://en.wikipedia.org/wiki/Silver", "Silver"),
    ("https://en.wikipedia.org/wiki/Zinc", "Zinc"),
    ("https://en.wikipedia.org/wiki/Titanium", "Titanium"),
    ("https://en.wikipedia.org/wiki/Magnesium", "Magnesium"),
    ("https://en.wikipedia.org/wiki/Platinum", "Platinum"),
    ("https://en.wikipedia.org/wiki/Nickel", "Nickel"),
    ("https://en.wikipedia.org/wiki/Cobalt", "Cobalt"),
    ("https://en.wikipedia.org/wiki/Tungsten", "Tungsten"),
    ("https://en.wikipedia.org/wiki/Lead", "Lead"),
    ("https://en.wikipedia.org/wiki/Chromium", "Chromium"),
    ("https://en.wikipedia.org/wiki/Zirconium", "Zirconium"),
    ("https://en.wikipedia.org/wiki/Vanadium", "Vanadium"),
    ("https://en.wikipedia.org/wiki/Manganese", "Manganese"),
    ("https://en.wikipedia.org/wiki/Scandium", "Scandium"),
    ("https://en.wikipedia.org/wiki/Rhodium", "Rhodium"),
    ("https://en.wikipedia.org/wiki/Germanium", "Germanium"),
    ("https://en.wikipedia.org/wiki/Cadmium", "Cadmium"),
    ("https://en.wikipedia.org/wiki/Hafnium", "Hafnium"),
    ("https://en.wikipedia.org/wiki/Indium", "Indium"),
    ("https://en.wikipedia.org/wiki/Palladium", "Palladium"),
    ("https://en.wikipedia.org/wiki/Tin", "Tin"),
    ("https://en.wikipedia.org/wiki/Bismuth", "Bismuth"),
    ("https://en.wikipedia.org/wiki/Antimony", "Antimony"),
    ("https://en.wikipedia.org/wiki/Cesium", "Cesium"),
    ("https://en.wikipedia.org/wiki/Gallium", "Gallium"),
    ("https://en.wikipedia.org/wiki/Lithium", "Lithium"),
    ("https://en.wikipedia.org/wiki/Thallium", "Thallium"),
    ("https://en.wikipedia.org/wiki/Rubidium", "Rubidium"),
    ("https://en.wikipedia.org/wiki/Calcium", "Calcium"),
    ("https://en.wikipedia.org/wiki/Sodium", "Sodium"),
    ("https://en.wikipedia.org/wiki/Potassium", "Potassium"),
    ("https://en.wikipedia.org/wiki/Beryllium", "Beryllium"),
    ("https://en.wikipedia.org/wiki/Yttrium", "Yttrium"),
    ("https://en.wikipedia.org/wiki/Strontium", "Strontium"),
    ("https://en.wikipedia.org/wiki/Barium", "Barium"),
    ("https://en.wikipedia.org/wiki/Calcium", "Calcium"),
    ("https://en.wikipedia.org/wiki/Zinc", "Zinc"),
    ("https://en.wikipedia.org/wiki/Platinum", "Platinum"),
    ("https://en.wikipedia.org/wiki/Thulium", "Thulium"),
    ("https://en.wikipedia.org/wiki/Terbium", "Terbium"),
    ("https://en.wikipedia.org/wiki/Ytterbium", "Ytterbium"),
    ("https://en.wikipedia.org/wiki/Erbium", "Erbium"),
    ("https://en.wikipedia.org/wiki/Holmium", "Holmium"),
    ("https://en.wikipedia.org/wiki/Dysprosium", "Dysprosium"),
    ("https://en.wikipedia.org/wiki/Gadolinium", "Gadolinium"),
    ("https://en.wikipedia.org/wiki/Europium", "Europium"),
    ("https://en.wikipedia.org/wiki/Samarium", "Samarium"),
    ("https://en.wikipedia.org/wiki/Neodymium", "Neodymium"),
    ("https://en.wikipedia.org/wiki/Praseodymium", "Praseodymium"),
    ("https://en.wikipedia.org/wiki/Cerium", "Cerium"),
    ("https://en.wikipedia.org/wiki/Lanthanum", "Lanthanum"),
    ("https://en.wikipedia.org/wiki/Actinium", "Actinium"),
    ("https://en.wikipedia.org/wiki/Thorium", "Thorium"),
    ("https://en.wikipedia.org/wiki/Protactinium", "Protactinium"),
    ("https://en.wikipedia.org/wiki/Uranium", "Uranium"),
    ("https://en.wikipedia.org/wiki/Plutonium", "Plutonium"),
    ("https://en.wikipedia.org/wiki/Neptunium", "Neptunium"),
    ("https://en.wikipedia.org/wiki/Americium", "Americium"),
    ("https://en.wikipedia.org/wiki/Curium", "Curium"),
    ("https://en.wikipedia.org/wiki/Berkelium", "Berkelium"),
    ("https://en.wikipedia.org/wiki/Californium", "Californium"),
    ("https://en.wikipedia.org/wiki/Einsteinium", "Einsteinium"),
    ("https://en.wikipedia.org/wiki/Fermium", "Fermium"),
    ("https://en.wikipedia.org/wiki/Mendelevium", "Mendelevium"),
    ("https://en.wikipedia.org/wiki/Nobelium", "Nobelium"),
    ("https://en.wikipedia.org/wiki/Lawrencium", "Lawrencium"),
    ("https://en.wikipedia.org/wiki/Rutherfordium", "Rutherfordium"),
    ("https://en.wikipedia.org/wiki/Dubnium", "Dubnium"),
    ("https://en.wikipedia.org/wiki/Seaborgium", "Seaborgium"),
    ("https://en.wikipedia.org/wiki/Bohrium", "Bohrium"),
    ("https://en.wikipedia.org/wiki/Hassium", "Hassium"),
    ("https://en.wikipedia.org/wiki/Meitnerium", "Meitnerium"),
    ("https://en.wikipedia.org/wiki/Darmstadtium", "Darmstadtium"),
    ("https://en.wikipedia.org/wiki/Roentgenium", "Roentgenium"),
    ("https://en.wikipedia.org/wiki/Copernicium", "Copernicium"),
    ("https://en.wikipedia.org/wiki/Nihonium", "Nihonium"),
    ("https://en.wikipedia.org/wiki/Flerovium", "Flerovium"),
    ("https://en.wikipedia.org/wiki/Moscovium", "Moscovium"),
    ("https://en.wikipedia.org/wiki/Livermorium", "Livermorium"),
    ("https://en.wikipedia.org/wiki/Tennessine", "Tennessine"),
    ("https://en.wikipedia.org/wiki/Oganesson", "Oganesson"),
    # Add more URL-key pairs for other crystalline metals
]


nested_data = {}
elements = []
for url, key in url_key_pairs:
    elements.append(key)
    # Make a GET request to the webpage
    response = requests.get(url)

    # Create a BeautifulSoup object with the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table with class name "infobox"
    table = soup.find('table', class_='infobox')

    # Process or extract information from the table as needed
    if table:
        data_dict = {}
        rows = table.find_all('tr')
        for row in rows:
            tm = row.find('td', class_='infobox-image')
            th = row.find('th', class_='infobox-label')
            td = row.find('td', class_='infobox-data')
            print(tm)
            # Check if the row contains the desired td class "infobox-image"
            if tm:
                print("Image")
                tm_image = tm.find('a', class_='image')
                print("tm img")
                print(tm_image)
                img_tag = tm_image.find('img')
                if img_tag:
                    image_src = img_tag['src']
                    print(image_src)
                else:
                    print("Image source not found.")
                print(image_src)
                data_dict['image_link'] = "https:" + image_src

            # Check if the row contains th and td elements
            elif th and td:
                data_dict[th.text.strip()] = td.text.strip().replace(u'\xa0', ' ')

        # Add the data dictionary to the nested structure with the corresponding key
        nested_data[key] = data_dict
    else:
        print(f"Table with class 'infobox' not found for {key}.")
nested_data['Elements'] = elements
# Serialize the nested data structure to JSON with indentation
json_output = json.dumps(nested_data, ensure_ascii=False, indent=4)

# Save the resulting JSON
with open('nested_data.json', 'w', encoding='utf-8') as file:
    file.write(json_output)

print("Nested JSON created and saved as 'nested_data.json'")
