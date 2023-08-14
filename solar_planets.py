import cv2

img = cv2.imread("Projects/Project-104/solar-system.jpg")
cv2.putText(    img,
                "<- Sun",
                (100,350),
                cv2.FONT_HERSHEY_COMPLEX,
                1.5,
                (0, 0, 225)   )

cv2.putText(    img,
                "Mercury",
                (110,250),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)   )

cv2.putText(    img,
                "Venus",
                (190,260),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)   )

cv2.putText(    img,
                "Earth",
                (280,265),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)   )

cv2.putText(    img,
                "Moon",
                (300,150),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)   )

cv2.putText(    img,
                "Mars",
                (380,250),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)   )

cv2.putText(    img,
                "Jupiter",
                (560,380),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)   )

cv2.putText(    img,
                "Saturn",
                (760,300),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)   )

cv2.putText(    img,
                "Uranus",
                (960,300),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)   )

cv2.putText(    img,
                "Neptune",
                (1120,300),
                cv2.FONT_HERSHEY_COMPLEX,
                0.5,
                (255,255,255)   )

cv2.putText(    img,
                "> The Solar System <",
                (680,400),
                cv2.FONT_HERSHEY_COMPLEX,
                1.5,
                (0,255,255)   )

cv2.imshow("Solar System",img)
cv2.waitKey(0)
cv2.imwrite("Projects/Project-104/Solar_system.jpg",img)