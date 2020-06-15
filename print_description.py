import xml.etree.ElementTree as ET 
class print_description(): 
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
    print('%-6s%-55s'%(productDT_d[0],productDT_d[1]))
     
    for e in productDL_d:
    
        print('%-6s%-55s'%(e['Code'],e['description'])) 
