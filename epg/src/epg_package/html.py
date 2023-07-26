# ideas from:

# https://github.com/Finn10111/tvh-auto-power/blob/master/tvh-auto-power.py

# https://github.com/dave-p/TVH-API-docs/wiki/

def wrap(tag,attr,content):
    return f'<{tag} {attr}>{content}</{tag}>'
    
def pwrap(tag,content):
    return f'<{tag}>{content}</{tag}>'
    
def html(head,body):
    return pwrap("html",head+body)
    
def head(title):
    style='*{box-sizing:border-box;margin:0}summary{overflow:hidden}'
    return pwrap('head',title+pwrap('style',style))
    
def body(content):
    return f'<body>{content}</body>'

def div(style,content):
    return f'<div style="{style}">{content}</div>'
    
def details(summary,text):
    return f'<details><summary>{summary}</summary>{text}</details>'
   
def flex(content):
    return div("display:flex;justify-content:center;",content)
