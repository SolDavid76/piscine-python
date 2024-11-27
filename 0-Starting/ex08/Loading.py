import shutil
from time import sleep


def ft_tqdm(lst: range) -> None:
    total = len(lst)
    bar_width = shutil.get_terminal_size().columns - 40

    for i, item in enumerate(lst, start=1):
        progress = int(i / total * bar_width)
        progress_percentage = int(progress * 100 / bar_width)
        bar = '|' + '█' * progress + ' ' * (bar_width - progress) + '|'
        print(f"\r{progress_percentage}%{bar}{i}/{total}", end="", flush=True)
        yield item

for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()

# ft_tqdm(range(333))
