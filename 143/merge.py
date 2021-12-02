from itertools import chain

NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
   """Look up name (case insensitive search) and return age.
      If name in > 1 dict, return the match of the group with
      greatest N (so group3 > group2 > group1)
   """
   try:
      name = name.lower()
      combined_keys = list(chain(group1.keys(),group2.keys(),group3.keys()))
      if name not in combined_keys:
         return NOT_FOUND
      elif name in group3.keys():
         return group3[name]
      elif name in group2.keys():
         return group2[name]
      else:
         return group1[name]
   except:
      return NOT_FOUND