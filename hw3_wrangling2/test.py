import json
from pandas import DataFrame, Series
from collections import Counter


with open("nytimes_archive_202001.json", "r") as f:
    dat = json.load(f)

subject_counter = Counter()
all_authors = set()


def get_full_name(author_info):
    name_letters = []

    first_name = author_info.get('firstname')
    if first_name:
        name_letters.append(first_name[0])

    middle_name = author_info.get('middlename')
    if middle_name:
        name_letters.append(middle_name[0])
    last_name = author_info.get('lastname')
    if last_name:
        name_letters.append(last_name[0])

    if not name_letters:
        return None
    full_name = ' '.join(name_letters)
    return full_name


def statistic_subject_and_author():
    for key, article in dat.items():
        keyword_list = article.get('keywords', [])

        current_subjects = []
        for keyword_info in keyword_list:
            if 'subject' in keyword_info.get('name', []):
                subjects = keyword_info.get('value', [])
                for sub in subjects:
                    # if subject not exist in global counter, need init
                    if sub not in subject_counter:
                        author_counter = Counter()
                        subject_counter[sub] = author_counter
                        current_subjects.append(sub)

        author_list = article.get("byline", {}).get("person", [])

        for author_info in author_list:
            full_name = get_full_name(author_info)
            if not full_name:
                continue
            all_authors.add(full_name)

            for sub in current_subjects:
                author_counter = subject_counter[sub]
                author_counter[full_name] += 1
                # if author_counter[full_name] > 1:
                #     print(sub, full_name)


def test_nytimes():
    statistic_subject_and_author()

    temp_df = DataFrame(columns=subject_counter.keys())

    for sub, author_counter in subject_counter.items():
        noninitual_authors = all_authors - set(author_counter.keys())
        for author in noninitual_authors:
                author_counter[author] = 0

        temp_df[sub] = Series(dict(author_counter))

    return temp_df


def test_a():
    auth_sub_df = test_nytimes()
    tx = (auth_sub_df == 0).mean().mean()
    print(tx)

test_a()
# statistic_subject_and_author()
#
# temp_df = DataFrame(columns=subject_counter.keys())
#
# for sub, author_counter in subject_counter.items():
#     noninitual_authors = all_authors - set(author_counter.keys())
#     for author in noninitual_authors:
#             author_counter[author] = 0
#
#     temp_df[sub] = dict(author_counter)
# auth_sub_df = temp_df

# auth_sub_df = DataFrame([{'a': 0, 'b': 0}], index=['test1'])


def testb():
    # How many unique authors are working for NYTimes
    nyt1 = len(auth_sub_df)
    # How many "subjects" have NYTimes written about
    nyt2 = len(auth_sub_df.columns)
    # Which author has written about the most number of "subjects"
    nyt3 = auth_sub_df.apply(sum, axis=1).idxmax()
    # Which "subject" is the most popular across authors for NYTimes
    nyt4 = auth_sub_df.apply(sum, axis=0).idxmax()

    print(nyt1, nyt2, nyt3, nyt4)
