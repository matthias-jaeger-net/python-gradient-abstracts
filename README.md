# python-gradient-abstracts
Abstract artistic background images created with code

## Research
- Create a vector graphic with ``python 3``
- Descided for ``<svg>`` as a output format
- Descided not to use any imported library

# Create my setup
## Visual Studio Code Community edition
- I choose to work in Visual Studio Code Community edition
- First I open a terminal and navigate into the my documents
- I git clone the repository and open it in VS Code
- - ``git clone git@github.com:matthias-jaeger-net/python-gradient-abstracts.git``
- Then I open a new terminal and proceeed with the setup

## Python 3 virtualenv
- Create a new directory to 'rest' the virtualenv
- - ```mkdir venv```
- Installing the virtualenv in the directory
- - ```virtualenv -p python3 venv```
- Activating the virtualenv
- - ```source venv/bin/activate```
- Hide the venv for gitHub, create a gitignore file
- - ``echo '/venv/' > .gitignore``

## Create the working directory
- ```mkdir work```
- ```cd work```
- ```touch test.py```
- ```echo 'print("hello world")' > test.py```
- ```python test.py```
- - ```Output: hello world```

# Writing a svg with python
There are many ways to open and write to a file in python. I picked the file handler variant in combination with a call to open() and give a name and method to the function. Since we want to create a svg graphic I used an example and added it to the code.

### Example
<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
</svg>

```xml
<svg width="100" height="100">
  <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
</svg>
```

```python
# Template parts
# - Cutting the example from w3schools
begin = "<svg version=\"1.1\" "
begin += "baseProfile=\"full\" "
begin += "width=\"300\" "
begin += "height=\"200\" "
begin += "xmlns=\"http://www.w3.org/2000/svg\">"
elem = "<circle cx=\"50\" cy=\"50\" r=\"40\" stroke=\"green\" stroke-width=\"4\" fill=\"yellow\" />"
end = "</svg>"

# Opens a handler for the file named 'f'
with open("gfx.svg", "w") as f:
  lines = [begin, elem, end]
  f.writelines(lines)
```

# Making the graphic variable
I started to create a function that can return me any kind of svg graphic, that I later on use in the same way as above to write to the file.

```python
# UTILS

def createGraphic(w, h, content):
  #  Returns a svg string based on
  #  - w: width, pixels
  #  - h: height, pixels
  #  - content: string given shape to draw

  # SVG attributes
  version = "1.1"
  baseProfile = "full"
  width = str(width)
  height = str(height)
  xmlns = "http://www.w3.org/2000/svg"

  # SVG string template
  return f"""
          <svg
              version="{version}"
              baseProfile="{baseProfile}"
              width="{width}"
              height="{height}"
              xmlns="{xmlns}">
              {content}
          </svg>
          """

# WRITING TO THE FILE

with open("gfx_variable.svg", "w") as f:

  # Basic circle from example
  elem = "<circle cx=\"50\" cy=\"50\" r=\"40\" stroke=\"green\" stroke-width=\"4\" fill=\"yellow\" />"

  # Using the defined function from above
  f.write(createGraphic(300, 300, elem))
```