Chú ý: Nhớ nhấn nút để chuyển background trước khi nhấn bắt đầu chứ không thì nó sẽ bị lỗi.

//UPDATE:

16/12: 
~~+Đã gộp hai file menu và game lại vào test2.py.~~

Cập nhật file test3.py thay cho file test2.py. Ai làm thì dùng file này thay cho 3 file race/menu/test2.py nhé.

18/12:
Cập nhật lại file test3.py để khi resize không gặp lỗi. Cập nhật thêm file background.jpg.

20/12:
Fix được hoàn toàn lỗi resize của file test3.py!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Bổ sung library animate.py, library này cho phép thêm ảnh chuyển động được (animate), còn làm như thế nào thì chưa biết. Code của file test3.py hiện đang sử dụng hàm load_image của lib này (cho tiện)

Bổ sung nhạc khi chạy đua.

21/12:
Bổ sung thêm code để load liên tiếp ảnh. Bổ sung folder ảnh "racer" và thay đổi code để load ảnh từ đó, cập nhật file test3.py

22/12:
Bổ sung code để chọn được map. 

Thay đổi cấu trúc thư mục ảnh, từ giờ trở đi tất cả các file ảnh đều đưa vào thư mục "images", không sử dụng thư mục racer nữa.
23/12:
Lưu được thứ hạng xe đua trong từng biến self.rank (từ 1->5, self ở đây là các class racer1->5)

------------------------------------------------
Nhóm cài pygame, pygame-menu. 

>Đọc và tìm hiểu cách dùng qua https://pygame-menu.readthedocs.io/en/latest/ để làm menu và giao diện các thành phần cho game. 
>Cố gắng tìm hiểu sâu vào cách tạo giao diện qua pygame-menu.
>
>Nhóm code bổ sung các thành phần đã có ghi đỏ tên hàm vào code file main.py trên github. Trước tiên cứ tham khảo cách tạo menu trên file main.py đó.
>Cách đặt tên hàm, gói code vào hàm nào thì xem mấy chữ bôi đỏ ở các trang 4-6. Tiện thể việt hóa mấy cái nút luôn.
>
>Riêng nhóm design tìm hiểu tập trung vào hai trang https://pygame-menu.readthedocs.io/en/latest/_source/add_sounds.html, https://pygame-menu.readthedocs.io/en/latest/_source/themes.html, https://pygame-menu.readthedocs.io/en/latest/_source/add_widgets.html để chỉnh sửa giao diện và âm thanh ở màn hình giao diện menu.



#Cài và sử dụng pygame-menu
>Đặt biến môi trường để có thể sử dụng được pip của python, cách để làm sao có thể google
>(hoặc mở cmd, dùng lệnh set PATH=<tên thư mục để pip, ví dụ ở đây là D:\Python38\Scripts>
>
>cài pygame thông qua lệnh cmd: 
>  pip install pygame
>  
>cài pygame-menu thông qua lệnh:
>  pip install pygame-menu
>(nếu chưa được thì xem báo lỗi xem nó yêu cầu cài thêm cái gì, ví dụ như sphinx thì phải dùng lệnh pip install sphinx)

-----
Task: Hoàn thiện phần đã giao, bổ sung bùa.
nghĩa:
-thêm biểu tượng no effect
-quyết định xem có đổi background cho main menu hay không
-sửa lại hướng dẫn, bỏ cái giới thiệu trò chơi là gì đầu game đi, hướng dẫn chơi và chức năng game thôi, các phím ấn chức năng gì, làm sao cho nó ngắn gọn lại
long:
-bổ sung cho chức năng lưu/chơi tiếp
-nuke phần bùa đi để lại vòng quay thôi, hiện câu hỏi bạn muốn quay bùa ngẫu nhiên phải không, kết quả là 1 bùa ngẫu nhiên nào đó, sau đó hiện lựa chọn là chọn ô thứ mấy từ 1-9 để lưu bùa này, ô nào cài bùa rồi thì hiện câu hỏi muốn ghi đè hay ko
-tiếp tục phần đặt cược và tiền tệ, nhớ thêm chỗ để hiển thị số tiền của người chơi ở màn hình chọn xe và cửa hàng nữa
-add các nhạc còn thiếu
-bỏ cái hiển thị tiền trên màn hình đi, khi nào về đích thì hiển thị tiền gốc, tiền cược, số tiền có được sau khi cộng/trừ tiền cược
-hiển thị thứ hạng người chơi cái đã rồi tiền sau, thêm phím như "space" để chuyển sang. được thì cứ hiển thị hết trên cùng 1 màn hình
-thêm bảng chọn bạn có muốn tiếp tục ko, hiển thị thêm số tiền ban đầu cược và số tiền còn lại hiện có, nếu hết tiền rồi thì ko cho tiếp tục nữa mà đá về menu; sau khi tiếp tục thì chơi lại map đó
kiệt:tiếp tục nghĩ và làm phụ kiện
long:
-đòi hỏi thấp thấp, chỉ cần add đủ 100 câu đố là ok rồi; 
-tìm nhạc cho minigame; 
-tìm background cho minigame luôn, có thể yêu cầu team design thiết kế; 
-làm sao để khi vào minigame thì background đổi thành background của minigame và khi về menu (do thua hoặc hết câu hỏi) thì menu về lại background cũ