from docxtpl import DocxTemplate
import os


f=open('billing.txt', 'r', encoding='utf-8')
a=f.readlines()
price=float(a[-1].split()[0])


f=open('output.txt', 'r', encoding='utf-8')
a=f.readlines()
price+=float(a[-1].split()[0])

nds=round(price*0.13,2)
templates=[]

doc = DocxTemplate("template.docx")
context = {'service':"Звонки, Смс, Интернет", 'number':"1",'ed':' ','price_ed':'1','price':price, 'nds':nds}
doc.render(context)
doc.save("final_doc.docx")


os.system('abiword --to=pdf final_doc.docx 2>/dev/null')
os.system('final_doc.docx')
