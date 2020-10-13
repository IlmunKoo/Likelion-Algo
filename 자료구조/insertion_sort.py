def insertion_sort(L): # L은 포지셔널 리스트
    if len(L) > 1 :
        marker = L.first() # 마커 설정
        while marker != L.last(): # 마커가 끝가지 갔을 경우 정렬 종료
            pivot = L.after(marker) # 피벗은 마커 다음
            value = pivot.element()

            if value > marker.element(): # 피벗이 마커보다 뒤에 있을 때-> 정상(정렬할 것이 x)
                marker = pivot # 피벗이 새 마커가 된다
            else: # must replace pivot
                walk = marker # value보다 큰 값중 가장 왼쪽값?
                while walk != L.first() and L.before(walk).element() > value:  
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value) 



