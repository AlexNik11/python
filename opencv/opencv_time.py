import cv2
import time
import matplotlib.pyplot as plt

def lineplot(x_data, y_data, title, x_label="Время обработки", y_label="Кадры"):
    # Create the plot object
    _, ax = plt.subplots()

    # Plot the best fit line, set the linewidth (lw), color and
    # transparency (alpha) of the line
    ax.plot(x_data, y_data, lw = 2, color = '#539caf', alpha = 1)

    # Label the axes and provide a title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


def main():
    cap=cv2.VideoCapture(0)
    full_img_to_gray=0
    full_detection=0
    ImageConvPlot=[]
    ObjDetectPlot=[]
    Cadrs=100
    
    print(f'========\tSTARTING SCORE TEST OF VIOLA-JONES ALGORITM OF OBJECT DETECTION\t========\n')
    print(cv2.getBuildInformation())

    clf = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    #clf = cv2.CascadeClassifier('/usr/local/share/opencv4/haarcascades/' + 'haarcascade_frontalface_default.xml')
    #f1 = open('Image converting.txt', 'w')
    #f2 = open('Object detection.txt', 'w')

    for i in range(Cadrs):
        ret, frame=cap.read()
        start_t = time.perf_counter()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        end_t = time.perf_counter()
        img_to_gray = end_t - start_t
        full_img_to_gray+=img_to_gray

        start_t = time.perf_counter()
        clf.detectMultiScale(gray, 1.3, 125)
        end_t = time.perf_counter()
        detection = end_t - start_t
        full_detection+=detection
        
        print(f'Time has passed:\t{img_to_gray + detection}\t\n')
        print(f'Image converting:\t{img_to_gray}')
        ImageConvPlot.append(img_to_gray)
        #f1.writelines(str(img_to_gray)+"\n")
        print(f'Object detection:\t{detection}')
        ObjDetectPlot.append(detection)
        #f2.writelines(str(detection)+"\n")
        print ("Frame default resolution: " + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + "; " + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        

    #f1.close()
    #f2.close()
    print(f'\nFull time has passed:\t{full_img_to_gray + full_detection}\t')
    print(f'Full image converting:\t{full_img_to_gray}')
    print(f'Full object detection:\t{full_detection}')
    time.sleep(3)
    lineplot(range(1,Cadrs+1), ImageConvPlot, "Конвертация изображения")
    lineplot(range(1,Cadrs+1), ObjDetectPlot, "Поиск объекта")
    
    return 0

if __name__ == '__main__':
    main()
