from pathlib import Path

cwd = Path.cwd()

demo_file = Path(Path.joinpath(cwd, 'demo.text'))

# Get the file name
print(' file name : ' + demo_file.name)

# Get the extension
print(' file suffix: ' + demo_file.suffix)

# Get the folder containing
print(' File folder : ' + demo_file.parent.name)

# Get the size 
print(' File size: ' + str(demo_file.stat().st_size) + ' ')