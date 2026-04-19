from collections import Counter

def count_skills(skill_lists):
    counter = Counter()

    for skills in skill_lists:
        counter.update(skills)

    return counter


def sort_skills(counter):
    return counter.most_common()