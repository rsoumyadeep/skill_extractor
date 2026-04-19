import os

from skill_extractor.config import SKILLS
from skill_extractor.preprocess import preprocess
from skill_extractor.extractor import extract_skills
from skill_extractor.analyzer import count_skills, sort_skills
from skill_extractor.visualize import plot_histogram


DATA_DIR = "data"
OUTPUT_PATH = "output/histogram.png"


def main():
    all_skills = []

    for file in os.listdir(DATA_DIR):
        if file.endswith(".txt"):
            path = os.path.join(DATA_DIR, file)

            with open(path, "r", encoding="utf-8") as f:
                text = preprocess(f.read())
                skills = extract_skills(text, SKILLS)
                all_skills.append(skills)

    counter = count_skills(all_skills)
    sorted_skills = sort_skills(counter)

    print("\nTop Skills:\n")
    for skill, count in sorted_skills:
        print(f"{skill}: {count}")

    plot_histogram(sorted_skills, OUTPUT_PATH)


if __name__ == "__main__":
    main()