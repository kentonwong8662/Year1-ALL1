import xml.etree.ElementTree as ET  
tree = ET.parse('SOLD.xml')  
root = tree.getroot()
code=[]
name=[]
brand=[]
price=[]
x=1 
y=1 
productDT_s=['Code','Product name','Brand','Price(HKD)']
productDL_s=[]
    
for elem in root: 
    y=1 
    for subelem in elem:
        if y==1:
            code.append(subelem.text)
            
        elif y==2:
            name.append(subelem.text)
            
        elif y==3:
            brand.append(subelem.text)
                        
        elif y==4:
            price.append(subelem.text)
            
        
        y=y+1
        
i=0
while i< len(code) :
    productDL_s.append(dict(zip(productDT_s,[code[i],name[i],brand[i],float(price[i])])))
    i=i+1
for e in productDL_s:
    
    print('%-6s%-55s%-35s%15.2f'%(e['Code'],e['Product name'],e['Brand'],e['Price(HKD)']))