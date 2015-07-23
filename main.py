#content
#basis
p0_list = []
p1_list = []
p2_list = []
view_list = []

def creat_list(l):
    for x in range(10):
        l.append(["."] * 9)
        l[0] = ['1','2','3','4','5','6','7','8','9']
def creat_vlist(l):
    for x in range(10):
        l.append([" "] * 9)
        l[0] = ['1','2','3','4','5','6','7','8','9']
def drawing_check(pos,lst):
    para = 0
    for i in pos:
        if lst[i[0]][i[1]] == 'X' or lst[i[0]][i[1]] == '@':
            para += 1
    if para == 0:
        return True
    else:
        return False
def drawing(pos,lst):#replace space to X
    if drawing_check(pos,lst):
        for i in pos:
            lst[i[0]][i[1]] = 'X'
        lst[pos[0][0]][pos[0][1]] = '@'
        return True
    else:
        return False
def print_list(list_x):
    for index, row in enumerate(list_x):
        print(index, ' '.join(row))
def draw_plane(pos1,pos2,lst):
    pos1[1] -= 1
    pos2[1] -= 1
    if pos1[1] == pos2[1] and pos1[0] > pos2[0]:
        x = pos1[0]
        y = pos1[1]
        if y-2 < 0 or y+2 > 8 or x-3 < 1:
            return False
        else:
            body_1 = [x - 1,y]
            body_2 = [x - 2,y]
            body_3 = [x - 3,y]
            wing_1 = [x-1,y-1]
            wing_2 = [x-1,y+1]
            wing_3 = [x-1,y-2]
            wing_4 = [x-1,y+2]
            tail_1 = [x-3,y-1]
            tail_2 = [x-3,y+1]
            pos = [pos1,body_1,body_2,body_3,wing_1,wing_2,wing_3,wing_4,tail_1,tail_2]
            if not drawing(pos,lst):
                return False
            return True
    #south
    elif pos1[1] == pos2[1] and pos1[0] < pos2[0]:
        x = pos1[0]
        y = pos1[1]
        if y-2 < 0 or y+2 > 8 or x+3 > 9:
            return False
        else:
            body_1 = [x + 1,y]
            body_2 = [x + 2,y]
            body_3 = [x + 3,y]
            wing_1 = [x+1,y-1]
            wing_2 = [x+1,y+1]
            wing_3 = [x+1,y-2]
            wing_4 = [x+1,y+2]
            tail_1 = [x+3,y-1]
            tail_2 = [x+3,y+1]
            pos = [pos1,body_1,body_2,body_3,wing_1,wing_2,wing_3,wing_4,tail_1,tail_2]
            if not drawing(pos,lst):
                return False
            return True
    #north
    elif pos1[0] == pos2[0] and pos1[1] < pos2[1]:
        x = pos1[0]
        y = pos1[1]
        if x-2 < 1 or x+2 > 9 or y+3 > 8:
            return False
        else:
            body_1 = [x,y + 1]
            body_2 = [x,y + 2]
            body_3 = [x,y + 3]
            wing_1 = [x-1,y+1]
            wing_2 = [x+1,y+1]
            wing_3 = [x-2,y+1]
            wing_4 = [x+2,y+1]
            tail_1 = [x-1,y+3]
            tail_2 = [x+1,y+3]
            pos = [pos1,body_1,body_2,body_3,wing_1,wing_2,wing_3,wing_4,tail_1,tail_2]
            if not drawing(pos,lst):
                return False
            return True
    #west
    elif pos1[0] == pos2[0] and pos1[1] > pos2[1]:
        x = pos1[0]
        y = pos1[1]
        if x-2 < 1 or x+2 > 9 or y-3 < 0:
            return False
        else:
            body_1 = [x,y - 1]
            body_2 = [x,y - 2]
            body_3 = [x,y - 3]
            wing_1 = [x-1,y-1]
            wing_2 = [x+1,y-1]
            wing_3 = [x-2,y-1]
            wing_4 = [x+2,y-1]
            tail_1 = [x-1,y-3]
            tail_2 = [x+1,y-3]
            pos = [pos1,body_1,body_2,body_3,wing_1,wing_2,wing_3,wing_4,tail_1,tail_2]
            if not drawing(pos,lst):
                return False
            return True
    #east
def clear():
    '''clear screen'''
    for i in range(60):
        print()
def guess(pos,v_list,b_list):
    global head_count
    if b_list[pos[0]][pos[1]-1] == '.':
        v_list[pos[0]][pos[1]-1] = '.'
    elif b_list[pos[0]][pos[1]-1] == 'X':
        v_list[pos[0]][pos[1]-1] = 'X'
    elif b_list[pos[0]][pos[1]-1] == '@':
        v_list[pos[0]][pos[1]-1] = '@'
        head_count += 1

#single play
import random
def rand_draw(lst):
    count = 0
    while count != 3:#prevent infinite loop
        infi_count = 0
        while infi_count < 200:
            while True:
                a = random.randint(1,9)
                b = random.randint(1,9)
                random_num = random.randint(1,4)
                rand_pos1 = [a,b]
                if random_num == 1:
                    c = a + 3
                    if c <= 9:
                        rand_pos2 = [c,b]
                        break
                elif random_num == 2:
                    c = a - 3
                    if c >= 1:
                        rand_pos2 = [c,b]
                        break
                elif random_num == 3:
                    c = b + 3
                    if c <= 9:
                        rand_pos2 = [a,c]
                        break
                elif random_num == 4:
                    c = b - 3
                    if c >= 1:
                        rand_pos2 = [a,c]
                        break
            if draw_plane(rand_pos1,rand_pos2,lst) == True:
                count += 1
                if count == 3:
                    break
            else:
                infi_count += 1

#create list
creat_list(p0_list)
creat_list(p1_list)
creat_list(p2_list)
creat_vlist(view_list)
rand_draw(p0_list)
rand_draw(p1_list)

#single play
head_count = 0
yorn = ''
while yorn != 'y':
    print('Instructions')
    print()
    print('This game is played in a 9X9 grid,where are hidden three jets.Your goal is to seek and shoot down all three jets.When you hit the head,you will get "@",when you hit the plane but not the head,you will get "X",when you hit nothin,you get ".".')
    print('Below is a example.A jet have a 5-long wing and 3-long tail and 4-long body.')
    print('An important thing you should remember is a jet won\'t overlap the others.')
    print_list(p1_list)
    yorn = input('If you understand,enter "y",if not,just press "Enter" key to reread.')

clear()

while head_count < 3:
    print_list(view_list)
    pos_input_str = input('Please enter the position you want to fire(Row first then column) e.g. "19" :')
    pos_input = [int(pos_input_str[0]),int(pos_input_str[1])]
    guess(pos_input,view_list,p0_list)
    clear()
    print(pos_input)
print_list(p0_list)
print('Congrats!You have found all jets!')
