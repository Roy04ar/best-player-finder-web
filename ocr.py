import easyocr, os, cv2

def extract_jersey_numbers(frame_dir="temp/frames"):
    reader = easyocr.Reader(['en'])
    jersey_counts = {}
    for img_file in os.listdir(frame_dir):
        img = cv2.imread(os.path.join(frame_dir, img_file))
        results = reader.readtext(img)
        for (bbox, text, conf) in results:
            if text.strip().isdigit() and len(text.strip()) <= 2:
                num = text.strip()
                jersey_counts[num] = jersey_counts.get(num, 0) + 1
    return jersey_counts