import cv2 as cv


class ImageProcessing():
    
    def __init__(self, path):
        self.path = path
        # self.name = self.resizing()
        

    
    def get_frame(self):
        img = cv.imread(self.path)
        return img

    def resizing(self):
        img = self.get_frame()
        img = cv.resize(img,(500,500))
        return img 
    
    def color_cvt(self, img):
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        return img
    
    def cvt_rez(self):
        img = self.resizing()
        img = self.color_cvt(img)
        return img
        

def main():
    path = "./1.png"
    k = ImageProcessing(path).cvt_rez()

    cv.imshow("Result", k)
    cv.waitKey(0)

if __name__ == "__main__":
    main()
    cv.destroyAllWindows()
