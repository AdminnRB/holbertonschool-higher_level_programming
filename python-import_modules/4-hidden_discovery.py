#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Modulun içindəki bütün adları götürürük
    all_names = dir(hidden_4)

    # __ ilə başlamayan adları filtrləyib ekrana çıxarırıq
    for name in all_names:
        if not name.startswith("__"):
            print("{}".format(name))
