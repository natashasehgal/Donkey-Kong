import donkeykong as d

class Test_Donkey():
    def test_checkDonk(self):
        flag=0
        for i in range(d.HEIGHT):
            for j in range(d.WIDTH):
                if d.lay[i][j]=='D':
                    flag+=1
        assert flag==1

