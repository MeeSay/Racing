import pygame, pygame_menu,sys,os,minigame,time,turtle	
#from pygame_menu import *	
from minigame import *	
#from random import *	
#from os.path import *	
from sys import exit	
from pygame.locals import *	
from animate import *	
pygame.init()	
infoObject = pygame.display.Info()	
surface = pygame.display.set_mode((1024,576), pygame.RESIZABLE | pygame.SCALED)	
vat_pham_phu_kien=[]	
dang_kich_hoat=[]	
'''	
Dong 1 la noi de chu thich phu kieen dang luu, 0 la de bieu thi van chua mua phu kien do	
Dong 2 la cai nao dang kich hoat	
'''	
gia_sp=[99999] # biến lưu giá sản phẩm, không cần thiết nhưng chỉ tạm lưu đây thôi	
kho_bua=[["spd***",99]]	
'''	
Cac bua luu vao vi tri phim so	
[0]: bùa SPD***	
'''	
bua=["spd***"," "," "," "," "," "," "," "," ",]	
# Lưu bùa đã mua	
#khai bao bien, mau sac	
bg_choice="background1.jpg"	
map_size="long"	
setnv="setnv1"	
setnv_ver="original"	
Tien = 0	
youwin = False	
white = pygame.Color(255,255,255)	
black = pygame.Color(0,0,0)	
blue = pygame.Color(0,0,255)	
green = pygame.Color(0,255,0)	
red = pygame.Color(255,0,0)		
hien = 1	
_dichden = None #biến đích đến của xe	
f = open('user.txt','r')
#Tien = int (f.read())
with open('user.txt') as file:
        noi_dung_file = file.readlines()
#Luu = noi_dung_file[0]
Tien = int( noi_dung_file[0])
Tienthang = None		
thang_thua = 1	
xe_chon=[1,0,0,0,0] # xe nào được chọn thì số thứ đó sẽ = 1	
m_index=0 #THIS	
Rankcuaban = None	
class player:	
    name='Player'	
    def create(value):	
        global name	
        player.name=value	
    money=100000	
    	
class label:	
    #help=	
    '''Nhap huong dan su dung cho phan help tai day!'''    	
def bat_dau():	
    background = load_image(os.path.join("images","bg",map_size,bg_choice)).convert() # Map chọn để đua	
    cnt_321=1 # dùng để chạy các lệnh ban đầu 1 lần	
    global rank12345 # khi có một xe nào về đích rồi thì nó sẽ lấy thứ hạng từ biến này rồi sau đó tăng lên một đơn vị	
    rank12345=1	
    #----------set setnv theo phụ kiện------------#	
    def check_setnv():	
        global setnv	
        #setnv="setnv1"	
        global setnv_ver	
        #setnv_ver="original"	
        i=0	
        while i<len(dang_kich_hoat):	
            if (dang_kich_hoat[i]=="saodo" and setnv=="setnv1" 	
                or dang_kich_hoat[i]=="mask" and setnv=="setnv1"):	
                setnv_ver="mod1"	
            i+=1	
    check_setnv()	
    #____________________________________________	
    pygame.mixer.music.unload()	
    pygame.mixer.music.load('race_music.mp3')	
    pygame.mixer.music.play(loops=0, start=0.0, fade_ms = 0)	
    	
    bualoi=load_image(os.path.join("images","bua","box.png")).convert_alpha()	
    loai_bua="up.png"	
    hieuung_bua=load_image(os.path.join("images","bua",loai_bua)).convert_alpha()	
    class racer1:	
        name="Xe Cam"	
        rank=None	
        	
        # Thêm ảnh cho xe động đậy	
        img_data=[]	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"orange","racer1.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"orange","racer2.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"orange","racer3.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"orange","racer4.png")).convert_alpha())	
        # Dữ liệu bùa	
        bua_pos=[]	
        bua_effect=[]	
        index2=0 # dùng truy cập vị trí bùa khi kích hoạt bùa	
        allow_runtime_turn=0	
        	
        #	
        index=0	
        img=img_data[index] # gán ảnh	
        img2=img.copy()	
        spd=randrange(2,5)                                 # tốc độ	
        xy=img.get_rect()	
        temprect=xy	
        xy=xy.move(0,285)                          # tọa độ ban đầu của xe	
        xy2=xy.copy()	
        step=0                                        # số bước xe đã đi	
        choose=xe_chon[0]                                # xe có phải là xe đặt cược?	
        #	
        turn=0 # luợt dùng cho các hàm bùa	
        	
    class racer2:	
        name="Xe Vàng"	
        rank=None	
        	
        img_data=[]	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"yellow","racer1.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"yellow","racer2.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"yellow","racer3.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"yellow","racer4.png")).convert_alpha())	
        # Dữ liệu bùa	
        bua_pos=[]	
        bua_effect=[]	
        index2=0 # dùng truy cập vị trí bùa khi kích hoạt bùa	
        allow_runtime_turn=0	
        #	
        index=0	
        img=img_data[index] # gán ảnh	
        img2=img.copy()	
        spd=randrange(2,5)    	
        xy=img.get_rect()	
        temprect=xy	
        xy=xy.move(0,345)	
        xy2=xy.copy()	
        step=0	
        choose=xe_chon[1]	
        #	
        turn=0 # luợt dùng cho các hàm bùa	
        	
    class racer3:	
        name="Xe Xanh Lá"	
        rank=None	
        	
        img_data=[]	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"green","racer1.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"green","racer2.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"green","racer3.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"green","racer4.png")).convert_alpha())	
        # Dữ liệu bùa	
        bua_pos=[]	
        bua_effect=[]	
        index2=0 # dùng truy cập vị trí bùa khi kích hoạt bùa	
        allow_runtime_turn=0	
        #	
        index=0	
        img=img_data[index] # gán ảnh	
        img2=img.copy()	
        spd=randrange(2,5)     	
        xy=img.get_rect()	
        temprect=xy	
        xy=xy.move(0,405)	
        xy2=xy.copy()	
        step=0	
        choose=xe_chon[2]	
        #	
        turn=0 # luợt dùng cho các hàm bùa	
        	
        	
    class racer4:	
        name="Xe Xanh Dương"	
        rank=None	
        	
        img_data=[]	
        	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"blue","racer1.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"blue","racer2.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"blue","racer3.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"blue","racer4.png")).convert_alpha())	
        # Dữ liệu bùa	
        bua_pos=[] # Lưu vị trí xuất hiện các bùa trên trục tung, trục hoành là vị trí đường đua của xe vd với xe 1 thì đó là xy[1]=465	
        bua_effect=[]	
        index2=0 # dùng truy cập vị trí bùa khi kích hoạt bùa	
        allow_runtime_turn=0	
        	
        #	
        index=0	
        img=img_data[index] # gán ảnh	
        img2=img.copy()	
        spd=randrange(2,5)      	
        xy=img.get_rect()	
        temprect=xy	
        xy=xy.move(0,465)	
        xy2=xy.copy()	
        step=0	
        choose=xe_chon[3]	
        #	
        turn=0 # luợt dùng cho các hàm bùa	
        	
    class racer5:	
        name="Xe Tím"	
        rank=None	
        	
        img_data=[]	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"purple","racer1.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"purple","racer2.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"purple","racer3.png")).convert_alpha())	
        img_data.append(load_image(os.path.join("images",setnv,setnv_ver,"purple","racer4.png")).convert_alpha())	
        # Dữ liệu bùa	
        bua_pos=[]	
        bua_effect=[]	
        index2=0 # dùng truy cập vị trí bùa khi kích hoạt bùa	
        allow_runtime_turn=0	
        #	
        index=0	
        img=img_data[index] # gán ảnh	
        img2=img.copy()	
        spd=randrange(2,5)        	
        xy=img.get_rect()	
        temprect=xy	
        xy=xy.move(0,519)	
        xy2=xy.copy()	
        step=0	
        choose=xe_chon[4]	
        #	
        turn=0 # luợt dùng cho các hàm bùa	
        	
    # hàm đếm ngược trước khi đua	
    def dem_nguoc_321():	
        pygame.time.delay(600)	
        img_123=load_image(os.path.join("images","321","3.png"))	
        surface.blit(img_123,(infoObject.current_w/2-512    # 150 là nửa kích thước hình	
                              ,infoObject.current_h/2-265))	
        pygame.display.update()	
        pygame.time.delay(500)	
        img_123=load_image(os.path.join("images","321","2.png"))	
        surface.blit(img_123,(infoObject.current_w/2-512	
                              ,infoObject.current_h/2-265))	
        pygame.display.update()	
        pygame.time.delay(500)	
        img_123=load_image(os.path.join("images","321","1.png"))	
        surface.blit(img_123,(infoObject.current_w/2-512	
                              ,infoObject.current_h/2-253))	
        pygame.display.update()	
        pygame.time.delay(500)	
        img_123=load_image(os.path.join("images","321","START.png"))	
        surface.blit(img_123,(infoObject.current_w/2-512	
                              ,infoObject.current_h/2-253))	
        pygame.display.update()	
        pygame.time.delay(500)	
        pass	
    # hàm tạo bùa	
    def generate_bua(self):	
        so_bua=randrange(0,5)	
        dem=0	
        while dem<=so_bua:	
            self.bua_pos.append(randrange(177,_dichden))	
            self.bua_effect.append(generate_effect())	
            dem+=1	
        self.bua_pos.sort()	
    # hàm hình ảnh khi có hiệu ứng của bùa	
    def effect_bua(self):	
        if(self.choose==1):	
            tieng_bua()	
            surface.blit(pygame.transform.scale(hieuung_bua,(54,54)),(self.xy[0],(self.xy[1]-54)))	
            pass	
    # hàm tạo lõi (hiệu ứng) cho bùa	
    def generate_effect():	
        x=randrange(1,6)	
        if(x==1):	
            return "tangtoc"	
        if(x==2):	
            return "tangtocS"	
        if(x==3):	
            return "tangtocL"	
        if(x==4):	
            return "giamtoc"	
        if(x==5):	
            return "giamtocS"	
        if(x==6):	
            return "giamtocL"	
        pass	
    	
    # reset bùa	
    # kích hoạt bùa	
    def kich_hoat_bua(self):	
        ten_bua=self.bua_effect[self.index2]	
        	
        if(ten_bua=="tangtoc" or ten_bua=="tangtocS" or ten_bua=="tangtocL"):	
            tang_toc(self)	
        if(ten_bua=="giamtoc" or ten_bua=="giamtocS" or ten_bua=="giamtocL"):	
            giam_toc(self)	
        	
    # tiếng nhận bùa	
    def tieng_bua():	
        keng=pygame.mixer.Sound(os.path.join("SE","bua.mp3"))	
        pygame.mixer.Sound.play(keng)	
    def phim_bua():	
        if pygame.key.get_pressed()[K_1]:	
            if(racer1.choose==1):	
                tang_toc(racer1)	
                effect_bua(racer1)	
            if(racer2.choose==1):	
                tang_toc(racer2)	
                effect_bua(racer2)	
            if(racer3.choose==1):	
                tang_toc(racer3)	
                effect_bua(racer3)	
            if(racer4.choose==1):	
                tang_toc(racer4)	
                effect_bua(racer4)	
            if(racer5.choose==1):	
                tang_toc(racer5)	
                effect_bua(racer5)	
    	
    ''' Các hàm bùa viết ở đây'''	
    def tang_toc(self):	
        self.spd+=2	
        self.allow_runtime_turn=1	
    def giam_toc(self):	
        if(self.spd-2>0):	
            self.spd-=2	
            self.allow_runtime_turn=1	
        else:	
            pass	
            # thêm biểu tượng no effect	
        	
    ''''''''''''''''''''''''''''''	
    # vị trí camera ban đầu	
    class bg:	
        x=0	
        y=0	
    # dịch camera theo xe đã đặt cược theo tốc độ của xe	
    def dich_camera_x(huong,self):	
        if huong=='phai':	
            #bg.x-=self.spd	
            racer1.xy[0]-=self.spd	
            racer2.xy[0]-=self.spd	
            racer3.xy[0]-=self.spd	
            racer4.xy[0]-=self.spd	
            racer5.xy[0]-=self.spd	
        if huong=='trai':	
            bg.x+=self.spd	
            racer1.xy[0]+=self.spd	
            racer2.xy[0]+=self.spd	
            racer3.xy[0]+=self.spd	
            racer4.xy[0]+=self.spd	
            racer5.xy[0]+=self.spd	
    def dich_camera_y(huong,self):	
        if huong=='len':	
            bg.y+=self.spd	
            racer1.xy[1]+=self.spd	
            racer2.xy[1]+=self.spd	
            racer3.xy[1]+=self.spd	
            racer4.xy[1]+=self.spd	
            racer5.xy[1]+=self.spd	
        if huong=='xuong':	
            bg.y-=self.spd	
            racer1.xy[1]-=self.spd	
            racer2.xy[1]-=self.spd	
            racer3.xy[1]-=self.spd	
            racer4.xy[1]-=self.spd	
            racer5.xy[1]-=self.spd	
    # cac ham di chuyen xe theo toc do	
    def ngang_phai(self):	
        self.step+=self.spd              # cộng vào quãng đường mỗi vận tốc trên giây đi được	
        self.xy=self.xy.move(self.spd,0) # dịch xe theo tốc độ của xe	
        #if self.choose==1 and self.step<_dichden-400: #khúc sau của câu lệnh nhằm không để camera lọt ngoài tầm	
            #dich_camera_x('phai',self)	
    def chay_xe(self):	
        pass	
        if (self.step<_dichden):	
            ngang_phai(self)	
        global rank12345	
        if(self.rank==None and self.step>=_dichden): # Nếu xe đã đến đích rồi thì code sẽ lưu thứ hạng vào self.rank	
            self.rank=rank12345	
            rank12345+=1	
        	
        if(self.index2<len(self.bua_pos)):	
            if(self.xy[0]>=self.bua_pos[self.index2]):	
                kich_hoat_bua(self)	
                effect_bua(self)	
                self.index2+=1	
                self.bua_pos[self.index2-1]=-51 # -51 tức là vứt nó ra khỏi màn hình	
    	
        	
    def hien_xe(self):	
        self.xy2 = self.xy.copy()	
        self.xy2 = (self.xy2[0],self.xy2[1])	
        surface.blit(self.img2,self.xy2)	
    def img_update(self): # thay ảnh theo từng lượt (tạo cảm giác như ảnh chuyển động)	
        self.index=self.index+1	
        if (self.index==len(self.img_data)):	
            self.index=0                     	
        self.img2=self.img_data[self.index]	
    def nam_chiec_xe():	
        img_update(racer1)	
        img_update(racer2)	
        img_update(racer3)	
        img_update(racer4)	
        img_update(racer5)	
        	
        hien_xe(racer1)	
        hien_xe(racer2)	
        hien_xe(racer3)	
        hien_xe(racer4)	
        hien_xe(racer5)	
        	
        chay_xe(racer1)	
        chay_xe(racer2)	
        chay_xe(racer3)	
        chay_xe(racer4)	
        chay_xe(racer5)	
    # Vẽ bùa lên màn hình game	
    # 50 LA KICH THUOC CUA BUA, TEAM DESIGN THIET KE BUA ROI THI NHO SUA CODE LAI	
    def ve_bua():	
        dem=0	
        while(dem<len(racer1.bua_pos)):	
            surface.blit(pygame.transform.scale(bualoi,	
                                               (25,25))	
                                                ,(racer1.bua_pos[dem],racer1.xy[1]+10))	
            dem+=1	
        dem=0	
        while(dem<len(racer2.bua_pos)):	
            surface.blit(pygame.transform.scale(bualoi,	
                                               (25,25))	
                                                ,(racer2.bua_pos[dem],racer2.xy[1]+10))	
            dem+=1	
        dem=0	
        while(dem<len(racer3.bua_pos)):	
            surface.blit(pygame.transform.scale(bualoi,	
                                               (25,25))	
                                                ,(racer3.bua_pos[dem],racer3.xy[1]+10))	
            dem+=1	
        dem=0	
        while(dem<len(racer4.bua_pos)):	
            surface.blit(pygame.transform.scale(bualoi,	
                                               (25,25))	
                                                ,(racer4.bua_pos[dem],racer4.xy[1]+10))	
            dem+=1	
        dem=0	
        while(dem<len(racer5.bua_pos)):	
            surface.blit(pygame.transform.scale(bualoi,	
                                               (25,25))	
                                                ,(racer5.bua_pos[dem],racer5.xy[1]+10))	
            dem+=1	
        	
    	
        	
    #vvvvv các hàm xử lý lượt khi game chạy vvvvv	
    def car_turn(self):	
        if(self.index2>=1):	
            	
            if(self.bua_effect[self.index2-1]=="tangtoc"):	
                if(self.allow_runtime_turn==1):	
                    #if(self.turn>=0):	
                    self.turn+=1	
                    if(self.turn==10):	
                        self.spd-=2	
                        self.turn=0	
                        self.allow_runtime_turn=0	
            if(self.bua_effect[self.index2-1]=="tangtocS"):	
                if(self.allow_runtime_turn==1):	
                    #if(self.turn>=0):	
                    self.turn+=1	
                    if(self.turn==5):	
                        self.spd-=2	
                        self.turn=0	
                        self.allow_runtime_turn=0	
            if(self.bua_effect[self.index2-1]=="tangtocL"):	
                if(self.allow_runtime_turn==1):	
                    #if(self.turn>=0):	
                    self.turn+=1	
                    if(self.turn==15):	
                        self.spd-=2	
                        self.turn=0	
                        self.allow_runtime_turn=0	
            if(self.bua_effect[self.index2-1]=="giamtoc"):	
                if(self.allow_runtime_turn==1):	
                    #if(self.turn>=0):	
                    self.turn+=1	
                    if(self.turn==10):	
                        self.spd+=2	
                        self.turn=0	
                        self.allow_runtime_turn=0	
            if(self.bua_effect[self.index2-1]=="giamtocS"):	
                if(self.allow_runtime_turn==1):	
                    #if(self.turn>=0):	
                    self.turn+=1	
                    if(self.turn==5):	
                        self.spd+=2	
                        self.turn=0	
                        self.allow_runtime_turn=0	
            if(self.bua_effect[self.index2-1]=="giamtocL"):	
                if(self.allow_runtime_turn==1):	
                    #if(self.turn>=0):	
                    self.turn+=1	
                    if(self.turn==15):	
                        self.spd+=2	
                        self.turn=0	
                        self.allow_runtime_turn=0	
            ''' viết tiếp các lệnh reset khác tại đây'''	
    def runtime_turn():	
        car_turn(racer1)	
        car_turn(racer2)	
        car_turn(racer3)	
        car_turn(racer4)	
        car_turn(racer5)	
        	
    #^^^^^^ các hàm xử lý lượt khi game chạy ^^^^^^^^	
    def show_quang_duong(hien = 1):	
        def duong(self):    	
            dfont = pygame.font.SysFont('consolas',20)	
            dtext=str(self.name)+':'+str(self.step)	
            qduong = dfont.render(dtext,True,blue)	
            if(self.step>=_dichden):	
                qduong = dfont.render("Về đích",True,green)	
            drect = qduong.get_rect()	
            if (hien == 1):	
                if self.name==racer1.name:	
                    drect.midtop = (850,10)	
                if self.name==racer2.name:	
                    drect.midtop = (850,30)	
                if self.name==racer3.name:	
                    drect.midtop = (850,50)	
                if self.name==racer4.name:	
                    drect.midtop = (850,70)	
                if self.name==racer5.name:	
                    drect.midtop = (850,90)	
                surface.blit(qduong,drect)	
        duong(racer1)	
        duong(racer2)	
        duong(racer3)	
        duong(racer4)	
        duong(racer5)	
    def show_bua(hien = 1):	
        def so_bua(index):    	
            bfont = pygame.font.SysFont('consolas',12)	
            sfont = pygame.font.SysFont('consolas',8)	
            ten = bfont.render(kho_bua[index][0],True,blue)	
            sll = bfont.render(str(kho_bua[index][1]),True,red)	
            key = bfont.render("=="+str(index+1)+"==",True,green)	
            rect_ten = ten.get_rect()	
            rect_sll = sll.get_rect()	
            rect_key = key.get_rect()	
            if (hien == 1):	
                rect_ten.topleft = (index*50,0)	
                rect_sll.topleft = (index*50,20)	
                rect_key.topleft = (index*50,40)	
                surface.blit(ten,rect_ten)	
                surface.blit(sll,rect_sll)	
                surface.blit(key,rect_key)	
        so_bua(0)	
    def rank_cua_ban(self):	
        if self.choose == 1:	
            global Rankcuaban	
            Rankcuaban = self.rank	
        	
            	
#--------------------------------------main------------------------------#	
    	
    while True:	
        pygame.event.pump()	
        infoObject = pygame.display.Info()	
        nut_an= pygame.key.get_pressed()	
        	
        runtime_turn()	
        phim_bua()	
                	
        for event in pygame.event.get():	
            if (event.type == pygame.QUIT):	
                pygame.quit()	
                exit()	
            elif pygame.key.get_pressed()[K_ESCAPE]:	
                pygame.mixer.music.unload()	
                return False	
                sys.exit()	
                	
        '''	
        execute_bua(racer1) #chạy bùa trong khi đang thực hiện chương trình	
        execute_bua(racer2)	
        execute_bua(racer3)	
        execute_bua(racer4)	
        execute_bua(racer5)	
        '''	
        surface.blit(pygame.transform.scale(background, (infoObject.current_w, infoObject.current_h)), (bg.x, bg.y))	
        ve_bua()	
        nam_chiec_xe() # hien hinh anh xe va cho chay xe    	
        pygame.time.delay(35) # tu dieu chinh theo y muon	
        show_quang_duong() # hien thi quang duong xe dua dc	
        show_bua() # hien thi cac bua co the dung duoc	
        pygame.display.update()	
        	
        	
        	
        if(cnt_321==1): # thực hiện các lệnh chỉ một lệnh duy nhất	
            pass	
            generate_bua(racer1)	
            generate_bua(racer2)	
            generate_bua(racer3)	
            generate_bua(racer4)	
            generate_bua(racer5)	
            dem_nguoc_321()	
            cnt_321=0	
        	
        	
        if(rank12345==6):	
            def bao_thang_thua(self):    	
                if self.choose == 1 and self.rank ==1:	
                    sfont = pygame.font.SysFont('consolas',100)	
                    ssurf = sfont.render('YOU WIN!',True,red)	
                    srect = ssurf.get_rect()	
                    if cnt_321 == 0: 	
                        srect.midtop = (500,250)	
                    surface.blit(ssurf,srect)	
                    	
                    rfont = pygame.font.SysFont('consolas',40)	
                    rsurf = rfont.render('Tiền thắng: {0}'.format(Tienthang),True,red)	
                    rrect = rsurf.get_rect()	
                    if cnt_321 == 0:	
                        rrect.midtop = (500,350)	
                    surface.blit(rsurf,rrect)	
                    global thang_thua	
                    thang_thua = 1	
                    Tinh_tien()	
                    	
                    tfont = pygame.font.SysFont('consolas',40)	
                    tsurf = tfont.render('Tổng tiền hiện có: {0}'.format(Tien),True,red)	
                    trect = tsurf.get_rect()	
                    if cnt_321 == 0:	
                        trect.midtop = (500,400)	
                    surface.blit(tsurf,trect)	
                    	
                    hfont = pygame.font.SysFont('consolas',40)	
                    hsurf = hfont.render('Rank của bạn là: {0}'.format(Rankcuaban),True,red)	
                    hrect = hsurf.get_rect()	
                    if cnt_321 == 0:	
                        hrect.midtop = (500,450)	
                    surface.blit(hsurf,hrect)	
                    	
                    pygame.display.flip()	
                if self.choose == 1 and self.rank > 1:	
                    sfont = pygame.font.SysFont('consolas',100)	
                    ssurf = sfont.render('YOU LOSE!',True,red)	
                    srect = ssurf.get_rect()	
                    if cnt_321 == 0:	
                        srect.midtop = (500,250)	
                    surface.blit(ssurf,srect)	
                    	
                    rfont = pygame.font.SysFont('consolas',40)	
                    rsurf = rfont.render('Tiền thua: {0}'.format(Tienthang),True,red)	
                    rrect = rsurf.get_rect()	
                    if cnt_321 == 0:	
                        rrect.midtop = (500,350)	
                    surface.blit(rsurf,rrect)	
                    	
                    thang_thua = 0	
                    Tinh_tien()	
                    	
                    tfont = pygame.font.SysFont('consolas',40)	
                    tsurf = rfont.render('Tổng tiền hiện có: {0}'.format(Tien),True,red)	
                    trect = tsurf.get_rect()	
                    if cnt_321 == 0:	
                        trect.midtop = (500,400)	
                    surface.blit(tsurf,trect)	
                    	
                    hfont = pygame.font.SysFont('consolas',40)	
                    hsurf = hfont.render('Rank của bạn là: {0} (T.T)'.format(Rankcuaban),True,red)	
                    hrect = hsurf.get_rect()	
                    if cnt_321 == 0:	
                        hrect.midtop = (500,450)	
                    surface.blit(hsurf,hrect)	
                    	
                    pygame.display.flip()	
            rank_cua_ban(racer1)	
            rank_cua_ban(racer2)	
            rank_cua_ban(racer3)	
            rank_cua_ban(racer4)	
            rank_cua_ban(racer5)	
            bao_thang_thua(racer1)	
            bao_thang_thua(racer2)	
            bao_thang_thua(racer3)	
            bao_thang_thua(racer4)	
            bao_thang_thua(racer5)	
            	
            time.sleep(5)	
            pygame.mixer.music.unload()	
            return False	
            sys.exit()	
        pygame.display.update()    	
    #-----------------mini game--------------------------------------------------------#	
def minigame1():	
    shuffle(cau_hoi)	
    menu.clear()	
    menu.add_label("Luật chơi: ",max_char=-1)	
    menu.add_label(luat_choi,max_char=-1)	
    menu.add_button('Bắt đầu',minigame2)	
    menu.add_button('Quay lại',chuan_bi)	
def minigame2():	
    het_cau_hoi()	
    menu.clear()	
    menu.add_label(cau_hoi[m_index][0], max_char=-1)	
    menu.add_button(cau_hoi[m_index][1],dap_an_A)	
    menu.add_button(cau_hoi[m_index][2],dap_an_B)	
    menu.add_button(cau_hoi[m_index][3],dap_an_C)	
    menu.add_button(cau_hoi[m_index][4],dap_an_D)	
    pass	
def het_cau_hoi():	
    if(m_index==len(cau_hoi)):	
        cau_hoi.append(["Đã hết câu hỏi",'Ok',' ',' ',' ',0])	
def dap_an_dung():	
    #viết thêm code để cộng tiền 	
    menu.clear()	
    menu.add_label("Chính xác!")	
    menu.add_button('OK',minigame2)	
def dap_an_sai():	
    menu.clear()	
    menu.add_label("Rất tiếc đáp án của bạn đã sai rồi :(.")	
    menu.add_button('OK',chuan_bi)	
def dap_an_A():	
    global m_index	
    if(cau_hoi[m_index][5]==1):	
        m_index+=1	
        dap_an_dung()	
    else:	
        dap_an_sai()	
def dap_an_B():	
    global m_index	
    if(cau_hoi[m_index][5]==2):	
        m_index+=1	
        dap_an_dung()	
    else:	
        dap_an_sai()	
def dap_an_C():	
    global m_index	
    if(cau_hoi[m_index][5]==3):	
        m_index+=1	
        dap_an_dung()	
    else:	
        dap_an_sai()	
def dap_an_D():	
    global m_index	
    if(cau_hoi[m_index][5]==4):	
        m_index+=1	
        dap_an_dung()	
    else:	
        dap_an_sai()	
    #--------------kiểm tra đủ tiền mua sp ko----------------------------#	
def check_gia_sp_bua(self):	
    global Tien	
    if(Tien-self<0):	
        menu.clear()	
        menu.add_label("Không đủ tiền.")	
        menu.add_button('OK',bua)	
    else:	
        Tien-=self	
def check_gia_sp_pk(self):	
    global Tien	
    if(Tien-self<0):	
        menu.clear()	
        menu.add_label("Không đủ tiền.")	
        menu.add_button('OK',phu_kien)	
    else:	
        Tien-=self	
    #-----------phu kien-----------------------------------------------------#	
def phu_kien():	
    #------------ hàm kiểm tra vật phẩm chung -------------#	
    def check_vp(self):	
        global vat_pham_phu_kien	
        i=0	
        while i<len(vat_pham_phu_kien):	
            if vat_pham_phu_kien[i]==self:	
                return 1	
            i+=1	
        return 0	
    #______________________________________________________#	
    def sao_do():	
        def ap_dung():	
            global dang_kich_hoat	
            dang_kich_hoat.append("saodo")	
            phu_kien()	
        def mua():	
            check_gia_sp_pk(gia_sp[0])	
            global vat_pham_phu_kien	
            vat_pham_phu_kien.append("saodo")	
            sao_do()	
        menu.clear()	
        if(check_vp("saodo")==0):	
            menu.add_label("San pham nay co gia")	
            menu.add_label(gia_sp[0])	
            menu.add_label("Bạn có muốn mua sản phẩm này không?")	
            menu.add_button('Có',mua)	
            menu.add_button('Không',phu_kien)	
        if(check_vp("saodo")==1):	
            menu.add_label("Bạn có muốn áp dụng không?")	
            menu.add_button('Có', ap_dung)	
            menu.add_button('Không',phu_kien)	
    def mask():	
        def ap_dung():	
            global dang_kich_hoat	
            dang_kich_hoat.append("mask")	
            phu_kien()	
        def mua():	
            global vat_pham_phu_kien	
            vat_pham_phu_kien.append("mask")	
            mask()	
        menu.clear()	
        if(check_vp("mask")==0):	
            menu.add_label("San pham nay co gia")	
            menu.add_label(gia_sp[0])	
            menu.add_label("Bạn có muốn mua sản phẩm này không?")	
            menu.add_button('Có',mua)	
            menu.add_button('Không',phu_kien)	
        if(check_vp("mask")==1):	
            menu.add_label("Bạn có muốn áp dụng không?")	
            menu.add_button('Có', ap_dung)	
            menu.add_button('Không',phu_kien)	
    #--------------------- hàm reset setnv ---------------------------#	
    def reset_nhanvat(self):	
        i=0	
        global dang_kich_hoat	
        while i<len(dang_kich_hoat):	
            if self==dang_kich_hoat[i]:	
                dang_kich_hoat[i]=0	
            i+=1	
    #_________________________________________________________________#	
    def reset_setnv1():	
        def ap_dung():	
            reset_nhanvat("saodo")	
            #thiếu	
            phu_kien()	
        menu.clear()	
        menu.add_label("Bạn có reset lại set nhân vật xe đua không?")	
        menu.add_button('Có',ap_dung)	
        menu.add_button('Khônng',phu_kien)	
    def reset_setnv2():	
        def ap_dung():	
            #thiếu	
            phu_kien()	
        menu.clear()	
        menu.add_label("Bạn có reset lại set nhân vật mickey không?")	
        menu.add_button('Có',ap_dung)	
        menu.add_button('Khônng',phu_kien)	
    def reset_setnv3():	
        def ap_dung():	
            #thiếu	
            phu_kien()	
        menu.clear()	
        menu.add_label("Bạn có reset lại set nhân vật xe máy cày không?")	
        menu.add_button('Có',ap_dung)	
        menu.add_button('Khônng',phu_kien)	
    def reset_setnv4():	
        def ap_dung():	
            #thiếu	
            phu_kien()	
        menu.clear()	
        menu.add_label("Bạn có reset lại set nhân vật đĩa bay không?")	
        menu.add_button('Có',ap_dung)	
        menu.add_button('Khônng',phu_kien)	
    def reset_setnv5():	
        def ap_dung():	
            reset_nhanvat("mask")	
            phu_kien()	
        menu.clear()	
        menu.add_label("Bạn có reset lại set nhân vật sinh viên không?")	
        menu.add_button('Có',ap_dung)	
        menu.add_button('Khônng',phu_kien)	
        	
    	
    menu.clear()	
    menu.add_button('Sao đỏ cho xe đua',sao_do,align=pygame_menu.locals.ALIGN_LEFT)	
    menu.add_button('Khẩu trang cho sinh viên',mask,align=pygame_menu.locals.ALIGN_LEFT)	
    menu.add_button('Reset lại set nhân vật xe',reset_setnv1,align=pygame_menu.locals.ALIGN_LEFT)	
    menu.add_button('Reset lại set nhân vật sinh viên',reset_setnv5,align=pygame_menu.locals.ALIGN_LEFT)	
    menu.add_button('Quay lại',cua_hang,align=pygame_menu.locals.ALIGN_LEFT)	
    #----------------menu--------------------------------------------------------------#	
def chon_map(value,choice):	
    global bg_choice	
    bg_choice=choice	
    pass	
def chon_size(value,choice):	
    global map_size	
    map_size=choice	
    global _dichden	
    if(choice=="mid"):	
        _dichden=550	
    if(choice=="long"):	
        _dichden=935	
    if(choice=="short"):	
        _dichden=300	
    pass	
#----------------------------------    	
#def dat_cuoc(value,choice):	
    #if(choice == 10):	
        #global Tienthang	
        #Tienthang = Tien	
    #else:	
        #Tienthang = int(choice)*1000	
#-----------------------------
def dat_cuoc(value,choice):
    if(choice == 10):
        global Tienthang
        Tienthang = Tien
    elif(int(choice)*1000 >= Tien):
        Tienthang = Tien
    else:
        Tienthang = int(choice)*1000
#-------------------------------
def Tinh_tien():
        if thang_thua == 1:	
            global Tien	
            Tien = Tien + Tienthang	
        else:	
            Tien = Tien - Tienthang
def main_game():
    def reset_options():
        chon_map('Thành thị', "background1.jpg")
        chon_size('Dài [935]', "long")
        chon_xe('Cam', 1)
        chon_setnv('Xe XAEA-12', 1)
    
    menu.clear()
    reset_options()# reset lại cài đặt, không để lần sau chơi lấy cài đặt cũ như là "ngắn" dù màn hình tùy chọn là dài và tương tự
    menu.add_selector('Trường đua :', [('Thành thị', "background1.jpg"), ('Bãi biển', "background2.jpg"), ('Ngoài hành tinh', "background3.jpg"), ('Nhật Bản', "background4.jpg"), ('Nông thôn', "background5.jpg")], onchange=chon_map,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_selector('Kích thước :', [('Dài [935]', "long"), ('Trung bình[550]', "mid"), ('Ngắn[300]', "short")], onchange=chon_size,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_selector('Xe:', [('Cam', 1), ('Vàng', 2), ('Xanh lá', 3), ('Xanh dương',4), ('Tím',5)], onchange=chon_xe,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_selector('Set nhân vật:', [('Xe XAEA-12', 1), ('Mickey', 2), ('Xe máy cày', 3), ('UFO',4), ('Sinh viên',5)], onchange=chon_setnv,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_selector('Đặt cược', [('None',0),('1000', 1), ('2000', 2), ('5000', 5), ('10000',10), ('20000',20),('50000',50),('100000',100),('200000',200),('500000',500),('Toàn bộ',10)], onchange=dat_cuoc,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('OK',bat_dau,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Quay lai',chuan_bi,align=pygame_menu.locals.ALIGN_LEFT)
    pass
def show_tien(hien = 1):
    sfont = pygame.font.SysFont('consolas',40)
    ssurf = sfont.render('Tien: {0}'.format(Tien),True,red)
    srect = ssurf.get_rect()
    if hien == 1:
        srect.midtop = (850,40)
    else:
        srect.midtop = (460,288)
    surface.blit(ssurf,srect)
    
def chon_xe(xe,so):
    global xe_chon
    i=0
    while(i<5):
        xe_chon[i]=0
        i=i+1
    if(so==1):
        xe_chon[0]=1
    if(so==2):
        xe_chon[1]=1
    if(so==3):
        xe_chon[2]=1
    if(so==4):
        xe_chon[3]=1
    if(so==5):
        xe_chon[4]=1
    pass
def chon_setnv(set,so):
    global setnv
    if(so==1):
        setnv="setnv1"
    if(so==2):
        setnv="setnv2"
    if(so==3):
        setnv="setnv3"
    if(so==4):
        setnv="setnv4"
    if(so==5):
        setnv="setnv5"
    pass
def load_game():
    global Ten
    Ten = noi_dung_file[1]
    global Tien
    Tien = int(noi_dung_file[2])
    menu.clear()
    menu.add_label("Tên nhân vật: "+str(Ten),align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_label("Hiện có: "+str(Tien)+" VND",align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button("Ok",chuan_bi,align=pygame_menu.locals.ALIGN_LEFT)
    
    
def save_game():
    global noi_dung_file
    noi_dung_file[2] = str(Tien)
    file = open('user.txt','w')
    file.write(noi_dung_file[0])
    file.write(noi_dung_file[1])
    file.write(noi_dung_file[2])
    da_luu()
def da_luu():
    menu.clear()
    menu.add_label("Đã lưu!!!")
    menu.add_button('OK',chuan_bi)
        
def cua_hang():
    menu.clear()
    menu.add_label("Hiện có: "+str(Tien)+" VNĐ",align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Vòng quay bùa',bua,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Phụ kiện',phu_kien,align=pygame_menu.locals.ALIGN_LEFT)    
    menu.add_button('Quay lại',chuan_bi,align=pygame_menu.locals.ALIGN_LEFT)
def bua():
    def buaSPD1():
        def mua():
            menu.clear()
            global kho_bua
            kho_bua[0][1]+=1
            bua()
        
        menu.clear()
        menu.add_label("Tên: Bùa SPD***",align=pygame_menu.locals.ALIGN_LEFT)
        menu.add_label("Tác dụng tăng tốc trong khoảng thời gian ngắn",align=pygame_menu.locals.ALIGN_LEFT)
        menu.add_label("Rank: ***",align=pygame_menu.locals.ALIGN_LEFT)
        menu.add_label("Bạn có muốn mua bùa này?",align=pygame_menu.locals.ALIGN_LEFT)
        menu.add_button('Có',mua,align=pygame_menu.locals.ALIGN_LEFT)
        menu.add_button('Không',bua,align=pygame_menu.locals.ALIGN_LEFT)
    menu.clear()
    menu.add_label("Hiện có: "+str(Tien)+" VNĐ",align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Bùa SPD*',buaSPD1,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Quay lại',cua_hang,align=pygame_menu.locals.ALIGN_LEFT)
def chuan_bi():
    global m_index
    m_index=0
    menu.clear()
    menu.add_button('Bắt đầu',main_game,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_label("Hiện có: "+str(Tien)+" VNĐ",align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Cửa hàng',cua_hang,align=pygame_menu.locals.ALIGN_LEFT)    
    menu.add_button('Minigame',minigame1,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Lưu game',save_game,align=pygame_menu.locals.ALIGN_LEFT)
def luu_ten(value):
    global noi_dung_file
    noi_dung_file[1] = value+'\n'
    
def start_the_game():
    menu.clear()
    menu.add_text_input('Tên người chơi : ', default = ' ',onreturn=luu_ten,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Ok', chuan_bi,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Quay lại', main_menu,align=pygame_menu.locals.ALIGN_LEFT)
def help_game():
    menu.clear()
    menu.add_label("",max_char=-1,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Quay lại', main_menu,align=pygame_menu.locals.ALIGN_LEFT)
def main_menu():
    menu.clear()
    menu.add_button('Chơi mới', start_the_game,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Chơi tiếp', load_game,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Hướng dẫn', help_game,align=pygame_menu.locals.ALIGN_LEFT)
    menu.add_button('Thoát', pygame_menu.events.EXIT,align=pygame_menu.locals.ALIGN_LEFT)
mytheme=pygame_menu.themes.THEME_BLUE.copy()
myimage = pygame_menu.baseimage.BaseImage(
    image_path=os.path.join("images","main_menu.png"),
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)
mytheme.background_color = myimage
menu = pygame_menu.Menu(576, 1024, 'Đường đua bốc lửa', theme=mytheme)
main_menu()
menu.mainloop(surface)
pygame.display.flip()
