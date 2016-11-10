import re
per_info = 'E:Jackandjill@twitter.com'

def personal_info_mask(per_info):
    regex = r'[PE]:'
    matches = re.search(regex, per_info, re.IGNORECASE)
    if 'E' in matches.group(0):
        per_info = per_info.replace(' ', '')
        stars = ['*'] * 5
        i = 3
        counter = 0
        index = []
        for i in per_info:
            if i == '@':
                index.append(counter-1)
            counter += 1
        per_info = per_info[:2] + ''.join(stars) + per_info[index[0]:]
        return(per_info.strip())
    elif 'P' in matches.group(0):
        per_info = normalize_data(per_info, matches)
        return(matches.group(0) + per_info)

def char_replace(per_info):
    for char in (' ', '(', ')', '-'):
        if char in per_info:
            per_info = per_info.replace(char, '')
    return(per_info)

def normalize_data(per_info, matches):
    per_info = per_info.replace(matches.group(0), '')
    per_info = char_replace(per_info)
    if '+' in per_info:
        if len(per_info) <= 8:
            per_info = '+' + add_stars(per_info[1:4]) + '-' + per_info[4:]
        elif len(per_info) == 11:
            per_info = '+' + add_stars(per_info[-10:-7]) +'-'+ add_stars(per_info[-7:-4]) +'-'+ per_info[-4:]
        else:
            per_info = '+' + add_stars(per_info[1:-10]) +'-'+ add_stars(per_info[-10:-7]) +'-'+ add_stars(per_info[-7:-4]) +'-'+ per_info[-4:]
    else:
        if len(per_info) <= 7:
            per_info = add_stars(per_info[:3]) + '-' + per_info[3:]
        elif len(per_info) == 10:
            per_info = add_stars(per_info[-10:-7]) +'-'+ add_stars(per_info[-7:-4]) +'-'+ per_info[-4:]
        else:
            per_info = add_stars(per_info[0:-10]) +'-'+ add_stars(per_info[-10:-7]) +'-'+ add_stars(per_info[-7:-4]) +'-'+ per_info[-4:]
    return(per_info.strip())

def add_stars(per_info):
    temp_list = ['*' for x in list(per_info)]
    return(''.join(temp_list))

print(personal_info_mask(per_info))