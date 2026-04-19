def plot_histogram(sorted_skills, save_path=None):
    import matplotlib.pyplot as plt

    skills = [x[0] for x in sorted_skills]
    counts = [x[1] for x in sorted_skills]

    plt.figure(figsize=(14, 6))
    plt.barh(skills[::-1], counts[::-1])  # horizontal + sorted
    plt.xlabel("Frequency")
    plt.title("Skill Demand (Descending)")

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)

    plt.show()