def recupera_url(valores):
    urls = []
    for i in valores:
        if type(i) != int:
            urls.append(i)
    return urls
