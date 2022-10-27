import json
from pandas import DataFrame, Series

with open("nytimes_archive_202001.json", "r") as f:
    dat = json.load(f)

no_name_count = 0


def get_full_name(author_info):
    name_letters = []

    first_name = author_info.get('firstname')
    if first_name:
        if len(first_name) > 1:
            print(first_name)
        name_letters.append(first_name[0])

    middle_name = author_info.get('middlename')
    if middle_name:
        if len(middle_name) > 1:
            print(middle_name)
        name_letters.append(middle_name[0])
    last_name = author_info.get('lastname')
    if last_name:
        if len(last_name) > 1:
            print(last_name)
        name_letters.append(last_name[0])

    if not name_letters:
        global no_name_count
        no_name_count += 1
        return 'no_name' + str(no_name_count)

    full_name = ' '.join(name_letters)
    return full_name


from collections import defaultdict
sub_author_dict = defaultdict(dict)

all_subjects = set()
all_authors = set()


def get_all_subject_and_authors():
    for key, article in dat.items():
        keyword_list = article.get('keywords', [])

        current_subjects = set()
        for keyword_info in keyword_list:
            if 'subject' in keyword_info.get('name', []):
                subjects = keyword_info.get('value', [])
                for sub in subjects:
                    current_subjects.add(sub)
                    all_subjects.add(sub)

        author_list = article.get("byline", {}).get("person", [])

        for sub in current_subjects:
            if sub not in sub_author_dict:
                sub_author_dict[sub] = defaultdict(int)
            author_dict = sub_author_dict[sub]
            for author_info in author_list:
                full_name = get_full_name(author_info)
                all_authors.add(full_name)

                author_dict[full_name] += 1


get_all_subject_and_authors()
temp_df = DataFrame()

# print(all_authors)
#
for sub, author_info in sub_author_dict.items():
    noninitual_authors = all_authors - set(author_info.keys())
    for author in noninitual_authors:
        author_info[author] = 0

    temp_df[sub] = Series(author_info)
#
# print(temp_df.max().max())
auth_sub_df = temp_df

# How many unique authors are working for NYTimes
nyt1 = len(auth_sub_df)
# How many "subjects" have NYTimes written about
nyt2 = len(auth_sub_df.columns)
# Which author has written about the most number of "subjects"

def count_subject(row):
    num = 0
    xxx = dict(row)
    for k,v in xxx.items():
        if v>0:
            num+=1
    return num

nyt3 = auth_sub_df.apply(count_subject, axis=1).idxmax()
# Which "subject" is the most popular across authors for NYTimes
nyt4 = auth_sub_df.apply(count_subject, axis=0).idxmax()

print(nyt1, nyt2, nyt3, nyt4)