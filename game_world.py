# world[0] : 가장 뒤에
# world[1] : 그 앞에
world = [[], [], []]

# 월드에 객체 추가
def add_object(o, depth=1):
    world[depth].append(o)

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

    print('월드에 존재하지 않은 객체를 삭제하려고 합니다.')

# 월드 전체의 객체들을 업데이트
def update():
    for layer in world:
        for o in layer:
            o.update()

# 월드 전체의 객체들을 그린다.
def render():
    for layer in world:
        for o in layer:
            o.draw()