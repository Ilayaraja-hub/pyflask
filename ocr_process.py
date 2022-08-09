import gcsconnect,db

def ocr_maker(child):
    while 1:
        msg=child.recv()
        if msg=="END":
            break
        
        
    print(gcsconnect.ocr_maker(pageinfo))
    db.update_one(id,{"$set": {'queue':'Validation3','status':'Ready'}})
    print('updated')