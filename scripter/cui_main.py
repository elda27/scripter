from argparse import ArgumentParser
from pathlib import Path
from scripter.backend import PresentationGenerator
from scripter.io import Writer

def main():
    parser = ArgumentParser()
    parser.add_argument(
        '-i', '--input', type=Path, required=True,
        help='Input pptx file.'
    )
    parser.add_argument(
        '-o', '--output', type=Path, default=None,
        help='Output file name.'
    )
    parser.add_argument('-t', '--to', type=str, default='txt', choices=['txt', 'stdout'])
    parser.add_argument(
        '--safe-mode', action='store_true', default=False,
    )
    args = parser.parse_args()
    _main(vars(args))

def _main(args):
    generator = PresentationGenerator()
    if args.get('safe_mode',):
        generator.set_safe_mode()
    
    input_filename = args['input']
    presentation = generator.generate(input_filename)

    output_filename =  args.get('output')
    if output_filename is None:
        output_filename = args['input'].with_name(f'{input_filename.name}.{args.get("to")}')

    writer = Writer(output_filename, format=args.get("to"))
    writer.write(presentation.get_note_texts())

if __name__ == "__main__":
    main()