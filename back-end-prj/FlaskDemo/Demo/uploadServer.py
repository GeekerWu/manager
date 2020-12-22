'''
Created on 2019-2-12

@author: wuqi2
'''
'''
Created on 2018-6-7

Key 'Excel'

@author: wuqi2
'''
from flask import Flask,request,jsonify
from flask_uploads import UploadSet,DOCUMENTS
#flaskext.uploads.DOCUMENTS
from flask_cors import CORS
import os
import time


Excels = UploadSet('Excel', DOCUMENTS)
app = Flask(__name__)

UPLOAD_FOLDER='upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # 设置文件上传的目标文件夹
basedir= os.path.abspath(os.path.dirname(__file__)) # 获取当前项目的绝对路径
#ALLOWED_EXTENSIONS = set(['txt', 'png', 'jpg', 'xls', 'JPG', 'PNG', 'xlsx', 'gif', 'GIF'])  # 允许上传的文件后缀
ALLOWED_EXTENSIONS = set(['jpg','xls','xlsx'])

# 判断文件是否合法
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

CORS(app)
@app.route('/upload',methods=['POST','GET'])   
def webServer():
    print (request.method)
    #页面测试
    if request.method =='GET':
        print ("GET Header info:")
        print (str(request.headers))
        print ("GET Body")
        data = request.get_data()
        print (data)
        print ("Post Values")
        print (request.values)
        print ("Post Form")
        print (request.form)
        print ("GET REQUEST") 
        resp = 'Upload Server Ready！' 
#         resp.headers['Access-Control-Allow-Origin'] = '*'   
        return resp
    #文件接收逻辑
    if request.method == 'POST':
        file_dir =os.path.join(basedir, app.config['UPLOAD_FOLDER'])  # 拼接成合法文件夹地址
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)  # 文件夹不存在就创建
#         f=request.files['Excel']  # 从表单的file字段获取文件，Excel为该表单的name值
        f=request.files['photo'] 
        if f and allowed_file(f.filename):  # 判断是否是允许上传的文件类型
            fname=f.filename
            ext = fname.rsplit('.', 1)[1]  # 获取文件后缀
            old_filename = fname.rsplit('.', 1)[0]  # 获取文件名
            time_stamp = str(time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()))
            new_filename = old_filename+' '+time_stamp+'.'+ext   # 修改文件名
            f.save(os.path.join(file_dir, new_filename))  #保存文件到upload目录
            return jsonify({"errno": 0, "errmsg": "上传成功"})
        else:
            return jsonify({"errno": 1001, "errmsg": "上传失败"})
        #rec = Excels(filename=filename)
         
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
#     app.run(debug=True)
    