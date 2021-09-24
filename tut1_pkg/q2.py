top_icon = "^"
bottom_icon = "v"
left_icon = "<"
right_icon = ">"


def draw_top_bottom_border(icon):
    print(icon * 100)


def write_title(content, limit):
    i = 0
    while (i < limit):
        print(left_icon + "\t"*10 + content + "\t"*14 + right_icon)
        i += 1


def draw_left_right_border(limit):
    i = 0
    while (i < limit):
        print(left_icon + "\t"*25 + right_icon)
        i += 1
def write_content():
    print(left_icon + "\t" + "Option a" + "\t" * 22 + right_icon)
    print(left_icon + "\t" + "Option b" + "\t" * 22 + right_icon)
    print(left_icon + "\t" + "Option c" + "\t" * 22 + right_icon)

draw_top_bottom_border(top_icon)
draw_left_right_border(3)
write_title("Title",1)
draw_left_right_border(2)
write_content()
draw_left_right_border(2)
draw_top_bottom_border(bottom_icon)