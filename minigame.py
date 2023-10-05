#import random
from random import *

luat_choi="Chọn các đáp án ABCD,"\
          "nếu đúng người chơi sẽ được phép chơi tiếp và nhận tiền thưởng cho mỗi câu hỏi,"\
          "nếu chọn sai sẽ phải chơi lại từ đầu."

cau_hoi=[]

cau_hoi.append(["World Cup 2018 được tổ chức ở nước nào?",'A.Nga','B.Brazil','C.Pháp','D.Đáp án khác',1])
cau_hoi.append(["Có một đàn vịt, cho biết 1 con đi trước thì có 2 con đi sau, 1 con đi sau thì có 2 con đi trước, 1 con đi giữa thì có 2 con đi 2 bên. Hỏi đàn vịt đó có mấy con?",'A.1','B.2','C.3','D.4',3])
cau_hoi.append(["Ở Việt Nam có 5% số người sử dụng điện thoại không có tên trong danh bạ điện thoại. Nếu ta lấy ngẫu nhiên 100 người trong danh bạ thì trung bình sẽ có bao nhiêu người không có số điện thoại.?",'A.0%','B.20%','C.50%','D.100%',1])
cau_hoi.append(["Số nào tiếp theo trong dãy: 210, 245, 320, 355, 430, 505, 540, 615?",'A.700','B.680','C.650','D.725',3])
cau_hoi.append(["Tìm số tiếp theo: 5948, 1412, 53",'A.15','B.6','C.9','D.đáp án khác',4])
cau_hoi.append(["Tìm số tiếp theo của dãy: 2, 3, 4, 6, 8, 11, 14, 18, 22, 27",'A.31','B.32','C.33','D.đáp án khác',2])


'''
Làm theo cú pháp để thêm câu hỏi
cau_hoi.append(["<Câu hỏi>",'A.<Đáp án>','B.<Đáp án>','C.<Đáp án>','D.<Đáp án>',<Đáp án đúng là đáp án thứ mấy từ 1-4>])

'''
