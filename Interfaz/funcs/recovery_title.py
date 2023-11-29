from mechanize import Browser
def recupera_title(url):
    br = Browser()
    br.set_handle_robots(False)
    br.open(url)
    title = br.title()
    return title
