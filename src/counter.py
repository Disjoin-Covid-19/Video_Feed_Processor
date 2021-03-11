

import tensorflow
from src.Utilities.DB import my_collection
from imageai.Detection import ObjectDetection
import os
import cv2
from datetime import datetime, date, time, timedelta

#from src.Utilities.helpers import generate_out_video



class disjoin_counter:

    def __init__(self, Pass, recording_path):

        #intilizing the fundamental veriable
        self.recording_path = recording_path

        self.Pass = Pass

        self.my_col = None


    def connect(self):

        self.my_col = my_collection(self.Pass)

        if self.my_col == -1:
            print("Please enter a valid access key !")
            exit()

        print(" Disjoin counter started successfully!")

    def get_detector(self):

        # starting ObjectDetection module
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsRetinaNet()
        self.detector.setModelPath('Model/resnet50_coco_best_v2.1.0.h5')
        self.detector.loadModel()






    def start(self,store_output_video = False):

        self.connect()

        self.get_detector()


        # starting the video capture activity

        vid = cv2.VideoCapture('input_video.mp4')#str(self.recording_path))


        i = 0
        j = 10


        while(vid.isOpened()):

            ret, frame = vid.read()

            if ret == True:

                if(j%10 == 0):# taking every 10th frame

                  t = datetime.now()
                  t =  t +  timedelta(seconds=1)

                  custom = self.detector.CustomObjects(person=True)



                  returned_image, detections  = self.detector.detectCustomObjectsFromImage(
                                                    custom_objects=custom,
                                                    input_image= frame ,
                                                    output_type="array",
                                                    minimum_percentage_probability=30,
                                                    input_type ="array")


                  out_img = "Store/"+  "imagenew"+str(i)+".jpg"

                  if store_output_video:
                      cv2.imwrite(out_img, returned_image)


                  cv2.imshow('F',returned_image)

                  i+=1

                  count = len(detections)
                  d = t.strftime("%m/%d/%Y, %H:%M:%S")

                  mydict = { "_id": i ,"count": count, "Date_time": d }

                  x = self.my_col.insert_one(mydict) # inserting into database


                  if cv2.waitKey(25) & 0xFF == ord('q'):
                      break
                j+=1
            else:

                break

        vid.release()
        #out.release()

        cv2.destroyAllWindows()

        # if store_output_video:
        #     generate_out_video()
