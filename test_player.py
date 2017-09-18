import donkeykong as d

class Test_Player():
    def test_checkPlayer(self):
        flag=0
        for i in range(d.HEIGHT):
            for j in range(d.WIDTH):
                if d.lay[i][j]=='P':
                    flag+=1
        assert flag==1

    def test_moveUp(self):
        pos_x=d.P.X
        pos_y=d.P.Y
        d.P.moveUp(pos_x,pos_y,d.P)
        new_pos_x=d.P.X
        new_pos_y=d.P.Y
        if d.Dum.collision('up',d.P):
            assert new_pos_x==pos_x-1
            assert new_pos_y==pos_y
        else:
            assert new_pos_y==pos_y
            assert new_pos_x==pos_x


    def test_moveDown(self):
        pos_x=d.P.X
        pos_y=d.P.Y
        d.P.moveDown(pos_x,pos_y,d.P)
        new_pos_x=d.P.X
        new_pos_y=d.P.Y
        if d.Dum.collision('down',d.P):
            assert new_pos_x==pos_x+1
            assert new_pos_y==pos_y
        else:
            assert new_pos_y==pos_y
            assert new_pos_x==pos_x


    def test_moveLeft(self):
        pos_x=d.P.X
        pos_y=d.P.Y
        d.P.moveLR(pos_x,pos_y,d.P,'a')
        new_pos_x=d.P.X
        new_pos_y=d.P.Y
        if d.Dum.collision('left',d.P):
            assert new_pos_x==pos_x
            assert new_pos_y==pos_y-1
        else:
            assert new_pos_y==pos_y
            assert new_pos_x==pox_x


    def test_moveRight(self):
        pos_x=d.P.X
        pos_y=d.P.Y
        d.P.moveLR(pos_x,pos_y,d.P,'d')
        new_pos_x=d.P.X
        new_pos_y=d.P.Y
        if d.Dum.collision('right',d.P):
            assert new_pos_x==pos_x
            assert new_pos_y==pos_y+1
        else:
            assert new_pos_y==pos_y
            assert new_pos_x==pox_x

