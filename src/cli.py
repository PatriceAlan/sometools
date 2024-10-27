import click
from guess_number.guess_number import guess_the_number

@click.group()
def cli():
    """Main entry point for various tools"""
    pass

cli.add_command(guess_the_number, name="guess_the_number")

if __name__ == '__main__':
    cli()
