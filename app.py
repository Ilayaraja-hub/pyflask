from flask import Flask, render_template, url_for, request, redirect
from werkzeug.utils import secure_filename
from datetime import date, datetime
from multiprocessing import Process
from flask_pymongo import pymongo
#from flask_cors import CORS,cross_origin
import db,gcsconnect
import io

app = Flask(__name__)
#cors=CORS(app,resources={r'*':{"origins":"*"}})

current_time= datetime.now()

@app.route("/", methods=["GET","POST","PUT"])
def home():
    if request.method == "POST":
        file = request.files['file_upload']
        # file.save(f"./upload_files/{secure_filename(file.filename)}")
        file_obj= io.BytesIO()
        file.save(file_obj)
        file_obj.seek(0)
        gcsconnect.write_file("Contract/"+file.filename,file_obj.read())
        path="Contract/"+file.filename
        print(path)
        print("POST")

        id=db.insert_one({"name":secure_filename(file.filename),"upload_date":datetime.now().strftime(("%d/%m/%Y %H:%M:%S")),"queue":"Scan","status":"On Queue","doc_type":"Lease Agreement"}).inserted_id
        print("mongoObj_id",id)
        import pre_process 
        
        p=Process(target=pre_process.preprocess,args=(path,id,))
        p.start()
        return redirect("/")



        # db.collection_table.insert_one(
        #     {"name":secure_filename(file.filename),
        #     "Date":current_time
        #     })
        # print("POST")
        # return redirect("/")
    else:
        return render_template('home.html')
    return render_template('home.html')

# GEnerating Signed URL 

@app.route("/getSignedurl")
def getSignedurl():
    bucket=storage_client.bucket(bucket_name)
    filename=request.args.get('filename')
    action = request.args.get('action')
    print(filename,action)
    blob=bucket.blob(filename)
    url=blob.generate_signed_url(
        expiration=datetime.timedelta(minutes=2),
        method=action,
        version='v4'
    )
    return url


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@app.route("/test")
def test():
    
    table_data=db.collection_table.find_one() #Here collection is the subset of db..it can be of an name.

    return table_data
    


if __name__ == "__main__":
    app.debug = True
    app.run(host= "0.0.0.0", port = 5000)