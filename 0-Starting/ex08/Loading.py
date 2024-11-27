import shutil
from time import sleep


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_width = shutil.get_terminal_size().columns - 40

    for i, item in enumerate(lst, start=1):
        progress = int(i / total * bar_width)
        percentage = f"{int(progress * 100 / bar_width):>3}%"
        bar = f"|{'-' * progress:<{bar_width}}|"
        total_progress = f" {i}/{total}"
        print(f"\r{percentage}{bar}{total_progress}", end="", flush=True)
        yield item
