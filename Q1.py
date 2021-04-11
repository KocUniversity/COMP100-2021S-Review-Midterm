import random

POL_CATS = ["Conservative", "Democrat", "Liberal", "Bystander"]
OTHER_POL = ["Socialist", "Authoritarian", "Anarchist", "Communist"]

# Function that creates datasets, you do not need to understand or modify this
def generate_random_dataset(size, categories, other_categories=["Other"]):
  dataset = []
  for _ in range(size):
    preferences = []
    cur_prob = 0
    other_cat = random.choice(other_categories)
    all_cats = categories + [other_cat]
    random.shuffle(all_cats)
    for cat in all_cats:
      if cur_prob < 100:
        cat_prob = random.randrange(0, 101-cur_prob, 5)
      else:
        cat_prob = 0
      preferences.append((cat_prob/100, cat))
      cur_prob += cat_prob
    if cur_prob < 100:
      _, cat = preferences.pop()
      preferences.append(((100-cur_prob)/100, cat))
    dataset.append(preferences)
  return dataset

# Implement your solution for Parts 1 & 2 in this function.
# Do not change anything outside of the areas marked with our comments
def part1and2(dataset, threshold):
  summary = []
  ##########################
  ### START OF YOUR CODE ###
  ##########################



  ##########################
  ###  END OF YOUR CODE  ###
  ##########################
  return summary
    
# Implement your solution for Part 3 in this function.
# Do not change anything outside of the areas marked with our comments
def part3(dataset):
  means = []
  std_devs = []
  ##########################
  ### START OF YOUR CODE ###
  ##########################



  ##########################
  ###  END OF YOUR CODE  ###
  ##########################
  return means, std_devs

# Feel free to modify this function. It is here to help you test your code.
# When you run this file, the main function will do 3 things:
# * Generate a random dataset for part1, and test your part1and2 function
# * Generate a random dataset for part2, and test your part1and2 function
# * Using the dataset for part2, test your part3 function
def main():
  print("Part 1:")
  print("Printing Dataset")
  dataset = generate_random_dataset(5, POL_CATS)
  for elt in dataset:
      print(elt)
  print("-"*80)
  print("Part 1 Summary:")
  tldr = part1and2(dataset, 0.5)
  print(tldr)

  print("-"*80)

  print("Part 2:")
  print("Printing Dataset")
  dataset = generate_random_dataset(10, POL_CATS, OTHER_POL)
  for elt in dataset:
      print(elt)
  print("-"*80)
  print("Part 2 Summary:")
  tldr = part1and2(dataset, 0.5)
  print(tldr)

  print("-"*80)

  print("Part 3:")
  means, std_devs = part3(dataset)
  print("Means of votes:")
  print(means)

if __name__ == "__main__":
  main()