import cv2
import pickle

width, height = 115, 55

try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
        posList1 = pickle.load(f)

except:
    posList = []
    posList1 = []



def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        posList1.append((x, y))
    if events == cv2.EVENT_MBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)
    if events == cv2.EVENT_MBUTTONDOWN:
        for i, pos in enumerate(posList1):
            x1, y1 = pos
            if x1 < x < x1 + height and y1 < y < y1 + width:
                posList1.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)
        pickle.dump(posList1, f)




while True:
    img = cv2.imread('CarParkImg.png')
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)
    for pos in posList1:
        cv2.rectangle(img, pos, (pos[0] + height, pos[1] + width), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)

    k = cv2.waitKey(1) & 0xFF  # Capture the code of the pressed key.
    # Stop the loop when the user clicks on GUI close button [x].
    if not cv2.getWindowProperty("Image", cv2.WND_PROP_VISIBLE):
        print("Operation Cancelled")
        break
    if k == 27:  # Key code for ESC
        break
