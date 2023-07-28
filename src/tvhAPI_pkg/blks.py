from .html import div,details

def style(w,c):
    return f'width:{w}px;background-color:{c};border:1px solid black;padding:3px;'

def blk(item,dt):
    gc={16:'lightyellow',32:'lightsteelblue',48:'lightsalmon',64:'lavender',80:'lightgreen',96:'lightpink',112:'gainsboro',128:'cornsilk',144:'cadetblue',160:'bisque'}
    w=round(dt/18)
    if not 'genre' in item.keys():
        c='coral'
    else:
        c=gc[item['genre'][0]]
    if 'subtitle' in item.keys():
        return div(style(w,c),details(item["title"],item['subtitle']))
    return div(style(w,c),details(item["title"],''))

def chblk(name):
    return div(style(125,'lightgray'),name)
