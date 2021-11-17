"""
Position: Senior Python Developer
Candidate: Samuel Braganza
"""

from helpers.combinations import combinations
from helpers.files import load_tt


def timesheet():
    # filename = 'files/test-1.txt'
    filename = 'files/test-2.txt'
    tt_dic = load_tt(filename)
    tt_values = list(tt_dic.values())
    coincided_dic = {}

    tt_combinations = combinations(tt_values, 2)
    
    for tt_combination in tt_combinations:
        tt1_arr = tt_combination[0]
        tt2_arr = tt_combination[1]
        for tt1 in tt1_arr:
            for tt2 in tt2_arr:
                coincided_key = '{}-{}'.format(tt1.username, tt2.username)
                if coincided_key not in coincided_dic:
                    coincided_dic[coincided_key] = 0
                if tt1.is_overwritten(tt2):
                    print('Current timetracker ({}) overwrites existing timetracker ({})'
                            .format(str(tt2), str(tt1)))
                    coincided_dic[coincided_key] += 1
    print(coincided_dic)


if __name__ == '__main__':
    timesheet()