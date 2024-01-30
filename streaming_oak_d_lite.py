import cv2
import depthai as dai

def generate():
    pipeline = dai.Pipeline()

    # Create the ColorCamera node and set its properties
    camRgb = pipeline.create(dai.node.ColorCamera)
    camRgb.setBoardSocket(dai.CameraBoardSocket.CAM_A)
    camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)

    # Create the XLinkOut node for the video stream and set its properties
    xoutRgb = pipeline.create(dai.node.XLinkOut)
    xoutRgb.setStreamName("My first stream")

    # Link the ColorCamera to the XLinkOut node
    camRgb.video.link(xoutRgb.input)

    # Start the pipeline
    with dai.Device(pipeline) as device:
        video_queue = device.getOutputQueue(name="My first stream", maxSize=4, blocking=False) # get the video stream queue
        
        while True:
            frame = video_queue.get().getCvFrame() # get the video frame as a numpy array
            (flag, encodedImage) = cv2.imencode(".jpg", frame) # then encode the frame into a jpg image

            # if the frame was not successfully encoded, then skip this iteration
            if not flag:
                continue

            #otherwise, yield the output frame in the byte format.
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
