import gcsconnect,db
# from DBcode import mongoDB
def preprocess(path,id):
    print("*****Process Initiated*****")
    print(id)
    #pageinfo=convert_pdf_to_image_split('Contract/Residential-Lease-Agreement-4/','Contract/Residential-Lease-Agreement-4.pdf')
    pageinfo=gcsconnect.convert_pdf_to_image_split(path,path.rstrip('.pdf')+'/')
    print(gcsconnect.ocr_maker(pageinfo))
    db.update_one(id,{"$set": {'queue':'Validation3','status':'Ready'}})
    print('updated')