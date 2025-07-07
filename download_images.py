from icrawler.builtin import GoogleImageCrawler
import os

diseases = [
    "allergy", "bleeding", "cold", "diarrhea", "ear infection", "fever",
    "fracture", "infection", "limping", "mange", "normal", "parvo", "rabies",
    "tick", "tumor", "vomiting", "wound"
]

for category in diseases:
    for split in ["train", "val"]:
        save_dir = f"dataset/{split}/{category}"
        os.makedirs(save_dir, exist_ok=True)

        crawler = GoogleImageCrawler(storage={"root_dir": save_dir})
        crawler.crawl(keyword=f"{category} in dogs", max_num=20 if split == "val" else 50)

print("✅ Image download complete.")
