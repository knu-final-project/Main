import json
import pandas as pd

class tl_class:
    def __init__(self):
        pass

    def translabel(self, data):
    # Machine129 json translate
        machine129_dic = {'jabgogbab':'잡곡밥', 'baechugimchi':'배추김치', 'doenjangjjigae':'된장찌개',
                        'gimchijjigae':'김치찌개', 'myeolchibokk-eum':'멸치볶음', 'Sigeumchinamul':'시금치나물', 
                        'gajinamul':'가지나물', 'gosalinamul':'고사리나물', 'miyeoggug':'미역국',
                        'gimbab':'김밥', 'bulgogi':'불고기', 'aehobagbokk-eum':'애호박볶음',
                        'musaengchae':'무생채', 'jabchae':'잡채', 'mugug':'무국', 
                        'godeung-eogu-i':'고등어구이', 'ssalbab':'쌀밥', 'gyelanhulai':'계란후라이',
                        'gyelanmal-i':'계란말이'}

        data_b = data.split('\\')
        data_c = eval(data_b[0])
        for i in data_c:
            i['name'] = machine129_dic[i['name']]

        data_d = pd.DataFrame(data_c)

        return data_d

