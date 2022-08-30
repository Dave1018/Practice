import oss2

auth = oss2.Auth("LTAI5t8ZTQeawbsiHn5G2CvV","qv2zWdWUT9XOXYPXWwMgc9a7KaXA6X")
endpoint = "oss-cn-hongkong.aliyuncs.com"
bucketName1 = "davetest1"
bucket = oss2.Bucket(auth, endpoint, bucketName1)


key   = "test.txt"
#key2 = "test2/"
#key3 = "test3/test.txt"

##新增檔案
##bucket.put_object(key,"test123")

##列出文件內容
##print(bucket.get_object(key).read())

##刪除文件
bucket.delete_object(key)


####列出bucket的檔案
for object_info in oss2.ObjectIterator(bucket):
    print(object_info.key)

