import os

import cv2

def generate_out_video():
    ''' generating video from Images '''

    try:
        image_folder = 'Store/'
        video_name = 'Output_Video.avi'

        images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
        images = sort_(images)

        frame = cv2.imread(os.path.join(image_folder, images[0]))
        height, width, layers = frame.shape

        video = cv2.VideoWriter(video_name, 0, 1, (width,height))

        for image in images:
            video.write(cv2.imread(os.path.join(image_folder, image)))

        cv2.destroyAllWindows()
        video.release()
    except:
        pass


def sort_(images):
  ss = {}
  for img in images:
    img1 = int(img.split('.')[0].split('w')[1])
    ss[img1] = img

  ll = []
  for i in sorted (ss.keys()):
    ll.append(ss[i])

  return ll
