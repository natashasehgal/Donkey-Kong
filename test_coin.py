import donkeykong as d

class Test_Coin():
    def test_checkCoin(self):
        flag=0
        for i in range(d.HEIGHT):
            for j in range(d.WIDTH):
                if d.lay[i][j]=='C':
                    flag+=1
        assert flag==20
 
