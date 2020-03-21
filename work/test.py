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