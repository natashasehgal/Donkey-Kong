from threading import Thread
from termcolor import colored
import math,time,random,sys,os,numpy,readchar
WIDTH,HEIGHT,HEIGHT2=80,27,33
lay=[[' ' for i in range(WIDTH)] for j in range(HEIGHT2)] #create board
fb,f=[],0
class Board:
    def __init__(self):#initialize board
        self.lives,self.coincount,self.cc,self.fb=3,0,0,0
        self.level,self.ld,self.space=0,0,0
        self.layout()
    def coins(self):#generate coins
        c=0
        while(c<20):
            X=[5,9,13,17,21,25]
            x=random.randrange(6)
            y=random.randrange(WIDTH)
            if lay[X[x]][y]==' ' and lay[X[x]+1][y]=='X':
                lay[X[x]][y]='C'
                c+=1 
    def printLay(self):#print board
        for i in range(HEIGHT2):
            for j in range(WIDTH):
                sys.stdout.write(lay[i][j])
            print ' '
    def collectCoin(self):#add score
      self.coincount+=5
      lay[31][6]=str(self.coincount)

########---------LAYOUT:---------#########
    def layout(self):
        global f
    #########-------Border-------------########
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if(lay[i][j]=='P' and i!=HEIGHT-2 and j!=2):
                        lay[i][j]=' '
                if(self.cc==0):
                    lay[i][j]=' '
                lay[0][j],lay[HEIGHT-1][j]='X','X'
            lay[i][0],lay[i][WIDTH-1]='X','X'
    ########-----FLOOR---#################
        if(self.fb==0): 
            p_len=0 
            row=[6,10,14,18,22]
            for i in range(len(row)):
                y=random.randint(40,65)
                if i==0:
                    p_len=y  #length of line
                if i%2==0:
                    for j in range(y):
                        lay[row[i]][j]='X'
                else:
                    y=WIDTH-1-y
                    while(y!=WIDTH-1):
                        lay[row[i]][y]='X'
                        y+=1
    ###########---PRINCESS && DONKEY----###################
            x=random.randint(p_len/5,p_len/3) #length of cage 
            lay[5][2]='D'
            y=random.randrange(p_len-x+1) #start point
            lay[1][y+2],lay[1][x+y+1]='X','X'
            for i in range(y+2,x+y+2):
                lay[2][i]='X'
            lay[1][random.randint(y+3,x+y)]='Q'
    ############--------Stairs-----------###############
            row.append(2)        
	    for i in range(6):
                j=0
                while True:
                    y=random.randint(2,WIDTH-1)
                    if lay[row[5]-1][y] in ['X','Q']:#cage boundary
                        continue
                    if lay[row[i]][y]=='X'and lay[row[i]+4][y]=='X' and lay[row[i]][y-1]!='H' and lay[row[i]-1][y]!='H' and lay[row[i]][y+1]!='H':
                        lay[row[i]][y],lay[row[i]+1][y],lay[row[i]+2][y],lay[row[i]+3][y]='H','H','H','H'
                        j+=1
		        if j==2:
                            x=random.randrange(1,2)
                            lay[row[i]+x][y]=' '
                            break
            else:
                self.fb=0
    ##########----STATS-----#########
        lay[29][0],lay[29][1],lay[29][2],lay[29][3],lay[29][4],lay[29][5],lay[29][6],='L','E','V','E','L',':',str(self.level)
        lay[31][0],lay[31][1],lay[31][2],lay[31][3],lay[31][4],lay[31][5],lay[31][6]='S','C','O','R','E',':', str(self.coincount)
        lay[30][0],lay[30][1],lay[30][2],lay[30][3],lay[30][4],lay[30][5],lay[30][6]='L','I','V','E','S',':',str(self.lives)
        lay[HEIGHT-2][2]='P'
        P.X,P.Y=HEIGHT-2,2
        if str(type(f))=="<type 'list'>":
            lay[f[0]][f[1]]='H'
            f=0
        if(self.cc==1):
            self.cc=0
#########-----------Movement/Moving Players----------############# 

class Move():
    global board
    def __init__(self):#initialize moving player
        self.X,self.Y,self.name=0,0,'P'
    def getPosition(self):#get position
        return [self.X,self.Y]
    def collision(self,direction,player):#check for collision
        global P,board
        x,y=self.X,self.Y     
        if direction in ['left','right']:
            if(direction=='left'):
                c=-1
            else:
                c=1
            if(player.name=='O' and lay[x][y+c]=='P'):
                self.collision('fireball',P)
            if(lay[x][y+c]=='X' or lay[x+1][y+c]==' '):return True
            return False
        elif(direction=='up'):
            if board.space==0 and (lay[x-1][y]=='H' or (lay[x][y-1] in [' ','X'] and lay[x][y+1]=='X') or (lay[x][y-1]=='X' and lay[x][y+1] in [' ','X'])):
                player.ld,player.bc=0,0
                return False
            if board.space==1:
                board.space=0
                return False
            return True
        elif(direction=='down'):
            if(board.space==0 and lay[x+1][y]=='H'):#
                return False
            if(player.name=='P' and lay[x+1][y]=='O'):
                self.collision('fireball',P)
            if(player.name=='O' and lay[x+1][y]=='P'):
                self.collision('fireball',P)
            if(board.space==1):
                board.space=0
                if(lay[x+1][y]=='O'):#can't jump on fb
                    return True
                return False
        elif(direction=='fireball'):
            if(player.name=='P'):
                board.coincount-=25
                board.lives-=1
                board.cc,board.fb=1,1 #resest position,no coin/fireball
                board.layout() 
            if(player.name=='D'):
                return False
    def move(self,direction,player):
        x,y=player.X,player.Y
        if direction=="d" or direction=="a":
            self.moveLR(x,y,player,direction)
        elif direction=="w":
          self.moveUp(x,y,player)
        elif direction=="s":
            self.moveDown(x,y,player)
        elif direction==" ":
            os.system("stty cbreak -echo")
            z=sys.stdin.read(1)
            os.system("stty -cbreak -echo")
            if z=="d" or z=="a" or z=="w":
                self.moveSpaceLUR(z,player)
    
    def moveSpaceLUR(self,z,player):
        global board,Dum
        i,c,d=0,-1,0
        if(z=="d" or z=="a"):
            if(z=="d"):
                if(player.Y+4>WIDTH-2):return
                d,c,dire,dire1=1,1,'right','left'
            if(z=="a"):
                if(player.Y-4<1):return
                d,c,dire,dire1=-1,-1,'left','right'
            
            Dum.X,Dum.Y,board.space=player.X-2,player.Y+c*1,1  
            if self.collision(dire,Dum)==True:return
            board.space=1
            if self.collision('down',Dum)==True:return
            Dum.Y,board.space=player.Y+c*3,1
            if self.collision(dire1,Dum)==True:return
            board.space=1
            if self.collision('down',Dum)==True:return
            Dum.X,Dum.Y,board.space=player.X-1,player.Y+c*4,1
            if self.collision('down',Dum)==True:return
        elif(z=="w"):
            d=0
        else:
            return
        temp1=0
        while(i<4):
            temp,c=0,-1
            time.sleep(.2)
            if(i>=2):
                c=1
            temp=lay[player.X+c][player.Y+d]
            lay[player.X+c][player.Y+d]=player.name
            if(temp=='O'):
                lay[player.X+c][player.Y+d]=temp #put fireball back and collide
                self.collision('fireball',player)
                return
            elif(temp=='C'):#collect put space
                board.collectCoin()
                temp=' '
            lay[player.X][player.Y]=' '
            if(temp1=='H'): #up H put back
                lay[player.X][player.Y]='H'
            i+=1
            player.X+=c
            player.Y+=d
            temp1=temp
            board.printLay()

    def moveLR(self,x,y,player,direction):#move sideays
        c=0
        global flag
        if(direction=='a' and self.collision('left',player)==False):
            c=-1
        elif(direction=='d' and self.collision('right',player)==False):
            c=1
        if(c !=0):
            if(player.name=='P'):
                if lay[x][y+c]=='Q':
                    print 'Level  passed'
                    flag=2
                    return
                if lay[x][y+c]=='C':
                    board.collectCoin()
                elif lay[x][y+c]=='O':
                    self.collision('fireball',player)
            lay[x][y]=' '
            if(player.bc==1):
                lay[x][y]='C'
                player.bc=0
            if(lay[x][y+c]=='C' and player.name!='P'):
                player.bc=1
            if(lay[x-1][y]=='H'):
                lay[x][y]='H'
            if(lay[x][y+c]!='O'):
                lay[x][y+c]=player.name
                player.Y+=c

    def moveUp(self,x,y,player):
        if(self.collision('up',player)==False):
            if(lay[x-1][y]=='Q'):
                os.system('clear')
                print 'Level passed!'
                flag=2
            if(player.bc==1):
                lay[x][y]='C'
                player.bc=0
            if(player.ld==1):
                lay[x][y]='H'
                player.ld=0

            if(lay[x-1][y]=='C'):
                if(player.name=='P'):
                    board.collectCoin()
                else:
                    player.bc=1
            else:
                lay[x][y]='H'
                lay[x-1][y]=player.name
            player.X-=1
    def moveDown(self,x,y,player):
        if(self.collision('down',player)==False):
            lay[x][y]='H'
            if(lay[x+1][y-1] in['H','X',' '] and lay[x+1][y+1] in['H','X']) or (lay[x+1][y-1] in ['H','X'] and lay[x+1][y+1] in['H','X',' ']):
                lay[x][y]=' '

            if player.bc==1:
                lay[x][y]='C'
                player.bc=0
            if player.ld==1:
                lay[x][y]='H'
                player.ld=0
            
            if(lay[x+1][y]=='C' and player.name!='P'):
                player.bc=1
            lay[x+1][y]=player.name
            player.X+=1

#################---------MOVING CHARACTERS-----------#############################

class Player(Move):
    def __init__(self):
        self.name='P'
        self.X,self.Y=HEIGHT-2,2
        self.bc=-2
        self.ld=0
        lay[self.X][self.Y]=self.name
class Donkey(Move):
    def __init__(self):
        self.name='D'
        self.X,self.Y=5,2
        self.bc=0
    def Dmove(self):
        global board,D
        x=random.randrange(2)
        y=0.8-0.05*(board.level-1)#donkey speed increase
        time.sleep(y)
        if(x==1 and self.collision('left',D)==False):
            self.move('a',D)
        elif(x==0 and self.collision('right',D)==False):
            self.move('d',D)

class Fireball(Move):
    def __init__(self,name,X,Y,dire,ball,bc,ld):
        self.name,self.X,self.Y,self.dire,self.ball,self.bc,self.ld=name,X,Y,dire,ball,bc,ld
    def move1(self,obj):
        global f,ball,D,Move
        if(lay[self.X+1][self.Y]=='O'and lay[self.X+2][self.Y]!=' '):#if fireball underneath(not stuck) wait for turn
            return
        if(self.ball==1):
            self.dire='d'
        else:
            self.dire='a'
        if(lay[self.X][self.Y+self.ball] in ['X','O','D'] or lay[self.X+1][self.Y+self.ball]==' '):
            self.ball=-1*self.ball
            if(lay[self.X][self.Y+self.ball]=='O' and lay[self.X+1][self.Y+self.ball]==['O','H']):
                return
        if(lay[self.X+1][self.Y] in ['O','H','P']):
            obj.dire='s'
            if(lay[self.X+1][self.Y]=='P'):
                f=[self.X+1,self.Y]
            if(lay[self.X+1][self.Y-1]=='X' or lay[self.X+1][self.Y+1]=='X') and (lay[self.X+2][self.Y] in[' ','X']):#spaceadded
                z=random.randint(3,4)
                if lay[self.X-1][self.Y]=='H':#put H back
                    lay[self.X][self.Y]='H'
                if z==3:
                    obj.dire='a'
                if z==4:
                    obj.dire='d'
        self.move(self.dire,obj)

##########------SCREEN--------###########
D=Donkey()
P=Player()
board=Board()
board.coins()
board.printLay()
Dum = Move()    

if __name__ == "__main__":
    os.system('clear')
    #os.system('clear')

    print colored("------DONKEY KONG -----",'cyan',attrs=['reverse'])
    print '\n',colored("Instructions:Press",'green',attrs=['bold','underline']),'\n'
    print colored('a: move left          ','yellow','on_blue')
    print colored('d: move right         ','blue','on_yellow')
    print colored("w: move up            ",'yellow','on_blue')
    print colored("s: move down          ",'blue','on_yellow')
    print colored("space + d: jump right ",'yellow','on_blue')
    print colored("space + a: jump left  ",'blue','on_yellow')
    print colored("space + w: jump up    ",'yellow','on_blue')
    print colored("q: quit               ",'blue','on_yellow')
    print colored("k: Okay!              ",'yellow','on_blue'),'\n','\n'

    os.system("stty cbreak -echo")
    x=sys.stdin.read(1)
    os.system("stty -cbreak -echo")
    os.system('clear')
    flag=2
    def func1():
        global board,flag,P
        while flag!=0: 
            if flag==2:
                board.level+=1
                board.cc,board.fb=0,0  
                board.layout()
                board.coins()
                print '\n',colored('Level: ','magenta'),board.level
                print colored('Enter any key to begin','magenta'),'\n'
                os.system("stty cbreak -echo")
                x=sys.stdin.read(1)
                os.system("stty -cbreak -echo")
                os.system('clear')
                flag=1
            board.printLay()       
            os.system("stty cbreak -echo")
            x=sys.stdin.read(1)
            os.system("stty -cbreak -echo")
            P.move(x,P) 
            if x=='q':
                flag=0
            if (board.lives==0):
                os.system('clear')
                print colored("------------YOU LOSE!--------------",'red')
                print colored("-------Final Score is:",'red'),colored(board.coincount,'red'),colored("---------",'red')
                flag=0
    def func2():
        global fb,flag,F,D,board
        count,dire=0,0
        while flag!=0:
            if count%15==0:
                if(count%2==0):
                    dire='d'
                else:
                    dire='a'
                fb.append(Fireball('O',D.X,D.Y+1,dire,1,0,0))
            D.Dmove()
            count+=1
            board.printLay()
    def func3():
        global fb,flag,F,D,board
        x,rem=0,[]
        while flag!=0:
            if(x<0):
                x=0.05
            x=0.2-0.01*(board.level-1)#move faster when level gets higher
            time.sleep(x) 
            for i in range(len(fb)):
                end=0
                ob=fb[i]
                ob.move1(ob)
                temp=ob
                fb.pop(i)
                fb.append(temp)
                if temp.X==HEIGHT-2 and temp.Y in [1,2,3]:
                    rem.append(ob)
            for i in range(len(rem)):
                lay[HEIGHT-2][rem[i].Y]=' '
                try:
                    fb.remove(rem[i])
                except:
                    pass
            rem=[]
            board.printLay()
    t1=Thread(target=func1)
    t2=Thread(target=func2)
    t3=Thread(target=func3)
    t1.start()
    t2.start()
    t3.start()
