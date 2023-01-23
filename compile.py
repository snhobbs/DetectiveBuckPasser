'''
Make a tree of all content files
pass through each and generate the js for it
add to the end of the game disk
finally add append the disk to the end.
'''

import click, pypandoc, pandas
import os, glob


def parse_meta(lines):
    delimiter = ':'
    meta = dict()

    for line in lines:
        if delimiter in line:
            split = line.split(delimiter)
            meta[split[0]] = delimiter.join(split[1:]).strip()
    return meta


def make_js_from_markdown(markdown_file):
    return "%s:{\ntext:`%s\n%s`},\n"%(markdown_file['tag'], markdown_file['title'], markdown_file['text'])


class MarkdownFile:
    def __init__(self, fname):
        self._fname = fname
        with open(fname, 'r') as f:
            lines = [line.strip() for line in f.readlines()]

        series = pandas.Series(lines)
        meta_line = '---'
        start, end = list(series[series == meta_line].index)[:2]
        self._meta = parse_meta(series[start:end+1])
        self._body = '\n'.join(series[end+1:])
        self._dict = {'text': self._body}
        self._dict.update(self._meta)


    def __getitem__(self, key):
        return self._dict[key]


types = (
    "cut_scenes",
)


@click.command()
@click.option("--directory", "-d", required=True)
@click.option("--source", required=True, multiple=True)
@click.option("--out", required=True)
def main(directory, source, out):
    if os.path.exists(out):
        print(f"{out} exists, quiting")
        return

    with open(out, 'w') as f:
        for d in types:
            f.write("const %s = {\n"%d)
            path = os.path.join(directory, d)
            glob_path = os.path.join(path, "*.md")
            for fname in glob.glob(glob_path):
                markdown_file = MarkdownFile(fname=fname)
                f.write(make_js_from_markdown(markdown_file))

            f.write("};\n\n")


        for source_name in source:
            with open(source_name, 'r') as s:
                f.write(s.read())

main()
