def solution(s):
    st = []
    
    for c in s:
        if c == '(':
            st.append(c)
        else:
            if st: st.pop()
            else: return False

    return True if st == [] else False