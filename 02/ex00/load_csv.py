import pandas


def load(path: str) -> pandas.DataFrame | None:
    """load CSV file at 'path' and return Dataset object of pandas"""
    try:
        return pandas.read_csv(path)
    except Exception as e:
        print("Error: cannot load data.")
        print(e)
    return None
