import sensuspy as sp

print("Before reading files from aws")
s3_bucket_path = "s3://team5-4be5ce38-fa05-41ae-ad04-429dfd3d4cc5/data/GPS"
#  s3_bucket_path = "s3://sensus3-8ed2ecc1-d86e-4430-9ba7-50e72f10a284/data/proj_6160/"
sp.sync_from_aws(s3_bucket_path, "E:/MS_studyProcess/UNCC-Study/spring-2020/6160-BigDataDesign/Challenge-2/GPS", aws_client_path = "\"c:/Program Files/Amazon/AWSCLIV2/aws\"")

print("After reading files from aws :: ",s3_bucket_path)   
#If you are using a mac or a unix based machine, you can find the path of your aws client by running the command "which aws" on the terminal
#A similar command exists for windows, just google it

data = sp.read_json("E:/MS_studyProcess/UNCC-Study/spring-2020/6160-BigDataDesign/Challenge-2/GPS")

print("Data to be passed to function is :: \n ", data)

#Serialize the data in case you have to load it again, this makes the process much faster
sp.write_pickle(data, "E:/MS_studyProcess/UNCC-Study/spring-2020/6160-BigDataDesign/Challenge-2/GPSPickled")
#You can then do data = sp.read_pickle("E:/MS_studyProcess/UNCC-Study/spring-2020/6160-BigDataDesign/Challenge-2/GPSPickled")	and get the same data structure 

data = sp.drop_duplicates_from_data(data)
accelerometer_datum = data['AccelerometerDatum']

lags = sp.get_all_timestamp_lags(data)
accelerometer_datum_lags = lags['AccelerometerDatum']
#alteratively, accelerometer_datum_lags = sp.get_timestamp_lags(accelerometer_datum)

sp.plot_datum_lags(accelerometer_datum_lags)