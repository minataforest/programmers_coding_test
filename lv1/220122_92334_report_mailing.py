def solution(id_list, report, k):
    # 신고내역 중복 제거
    report = set(report)

    # 신고자와 피신고자 관계를 dict 형식으로 만듦
    # {'muzi': ['neo', 'frodo'], 'apeach': ['frodo', 'muzi'], 'frodo': ['neo']}
    # 신고 받은 개수 dict 형식으로 만듦 {'neo': 2, 'frodo': 2}
    new_list = dict()
    report_cnt = dict()
    
    for rp in report:
        name = rp.split(' ')
        report_cnt[name[1]] = 1 if name[1] not in report_cnt else (report_cnt[name[1]] +1)
        if name[0] in new_list:
            new_list[name[0]].append(name[1])
        else:
            new_list[name[0]] = [name[1]]

    # 피신고 개수를 세어 신고 개수가 k를 넘는 것만 남긴다
    final_report =[]
    for key, value in report_cnt.items():
        if value >= k:
            final_report.append(key)
            
    # 메일 리스트
    mail_list = dict()
    for i in id_list:
        mail_list[i] = 0
        
    # new_list 돌리면서 final_report에 해당하는 것이 있는지 확인. 있으면 mail_list에 +1
    for key, value in new_list.items():
        for v in value:
            if v in final_report:
                mail_list[key] += 1
                                 
    return [v for v in mail_list.values()]


# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    #[0, 0, 0, 0, ...]
#     reports = {x : 0 for x in id_list} #{'frodo':0, 'apeach': 0 ...}

#     for r in set(report):
#         reports[r.split()[1]] += 1  # {'frodo': 1, 'apeach': 0...}
        
#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer