class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in str(s):
            if i=="(" or i=="{" or i=="[":
                st.append(i)
            else:
                if len(st)==0:
                    return False
                top = st.pop()
                if i==")" and top!="(":
                    return False
                elif i=="}" and top!="{":
                    return False
                elif i=="]" and top!="[":
                    return False
        return len(st)==0

