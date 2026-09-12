import re
def extract(text:str):
    email=re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+',text)
    amounts=re.findall(r'\$\s?([0-9]+(?:\.[0-9]{2})?)',text)
    return {'email':email.group(0) if email else None,'amounts':[float(x) for x in amounts],'word_count':len(text.split())}
