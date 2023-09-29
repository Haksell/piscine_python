from load_image import ft_load

FILENAMES = ["landscape.jpg", "cat.jpeg", "assembly.png", "python.svg"]

for i, filename in enumerate(FILENAMES):
    if i:
        print()
    section = " " + filename.upper() + " "
    print(f"{section:-^42}")
    print(ft_load(filename))
