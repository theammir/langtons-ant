import random
COLORS = {
    'def': (10, 10, 10),
    'white': (240, 240, 240),
    'red' : (250, 10, 10),
    'green' : (12, 250, 12),
    'blue' : (8, 8, 250),
    'purple' : (139, 20, 255),
    'yellow' : (255, 255, 30),
    'pink' : (252, 15, 192),
    'sky blue' : (117, 187, 253),
    'orange' : (255, 128, 0),
    }
def receive_sequences():
    global COLORS
    color_list = []
    with open('colors_config.txt', 'r') as f:
        result = f.read().split('\n')
        for i in result:
            seqlist = i.split(' - ')
            if (len(seqlist) == 2):
                color_list.append({'color' : COLORS[seqlist[0].lower()], 'dir' : seqlist[1].lower()})
            else:
                color_list.append({'color' : COLORS[seqlist[0].lower()], 'dir' : random.choice(['left', 'right'])})
    return color_list