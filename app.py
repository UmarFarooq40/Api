from flask import Flask,request


app=Flask(__name__)



items=[
    {
        'name':'Mojito',
        'price':160
    },
    {
        'name':'Momos',
        'price':200
    },
    {
        'name':'biscuits',
        'price':90
    },
    {
        'name':'Pizza',
        'price':400
    },
    {
        'name':'Cake',
        'price':700
    },
    {
        'name':'Milkshake',
        'price':70
    }
]

@app.route('/')
def home():
      return {'items':items}


@app.get('/getitems')
def get_items():
    return {'items':items}

@app.get('/getitem')
def getitem():
    name=request.args.get('name')
    for item in items:
        if name==item['name']:
            return item
    return {'messege':'Item Not found'},404

@app.post('/additem')
def additem():
    request_item = request.get_json()
    items.append(request_item)
    return {"messege":"Item was added successfully"},201



@app.put('/updateitem')
def updateitem():
    request_data=request.get_json()
    for item in items:
        if item['name']== request_data['name']:
            item['price']=request_data['price']
            return {"messege":"item updated succesfully"}
        
    return {"messege":"Given record doesnot exist"},404



@app.delete('/deleteitem')
def delete_item():
    name=request.args.get('name')
    for item in items:
        if name ==item['name']:
            items.remove(item)
            return {"messege":"item deleted successfully"}
    return {"messege":"Item not found"},404


if __name__=='__main__':
    app.run(debug=True)