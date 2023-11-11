import yaml
import os
import Levenshtein

class Nurec:
  def __init__(self, recognized_data):
    self.recognized_data = recognized_data
    self.total_chars = 0
    self.mismatched_chars = 0
    self.details_list = []
    self.load_yaml_and_compare()

  def load_yaml_and_compare(self):
    for data in self.recognized_data:
      file_name = data["File Name"]
      module_dir = os.path.dirname(os.path.abspath(__file__))
      yaml_file_path = os.path.join(module_dir, 'verification', f"{file_name}.yaml")

      with open(yaml_file_path, 'r') as f:
        yaml_data = yaml.safe_load(f)

      # Comparing data
      for key, value in data.items():
        if key in yaml_data:
          # If the value is a list, we bypass each element
          if isinstance(value, list):
            for i, item in enumerate(value):
              for sub_key, sub_value in item.items():
                if sub_key in yaml_data[key][i]:
                  self.compare_values(sub_value, yaml_data[key][i][sub_key], file_name, sub_key)
          else:
            self.compare_values(value, yaml_data[key], file_name, key)

  def compare_values(self, recognized_value, yaml_value, file_name, key_name):
    self.total_chars += max(len(recognized_value), len(yaml_value))
    mismatched = False

    lev_distance = Levenshtein.distance(recognized_value, yaml_value)
    self.mismatched_chars += lev_distance

    if lev_distance > 0:  # If there's any difference between the strings
      mismatched = True

    if mismatched:
      self.details_list.append({
        "file_name": file_name,
        "key_name": key_name,
        "distance": lev_distance,
        "expected": yaml_value,
        "received": recognized_value
      })

  def accuracy(self):
    if self.total_chars == 0:
      return 0
    return 100 - (self.mismatched_chars / self.total_chars * 100)

  def details(self):
    result_str = ""
    for detail in self.details_list:
      result_str += f"[{detail['key_name']}] {detail['file_name']}\n"
      result_str += f"distance: {detail['distance']}\n"
      result_str += f"expected:\n{detail['expected']}\n"
      result_str += f"received:\n{detail['received']}\n\n"
    return result_str.rstrip()

  def total_distance(self):
    return self.mismatched_chars
