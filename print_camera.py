import xml.etree.ElementTree as ET  
class print_camera():
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
    print('%-6s%-55s%-35s%-20s%-8s%15s'%(productDT_d[0],productDT_d[1],productDT_d[2],productDT_d[3],productDT_d[5],productDT_d[4]))
     
    for e in productDL_d:
    
        print('%-6s%-55s%-35s%-20s%-8i%15.2f'%(e['Code'],e['Product name'],e['Brand'],e['Category'],e['Stock'],e['Price(HKD)'])) 
