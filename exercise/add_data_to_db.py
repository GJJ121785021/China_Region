import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'actual_combat.settings')
django.setup()

import json
from exercise.models import ChinaRegions, Industry

base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'china_regions')


def province():
    with open(os.path.join(base_dir, 'province.json'), 'r', encoding='utf-8') as f:
        datas = json.loads(f.read())
        for data in datas:
            name = data.get('name')
            code = data.get('id')
            ChinaRegions.objects.create(name=name, code=code)
    print('province.json插入数据库完成')


def after_province(filename):
    with open(os.path.join(base_dir, filename), 'r', encoding='utf-8') as f:
        datas = json.loads(f.read())
        for parent_code in datas.keys():
            parent = ChinaRegions.objects.get(code=parent_code)
            sons = datas[parent_code]
            for son in sons:
                name = son.get('name')
                code = son.get('id')
                ChinaRegions.objects.create(name=name, code=code, belong_to=parent)
    print(filename + '插入数据库完成')


if __name__ == '__main__':
    queryset = ChinaRegions.objects.all()
    if queryset.exists():
        inp = input('存在数据,是否删除重写？(yes/no):')
        if inp == 'yes':
            queryset.delete()
        else:
            print('未执行插入操作')
            import sys
            sys.exit(0)
    province()
    after_province('city.json')
    after_province('county.json')
    after_province('town.json')
