import re

def extract_skills(text: str, skill_dict: dict):
    found_skills = set()

    for skill, variants in skill_dict.items():
        for variant in variants:
            pattern = r'\b' + re.escape(variant) + r'\b'
            if re.search(pattern, text):
                found_skills.add(skill)
                break

    return list(found_skills)