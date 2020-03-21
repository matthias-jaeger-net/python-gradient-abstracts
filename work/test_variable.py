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