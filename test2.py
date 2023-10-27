import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

with mp_pose.Pose(static_image_mode = True) as pose:
    image = cv2.imread("Imagen3.jpg")
    height, width, _ = image.shape
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)
    print("pose landmarks: ", results.pose_landmarks)

    if results.pose_landmarks is not None:
        print(int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width ))
        x1 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER].x * width )
        y1 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER].y * height)

        x2 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_ELBOW].x * width )
        y2 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_ELBOW].y * height)

        x3 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_WRIST].x * width )
        y3 = int(results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_WRIST].y * height)

        x4 = int(results.pose_landmarks.landmark[11].x * width )
        y4 = int(results.pose_landmarks.landmark[11].y * height)

        x5 = int(results.pose_landmarks.landmark[13].x * width )
        y5 = int(results.pose_landmarks.landmark[13].y * height)

        x6 = int(results.pose_landmarks.landmark[15].x * width )
        y6 = int(results.pose_landmarks.landmark[15].y * height)

        x7 = int(results.pose_landmarks.landmark[10].x * width )
        y7 = int(results.pose_landmarks.landmark[10].y * height)

        x8 = int(results.pose_landmarks.landmark[9].x * width )
        y8 = int(results.pose_landmarks.landmark[9].y * height)

        x9 = int(results.pose_landmarks.landmark[6].x * width )
        y9 = int(results.pose_landmarks.landmark[6].y * height)

        x10 = int(results.pose_landmarks.landmark[5].x * width )
        y10 = int(results.pose_landmarks.landmark[5].y * height)

        x11 = int(results.pose_landmarks.landmark[4].x * width )
        y11 = int(results.pose_landmarks.landmark[4].y * height)

        x12 = int(results.pose_landmarks.landmark[1].x * width )
        y12 = int(results.pose_landmarks.landmark[1].y * height)

        x13 = int(results.pose_landmarks.landmark[2].x * width )
        y13 = int(results.pose_landmarks.landmark[2].y * height)

        x14 = int(results.pose_landmarks.landmark[3].x * width )
        y14 = int(results.pose_landmarks.landmark[3].y * height)


        cv2.line(image, (x1, y1), (x2,y2), (255,255,255), 3)
        cv2.line(image, (x2,y2), (x3,y3), (255,255,255), 3)
        cv2.circle(image, (x1,y1), 8, (128, 0, 255), -1)
        cv2.circle(image, (x2,y2), 8, (128, 0, 255), -1)
        cv2.circle(image, (x3,y3), 8, (128, 0, 255), -1)
        
        cv2.line(image, (x1,y1), (x4,y4), (255,255,255), 3)
        cv2.line(image, (x4, y4), (x5,y5), (255,255,255), 3)
        cv2.line(image, (x5,y5), (x6,y6), (255,255,255), 3)
        cv2.circle(image, (x4,y4), 8, (255, 191,0), -1)
        cv2.circle(image, (x5,y5), 8, (255, 191,0), -1)
        cv2.circle(image, (x6,y6), 8, (255, 191,0), -1)

        cv2.line(image, (x7,y7), (x8,y8), (255,255,255), 3)
        cv2.circle(image, (x7,y7), 6, (255, 191,0), -1)
        cv2.circle(image, (x8,y8), 6, (255, 191,0), -1)

        cv2.line(image, (x9,y9), (x10,y10), (255,255,255), 1)
        cv2.line(image, (x10,y10), (x11,y11), (255,255,255), 1)
        cv2.circle(image, (x9,y9), 6, (255, 191,188), -1)
        cv2.circle(image, (x10,y10), 6, (255, 191,188), -1)
        cv2.circle(image, (x11,y11), 6, (255, 191,188), -1)

        cv2.line(image, (x12,y12), (x13,y13), (255,255,255), 1)
        cv2.line(image, (x13,y13), (x14,y14), (255,255,255), 1)
        cv2.circle(image, (x12,y12), 6, (255, 191,188), -1)
        cv2.circle(image, (x13,y13), 6, (255, 191,188), -1)
        cv2.circle(image, (x14,y14), 6, (255, 191,188), -1)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
cv2.destroyAllWindows()