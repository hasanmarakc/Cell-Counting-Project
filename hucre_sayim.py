import cv2

def hucre_say(img_path):
    image = cv2.imread(img_path)
    if image is None:
        raise ValueError("❌ Görüntü yüklenemedi! Dosya adı veya yolu hatalı.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    _, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    hücre_sayısı = 0
    for c in contours:
        if cv2.contourArea(c) > 0.5:
            hücre_sayısı += 1
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)

    return hücre_sayısı, image

if __name__ == "__main__":
    try:
        sayi, img = hucre_say("ornekler/hucre1.jpg")  
        print(f"🧬 Hücre sayısı: {sayi}")
        cv2.imshow("Sayım Sonucu", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print(e)
