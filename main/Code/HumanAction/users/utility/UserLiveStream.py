from django.conf import settings
import os
import time
class LiveStream:
    def startProcess(self):
        import numpy as np
        import imutils
        import sys
        import cv2

        CLASSES = open(os.path.join(settings.MEDIA_ROOT,'action_recognition_kinetics.txt')).read().strip().split("\n")
        SAMPLE_DURATION = 16
        SAMPLE_SIZE = 112

        # load the human activity recognition model
        print("[INFO] loading human activity recognition model...")
        net = cv2.dnn.readNet(os.path.join(settings.MEDIA_ROOT,'resnet-34_kinetics.onnx'))

        # grab a pointer to the input video stream
        print("[INFO] accessing video stream...")
        # vs = cv2.VideoCapture(args["input"] if args["input"] else 0)
        vs = cv2.VideoCapture(0)
        start_time = time.time()
        capture_duration = 20
        rslt = set()

        # loop until we explicitly break from it
        #while True:
        while(int(time.time() - start_time) < capture_duration):
            # initialize the batch of frames that will be passed through the
            # model
            frames = []

            # loop over the number of required sample frames
            for i in range(0, SAMPLE_DURATION):
                # read a frame from the video stream
                (grabbed, frame) = vs.read()

                # if the frame was not grabbed then we've reached the end of
                # the video stream so exit the script
                if not grabbed:
                    print("[INFO] no frame read from stream - exiting")
                    sys.exit(0)

                # otherwise, the frame was read so resize it and add it to
                # our frames list
                frame = imutils.resize(frame, width=400)
                frames.append(frame)

            # now that our frames array is filled we can construct our blob
            blob = cv2.dnn.blobFromImages(frames, 1.0,
                                          (SAMPLE_SIZE, SAMPLE_SIZE), (114.7748, 107.7354, 99.4750),
                                          swapRB=True, crop=True)
            blob = np.transpose(blob, (1, 0, 2, 3))
            blob = np.expand_dims(blob, axis=0)

            # pass the blob through the network to obtain our human activity
            # recognition predictions
            net.setInput(blob)
            outputs = net.forward()
            label = CLASSES[np.argmax(outputs)]

            # loop over our frames
            for frame in frames:
                # draw the predicted activity on the frame
                cv2.rectangle(frame, (0, 0), (300, 40), (0, 0, 0), -1)
                cv2.putText(frame, label, (10, 25), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (255, 255, 255), 2)
                rslt.add(label)
                # display the frame to our screen
                cv2.imshow("Action Recognition", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break


        vs.release()
        cv2.destroyAllWindows()
        return rslt
