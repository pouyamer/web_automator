def get_confirmation_input(message, func, default):
  confirmation_input = func(message).strip()

  if confirmation_input == "":
    return default
  while not (confirmation_input == "y" or confirmation_input == "n"):
    print("Didn't catch that.")
    confirmation_input = func(message).strip()
    if confirmation_input.strip() == "":
      return default
  return  confirmation_input


def get_file_name_input(message, func, default):
  #TODO: Add naming conventions for files here.
  file_name = func(message)
  if file_name.strip() == "":
    file_name = default
  return file_name


def get_file_extention_input(message, func, options, default):
  file_extention = func(message).strip()
  if file_extention == "":
    return default

  else:

    for option in options:
      if file_extention == option:
        return option

    while True:
      print("Didn't catch that.")
      file_extention = func(message).strip()

      for option in options:
        if file_extention == option:
          return option

      if file_extention == "":
        return default


def get_folder_name_input(message, func, default):
    folder_name = func(message).strip()
    if folder_name == "" :
      return default
    else:
      return folder_name #TODO: Add Folder naming conventions
