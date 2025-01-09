# import os


def ft_tqdm(lst: range) -> None:
    """The function must copy the function tqdm with the yield operator."""

    terminal_size = 120
    # terminal_size = os.get_terminal_size().columns
    right_padding = ""
    # right_padding = ' ' * len("[00:02<00:00, 162.44it/s]")
    total = len(lst)

    for now in lst:
        now += 1
        percent = f"{now*100//total:3d}%"
        progress = f"{now}/{total}"

        progress_bar_size = terminal_size \
            - len(percent) - len(progress) - len(right_padding) - 6
        progress_percent = int(now*progress_bar_size//total)

        progress_bar = ('=' * (progress_percent - 1)) + '>' 
        if progress_percent == 0:
            progress_bar += (' ' * (progress_bar_size - progress_percent - 1))
        else:
            progress_bar += (' ' * (progress_bar_size - progress_percent))
            

        print(f"\r{percent}|[{progress_bar}]"
              f"| {progress}{right_padding}", end="")

        yield

    print()
