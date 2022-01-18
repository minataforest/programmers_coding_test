def solution(N, stages):
    f_rate = dict()
    cnt_all_player = len(stages)

    for i in range(1, N+1):
        if cnt_all_player != 0:          
            # 스테이지 클리어하지 못한 플레이어 수
            cnt_not_clear = stages.count(i)

            f_rate[i] = cnt_not_clear / cnt_all_player

            # 현재 스테이지를 클리어하지 못한 플레이어 수만큼을 전체 플레이어 수에서 제외
            cnt_all_player -= cnt_not_clear

        else:
            f_rate[i] = 0

    return sorted(f_rate, key = lambda x: f_rate[x], reverse = True)