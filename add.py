'''
=============SON OF GENISYS=====================
Các thành viên Astra thêm tập lệnh 4
Được mã hóa bởi một đứa trẻ ngu ngốc- github.com
************************************************
'''

# import libraries
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, PhoneNumberBannedError, ChatAdminRequiredError
from telethon.errors.rpcerrorlist import ChatWriteForbiddenError, UserBannedInChannelError, UserAlreadyParticipantError, FloodWaitError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
from telethon.tl.functions.messages import ImportChatInviteRequest, AddChatUserRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.types import UserStatusRecently
import time
import random
from colorama import init, Fore
import os
import pickle


init()


r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs

def banner():
    # fancy logo
    b = [
    '   #####     #    ######  #######',
    '  #     #   # #   #     # #     #',
    '  #        #   #  #     # #     #', 
    '   #####  #     # ######  #     #', 
    '        # ####### #     # #     #', 
    '  #     # #     # #     # #     #', 
    '   #####  #     # ######  #######' 
    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{rs}')
    print('=============SABO==============')
    print(f'{lg}   Version: {w}1.0{lg} | Tác giả: {w}SABO{rs}\n')


# function to clear screen
def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

# create sessions(if any) and check for any banned accounts
# TODO: Remove code input(just to check if an account is banned)
print('\n' + info + lg + ' Kiểm tra các tài khoản bị cấm...' + rs)
for a in accounts:
    phn = a[0]
    print(f'{plus}{grey} Kiểm tra {lg}{phn}')
    clnt = TelegramClient(f'sessions/{phn}', 3910389, '86f861352f0ab76a251866059a6adbd6')
    clnt.connect()
    banned = []
    if not clnt.is_user_authorized():
        try:
            clnt.send_code_request(phn)
            print('OK')
        except PhoneNumberBannedError:
            print(f'{error} {w}{phn} {r}is banned!{rs}')
            banned.append(a)
    for z in banned:
        accounts.remove(z)
        print(info+lg+' Đã xóa tài khoản bị cấm [Xóa vĩnh viễn bằng manager.py]'+rs)
    time.sleep(0.5)
    clnt.disconnect()


print(info+' Đã tạo phiên!')
clr()
banner()
# func to log scraping details(link of the grp to scrape
# and current index) in order to resume later
def log_status(scraped, index):
    with open('status.dat', 'wb') as f:
        pickle.dump([scraped, int(index)], f)
        f.close()
    print(f'{info}{lg} Phiên được lưu trữ trong {w}status.dat{lg}')
    

def exit_window():
    input(f'\n{cy} Nhấn enter để thoát...')
    clr()
    banner()
    sys.exit()

# đọc chi tiết người dùng
try:
    # yêu cầu tiếp tục thêm
    with open('status.dat', 'rb') as f:
        status = pickle.load(f)
        f.close()
        lol = input(f'{INPUT}{cy} Tiếp tục cạo các thành viên từ {w}{status[0]}{lg}? [y/n]: {r}')
        if 'y' in lol:
            scraped_grp = status[0] ; index = int(status[1])
        else:
            if os.name == 'nt': 
                os.system('del status.dat')
            else: 
                os.system('rm status.dat')
            scraped_grp = input(f'{INPUT}{cy} Liên kết nhóm Công khai/Riêng tư để cạo các thành viên: {r}')
            index = 0
except:
    scraped_grp = input(f'{INPUT}{cy} Liên kết nhóm Công khai/Riêng tư để cạo các thành viên: {r}')
    index = 0
# tải tất cả các tài khoản (số điện thoại)
accounts = []
f = open('vars.txt', 'rb')
while True:
    try:
        accounts.append(pickle.load(f))
    except EOFError:
        break

print(f'{info}{lg} Tổng số tài khoản: {w}{len(accounts)}')
number_of_accs = int(input(f'{INPUT}{cy} Nhập số tài khoản để sử dụng: {r}'))
print(f'{info}{cy} Chọn một sự lựa chọn{lg}')
print(f'{cy}[0]{lg} Thêm vào nhóm công khai')
print(f'{cy}[1]{lg} Thêm vào nhóm riêng tư')
choice = int(input(f'{INPUT}{cy} Nhập lựa chọn: {r}'))
if choice == 0:
    target = str(input(f'{INPUT}{cy} Nhập liên kết nhóm công khai: {r}'))
else:
    target = str(input(f'{INPUT}{cy} Nhập liên kết nhóm riêng tư: {r}'))
print(f'{grey}_'*50)
status_choice = str(input(f'{INPUT}{cy} Bạn có muốn lọc thành viên hoạt động không?[y/n]: {r}'))
to_use = [x for x in accounts[:number_of_accs]]
for l in to_use: accounts.remove(l)
with open('vars.txt', 'wb') as f:
    for a in accounts:
        pickle.dump(a, f)
    for ab in to_use:
        pickle.dump(ab, f)
    f.close()
sleep_time = int(input(f'{INPUT}{cy} Nhập thời gian trễ cho mỗi yêu cầu{w}[{lg}0 for None{w}]: {r}'))
#print(f'{info}{lg} Tham gia nhóm từ {w}{number_of_accs} tài khoản...')
#print(f'{grey}-'*50)
print(f'{success}{lg} -- Thêm thành viên từ {w}{len(to_use)}{lg} tài khoản --')
adding_status = 0
approx_members_count = 0
for acc in to_use:
    stop = index + 49
    c = TelegramClient(f'sessions/{acc[0]}', 3910389 , '86f861352f0ab76a251866059a6adbd6')
    c.start()
    acc_name = c.get_me().first_name
    print(f'{plus}{grey} User: {cy}{acc_name}{lg} -- {cy}Phiên bắt đầu ')
    try:
        if '/joinchat/' in scraped_grp:
            g_hash = scraped_grp.split('/joinchat/')[1]
            try:
                c(ImportChatInviteRequest(g_hash))
                print(f'{plus}{grey} Tài khoản: {cy}{acc_name}{lg} -- Đã tham gia nhóm để cạo')
            except UserAlreadyParticipantError:
                pass 
        else:
            c(JoinChannelRequest(scraped_grp))
            print(f'{plus}{grey} Tài khoản: {cy}{acc_name}{lg} -- Đã tham gia nhóm để cạo')
        scraped_grp_entity = c.get_entity(scraped_grp)
        if choice == 0:
            c(JoinChannelRequest(target))
            print(f'{plus}{grey} Tài khoản: {cy}{acc_name}{lg} -- Đã tham gia nhóm để thêm thành viên')
            target_entity = c.get_entity(target)
            target_details = InputPeerChannel(target_entity.id, target_entity.access_hash)
        else:
            try:
                grp_hash = target.split('/joinchat/')[1]
                c(ImportChatInviteRequest(grp_hash))
                print(f'{plus}{grey} Tài khoản: {cy}{acc_name}{lg} -- Đã tham gia nhóm để thêm thành viên')
            except UserAlreadyParticipantError:
                pass
            target_entity = c.get_entity(target)
            target_details = target_entity
    except Exception as e:
        print(f'{error}{r} Tài khoản: {cy}{acc_name}{lg} -- Không thể tham gia nhóm')
        print(f'{error} {r}{e}')
        continue
    print(f'{plus}{grey} Tài khoản: {cy}{acc_name}{lg} -- {cy}Truy xuất các thực thể...')
    #c.get_dialogs()
    try:
        members = []
        members = c.get_participants(scraped_grp_entity, aggressive=True)
    except Exception as e:
        print(f'{error}{r} Không thể loại bỏ thành viên')
        print(f'{error}{r} {e}')
        continue
    approx_members_count = len(members)
    assert approx_members_count != 0
    if index >= approx_members_count:
        print(f'{error}{lg} Không có thành viên nào để thêm!')
        continue
    print(f'{info}{lg} Start: {w}{index}')
    #adding_status = 0
    peer_flood_status = 0
    for user in members[index:stop]:
        index += 1
        if peer_flood_status == 10:
            print(f'{error}{r} Quá nhiều lỗi lũ lụt ngang hàng! Đang đỗi phiên..')
            break
        try:
            if status_choice == 'y':
                if not user.status == UserStatusRecently():
                    continue
            #added_users.append(user)
            #user_to_add = c.get_entity(user['id'])
            if choice == 0:
                c(InviteToChannelRequest(target_details, [user]))
            else:
                c(AddChatUserRequest(target_details.id, user, 42))
            user_id = user.first_name
            target_title = target_entity.title
            print(f'{plus}{grey} Tài khoản: {cy}{acc_name}{lg} -- {cy}{user_id} {lg}--> {cy}{target_title}')
            #print(f'{info}{grey} User: {cy}{acc_name}{lg} -- Ngủ 1 giây')
            adding_status += 1
            print(f'{info}{grey} Tài khoản: {cy}{acc_name}{lg} -- Ngủ {w}{sleep_time} {lg} giây')
            time.sleep(sleep_time)
        except UserPrivacyRestrictedError:
            print(f'{minus}{grey} Tài khoản: {cy}{acc_name}{lg} -- {r}Lỗi hạn chế quyền riêng tư của người dùng')
            continue
        except PeerFloodError:
            print(f'{error}{grey} Tài khoản: {cy}{acc_name}{lg} -- {r}Lỗi lũ lụt ngang hàng.')
            peer_flood_status += 1
            continue
        except ChatWriteForbiddenError:
            print(f'{error}{r} Không thể thêm vào nhóm. Liên hệ với quản trị viên nhóm để cho phép thêm thành viên')
            if index < approx_members_count:
                log_status(scraped_grp, index)
            exit_window()
        except UserBannedInChannelError:
            print(f'{error}{grey} Tài khoản: {cy}{acc_name}{lg} -- {r}Bị cấm viết trong nhóm')
            break
        except ChatAdminRequiredError:
            print(f'{error}{grey} Người dùng: {cy}{acc_name}{lg} -- {r}Cần thêm quyền Quản trị trò chuyện')
            break
        except UserAlreadyParticipantError:
            print(f'{minus}{grey} Người dùng: {cy}{acc_name}{lg} -- {r}Người dùng đã là người tham gia')
            continue
        except FloodWaitError as e:
            print(f'{error}{r} {e}')
            break
        except ValueError:
            print(f'{error}{r} Lỗi trong thực thể')
            continue
        except KeyboardInterrupt:
            print(f'{error}{r} ---- Thêm đã chấm dứt ----')
            if index < len(members):
                log_status(scraped_grp, index)
            exit_window()
        except Exception as e:
            print(f'{error} {e}')
            continue
#global adding_status, approx_members_count
if adding_status != 0:
    print(f"\n{info}{lg} Thêm phiên đã kết thúc")
try:
    if index < approx_members_count:
        log_status(scraped_grp, index)
        exit_window()
except:
    exit_window()
