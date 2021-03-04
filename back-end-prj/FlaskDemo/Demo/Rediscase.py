from flask import Flask

import redis

app = Flask(__name__)
# Check Configuring Flask-Cache section for more details
@app.route('/redis_insert',methods=['GET'])   
def redis_insert():
    pool = redis.ConnectionPool(host='10.122.27.44', port=6379)
    r = redis.Redis(connection_pool=pool)
    #r.set('name', 'wuqi22243',10)   #添加
    #r.set('name2', 'wuqi322222',10)
    print (r.get('name2'))   #获取
    #sismember(name, value)
    #检查value是否是name对应的集合内的元素
    return "success"+str(r.get('name2'))


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5001')
#     app.run(debug=True)