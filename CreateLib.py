# create image library

def get_cmd_line():
  import argparse

  parser = argparse.ArgumentParser(description="Create Image Library")
  parser.add_argument("-ConfigFile", required=True)
  args = parser.parse_args()

  return args.ConfigFile
  
def get_folder_list(config_file_name):
  import json
  config_file = open(config_file_name, "r")
  json_data = config_file.read()
  config_file.close()
  
  raw_data = json.loads(json_data)
  # raw data now is a list of dictionaries

  folder_list = [one_config_line["ImageFolder"] for one_config_line in raw_data if "ImageFolder" in one_config_line]

  return folder_list
  

def scan_single_folder(folder_path):
  import glob
  file_list = glob.glob(folder_path + "\\*.jpg")
  return file_list

def main():
  folder_list = get_folder_list(get_cmd_line())
  image_list = []
  for single_folder in folder_list:
    image_list.extend(scan_single_folder(single_folder))
  
  print("found %d files" % len(image_list))
  print(image_list[0])

main()
