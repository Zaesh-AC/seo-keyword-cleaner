import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "-origin", "--o",
    dest="origin",
    help="File CSV con i dati da pulire. Il delimitatore DEVE essere ';'"
)
parser.add_argument(
    "-dest", "--d",
    dest="dest",
    default="output",
    help="Nome del file di destinazione"
)
parser.add_argument(
    "-k", "--keys",
    dest="keys",
    help="File CSV con le chiavi da esaminare. Il delimitatore DEVE essere ','"
)
args = parser.parse_args()

def get_keys():
    keys = []
    with open(args.keys) as keys_file:
        keys_reader = csv.reader(keys_file)
        for key in keys_reader:
            keys.extend(key)
        return keys

def check_keys_match(row):
    for key in get_keys():
        if key == row or key in row:
            return True
    return False

def get_items(reader):
    valid_items = []
    invalid_items = []
    for readed_row in reader:
        if check_keys_match(readed_row[0]):
            invalid_items.append(readed_row)
        else:
            valid_items.append(readed_row)
    return valid_items, invalid_items

def main():
    with open(args.origin, "r") as origin:
        reader = csv.reader(origin, delimiter=";")
        valid_items, invalid_items = get_items(reader)
        with open(f"valid_{args.dest}.csv", "w+") as valid_items_file:
            valid_writer = csv.writer(valid_items_file, delimiter=";")
            for valid_row in valid_items:
                valid_writer.writerow(valid_row)
        with open(f"invalid_{args.dest}.csv", "w+") as invalid_items_file:
            invalid_writer = csv.writer(invalid_items_file, delimiter=";")
            for invalid_row in invalid_items:
                invalid_writer.writerow(invalid_row)

if __name__ == "__main__":
    main()