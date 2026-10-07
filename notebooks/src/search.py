

import ipywidgets as widgets
import requests
from bs4 import BeautifulSoup as bs4
import re

def web_scrape():
    w_url = widgets.Text(placeholder = "Copy and paste the url of the website", description = "URL",layout = {"width":"70%"})
    
    button = widgets.Button(description = "Submit",layout = {"width":"20%"})
    output = widgets.Output()
    
    def function(button):
        output.clear_output()
    
        with output:
            if w_url.value != "":
                url = str(w_url.value)
                response = requests.get(url)
                text = response.text
                html = bs4(text, 'html.parser')
                print(html)
                print(html.prettify())
        
    button.on_click(function)
    
    app = widgets.HBox(children = [w_url, button],layout = {"width":"100%"})
    display(app)
    display(output)
