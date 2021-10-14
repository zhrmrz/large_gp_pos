from collections import Counter
class Sol:
    def large_gp_pos(self,s):
        res=[]
        count=Counter(s)
        keys_list=[el[0] for el in count.items() if el[1] >= 3]
        values_list=[el[1] for el in count.items() if el[1] >= 3]
        for i,char in enumerate(keys_list):
            start=s.find(char)
            res.append([start,start+values_list[i]-1])
        return res

if __name__ == '__main__':
    p = Sol()
    print(p.large_gp_pos(s = "abbxxxxzzzy"))
