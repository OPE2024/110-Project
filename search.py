from wiki import year_metadata, ask_search, ask_advanced_search

def search(keyword):
  new_list = []
  for item in year_metadata():
    if str(keyword) in item[0:37]:
      new_list.append(item[0:61])
  return new_list
# print(search(2007))

def overall_population(selection, metadata):
    club_list = ""
    for meta in metadata:
      if int(selection) == 1:
        one = "The highest paying salary this club's positions in your chosen year:\n\n"
        club_list = club_list + one +  str(meta[1:7])

      if int(selection) == 2:
        two = "The highest paying salary this club's positions in your chosen year:\n\n"
        club_list = club_list + two +  str(meta[8:13])
      
      if int(selection) == 3:
        three = "The highest paying salary this club's positions in your chosen year:\n\n"
        club_list = club_list + three +  str(meta[14:20])

      if int(selection) == 4:
        four = "The highest paying salary this club's positions in your chosen year:\n\n"
        club_list = club_list + four +  str(meta[21:27])

    return club_list     
# print(overall_population(4,search("2012")))

def display_result():
    years = search(ask_search())

    advanced, value = ask_advanced_search()

    if advanced == 1:
      years = overall_population(value, years)
      pass
  
    print()

    if not years:
        print("That's not a year option.")
    else:
        print("" + str(years))
        
if __name__ == "__main__":
    display_result()

