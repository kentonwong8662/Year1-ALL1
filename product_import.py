
import xml.etree.ElementTree as ET  


class __camera__():
    tree = ET.parse('Camera.xml')  
    root = tree.getroot()
    code=[]
    name=[]
    brand=[]
    category=[]
    price=[]
    stock=[]

    x=1 
    y=1  
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
                category.append(subelem.text)
            
            elif y==5:
                price.append(subelem.text)
            
            elif y==6:
                stock.append(subelem.text)    
        
            y=y+1
            
    productDT_d=['Code','Product name','Brand','Category','Price(HKD)','Stock']
    productDL_d=[]



    i=0
    while i< len(code) :
        productDL_d.append(dict(zip(productDT_d,[code[i],name[i],brand[i],category[i],float(price[i]),int(stock[i])])))
    
    
        i=i+1

class __phone__():
    tree = ET.parse('Phone.xml')  
    root = tree.getroot()
    code=[]
    name=[]
    brand=[]
    price=[]
    x=1 
    y=1  
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
            
    productDT_d=['Code','Product name','Brand','Price(HKD)']
    productDL_d=[]



    i=0
    while i< len(code) :
        productDL_d.append(dict(zip(productDT_d,[code[i],name[i],brand[i],float(price[i])])))
    
    
        i=i+1

class __description__():
    tree = ET.parse('camera description.xml')  
    root = tree.getroot()
    code=[]
    description=[]
    x=1 
    y=1  
    for elem in root: 
        y=1 
        for subelem in elem:
            if y==1:
                code.append(subelem.text)
            
            elif y==2:
                description.append(subelem.text)
            
            y=y+1
            
    productDT_d=['Code','description']
    productDL_d=[]



    i=0
    while i< len(code) :
        productDL_d.append(dict(zip(productDT_d,[code[i],description[i]])))
    
    
        i=i+1
