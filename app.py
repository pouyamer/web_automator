import io

print("Web Automation v0.2.0 ")
print("Created by Pouya Moazzezi")
print("==========================================================")



html_name = input("Type a name for your html file name [index]:")
if html_name.strip() == "":
  html_name = "index"

html_extention = input("Your preferable html file extention (htm | html) [html]")
if html_extention.strip() == "":
  html_extention = "html"

while (html_extention != "htm" and html_extention != "html"):
  print("Didn't catch that.")
  html_extention = input("Your preferable html file extention (htm | html) [html]")
  if html_extention.strip() == "":
    html_extention = "html"

html_title_name = input("Type a title for your page [Document]")
if html_title_name.strip() == "":
  html_title_name = "Document"

css_file_name = input("Type a name for your stylesheet file [style]")
put_css_in_folder = input("You want to put ccs files in folder? y/n [n]")
css_extention = input("Type the name of stylesheet file extention: (css | less | sass | scss) [css]")
js_name = input("Type a name for your script file name: [main]")




with open(html_name + ("." + html_extention), "w") as html:
    html.write('''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="style.css" />
    <title>{html_title_name}</title>
  </head>
  <body>
    <script src="main.js"></script>
  </body>
</html>
'''.replace("{html_title_name}", html_title_name)) # Replaces the title with given name

with open("style.css" , "w") as css:
    css.write('''*,
*::after,
*::before {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}''')

with open("main.js", "w") as js:
    js.write("")

#TODO: add a confirmation at the end
#TODO: add an optional PATH request
#TODO: add validation via os.path.exists(path)
#TODO: add a "code <PATH>" via cmd
#TODO: learn about os in python
#TODO: add a html Title specifier
#TODO: Check if files are already there.
#TODO: add an auto builder using default parameters