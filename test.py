
import csv,math

#业务方配置好的数据
file_to_read=open('c:\\Users\\btr\\Desktop\\sql_export.csv','r',newline='')
reader=csv.reader(file_to_read)
#要保存的数据
file_to_write=open('c:\\Users\\btr\\Desktop\\aa.csv','w',newline='',encoding='utf-8')
writer=csv.writer(file_to_write)




for i in reader:
    if(i[0]=='id'):
        continue
    hugePartsFreight=i[1]
    bigPartsFreight=i[2]
    mediumPartsFreight=i[3]
    smallPartsFreight=i[4]
    writer.writerow(['update tms_area_freight  set hugePartsFreight='+hugePartsFreight+',bigPartsFreight='+bigPartsFreight +',mediumPartsFreight='+mediumPartsFreight +',smallPartsFreight='+smallPartsFreight +' where areaFreightId='+i[0]+' ;'])

file_to_read.close()
file_to_write.close()
print("数据处理完成 ")


