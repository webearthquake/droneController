from djitellopy import Tello
import cv2

tello = Tello()
tello.connect()

tello.takeoff()
tello.move_up(100)
#start forever loop
while True:
    keypress = cv2.waitKey(0.5) & 0xff
    #if esc key pressed, stop forever loop
    if keypress == 27:
        break
    #WASD movement controls
    elif keypress == ord('w'):
        tello.move_forward(25)
    elif keypress == ord('a'):
        tello.move_left(25)
    elif keypress == ord('s'):
        tello.move_back(25)
    elif keypress == ord('d'):
        tello.move_right(25)
        #E and Q to rotate drone
    elif keypress == ord('q'):
        tello.rotate_counter_clockwise(15)
    elif keypress == ord('e'):
        tello.rotate_clockwise(15)
#land when loop broken
tello.land()
