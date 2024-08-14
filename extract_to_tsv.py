import argparse
from pathlib import Path
import json
import csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output_file", required=True, help="the tsv output file to write to")
    parser.add_argument("json_file", help="the json file from which we are extracting content")
    parser.add_argument("num_posts_to_output", type=int, help="the number of posts to be in the tsv file")
    
    args = parser.parse_args()

    # load json data from specified file
    json_data = load_json_file(args.json_file)

    # access and get number of children for comparison to inputs
    children = json_data["data"]["children"]
    num_children = len(children)

    # FIX THIS
    line_counter = 0
    if args.num_posts_to_output > num_children:
        line_counter = num_children
    else:
        line_counter = args.num_posts_to_output

    write_to_tsv(json_data, args.output_file, line_counter)


def load_json_file(json_file):
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    return json_data


def write_to_tsv(json_file, output_file, line_counter):

    # use line_counter to randomize loop

    with open(output_file, 'w', encoding='utf-8') as file:
        tsv_writer = csv.writer(file, delimiter='\t')
        
        headers = ["Name", "title", "coding"]
        tsv_writer.writerow(headers)
        
        children = json_file["data"]["children"]
        
        for child in children:
            child_data = child["data"]
            name = child_data["name"]
            title = child_data["title"]
            tsv_writer.writerow([name, title])


if __name__ == '__main__':
    main()

# run as python extract_to_tsv.py -o annotated_mcgill.tsv mcgill.json 50
# run as python extract_to_tsv.py -o annotated_concordia.tsv concordia.json 50