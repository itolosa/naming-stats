from functools import reduce
import os
from typing import List


FILENAMES = [
    "django_top_1k_class_words.txt",
    "chromium_top_1k_class_words.txt",
    "dotnet_top_1k_class_words.txt",
    "python_top_1k_class_words.txt",
    "rails_top_1k_class_words.txt",
    "spree_top_1k_class_words.txt"
]


def dataset_path(filename: str) -> str:
    rootdir = os.path.dirname(__file__)
    return os.path.join(rootdir, "datasets", filename)


def results_path(filename: str) -> str:
    rootdir = os.path.dirname(__file__)
    return os.path.join(rootdir, "results", filename)


def read_file_into_lines(filename: str) -> list:
    with open(filename, "r") as fp:
        return [line for line in fp]
    raise Exception("Error reading the file at `read_lines`")


def convert_lines_to_dict(lines: list) -> dict:
    return {k: int(v) for v, k in map(lambda line: line.split(), lines)}


def read_file_into_dict(filename: str) -> dict:
    return convert_lines_to_dict(read_file_into_lines(filename))


def write_lines_to_file(filename: str, lines: list) -> None:
    with open(filename, "w") as fp:
        fp.write("\n".join(lines))


def convert_pair_to_line(pair: list) -> str:
    return f"{pair[0]} {pair[1]}"


def convert_items_to_lines(items: List[list]) -> List[str]:
    return map(convert_pair_to_line, items)


def convert_dict_to_lines(d: dict) -> list:
    return list(convert_items_to_lines(d.items()))


def write_dict_to_file(filename: str, d: dict) -> None:
    write_lines_to_file(filename, convert_dict_to_lines(d))


def get_common_keys(d1: dict, d2: dict) -> set:
    return set(d1.keys()).intersection(set(d2.keys()))


def filter_dict_by_keys(d: dict, selected_keys: set) -> dict:
    return {k: v for k, v in d.items() if k in selected_keys}


def combine_dicts(d1: dict, d2: dict) -> dict:
    result = dict(d1)
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result


def intersect_and_combine_dicts(d1: str, d2: str) -> dict:
    """
    Get the combination (sum of the values) of the common keys between both dicts
    """
    return filter_dict_by_keys(combine_dicts(d1, d2), get_common_keys(d1, d2))


def intersect_and_combine_multiple_dicts(ds: List[dict]) -> dict:
    return reduce(intersect_and_combine_dicts, ds)


def combine_multiple_dicts(ds: List[dict]) -> dict:
    return reduce(combine_dicts, ds)


def sort_by_count(d: dict) -> list:
    return sorted(d.items(), key=lambda x: x[1], reverse=True)


def print_each(items: list):
    for name, frequency in items:
        print(f"{name} {frequency}")

def read_files_into_dicts(filenames: List[str]) -> List[dict]:
    return [read_file_into_dict(filename) for filename in filenames]


def process_sorted_aggregation() -> None:
    ds = read_files_into_dicts(map(dataset_path, FILENAMES))
    d = combine_multiple_dicts(ds)
    lines = convert_items_to_lines(sort_by_count(d))
    write_lines_to_file(results_path("sorted_agg_all.txt"), lines)


def process_sorted_common() -> None:
    ds = read_files_into_dicts(map(dataset_path, FILENAMES))
    d = intersect_and_combine_multiple_dicts(ds)
    lines = convert_items_to_lines(sort_by_count(d))
    write_lines_to_file(results_path("sorted_agg_common.txt"), lines)


if __name__ == "__main__":
    process_sorted_aggregation()
    process_sorted_common()
