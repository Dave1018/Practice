import oss2

auth = oss2.Auth("AccessKeyId","AccessKeySecret")
endpoint = "oss-cn-hongkong.aliyuncs.com"
bucketName = "davetest1"
bucket = oss2.Bucket(auth, endpoint, bucketName)

key   = "test.txt"          #bucket的文件名稱
#key2 = "test2/"            #以/結尾為資料夾
#key3 = "test3/test.txt"    #新增資料夾並在該資料夾下新增文件

##新增檔案
##bucket.put_object(key,"test123")

##列出文件內容
##print(bucket.get_object(key).read())

##刪除文件
#bucket.delete_object(key)

####列出bucket的檔案
#for object_info in oss2.ObjectIterator(bucket):
#    print(object_info.key)

