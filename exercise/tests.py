import json

from django.test import TestCase

from exercise.models import ChinaRegions, Industry
import os


# Create your tests here.


class TestKLT(TestCase):

    def setUp(self):
        # Every test needs access to the request factory.
        Industry.objects.all().delete()


    def test_china_regions(self):
        # TODO 请把china_regions的省、市、区数据保存到数据库里
        #  注意：保存顺序是有讲究的，否则会保存失败。
        print(1)


    def test_industry(self):
        """
        测试注入全量行业数据到数据库，并测试查询
        """
        with open('./exercise/industry_classification/industry_classification_2017.json' , 'r', encoding='utf8') as f:
           industries: list = json.loads(f.read())

        def save_obj(industries, parent=None):
            for industry in industries:
                code: str = industry.get('code')
                name: str = industry.get('name')
                children: list = industry.get('children')
                if parent:
                    parent = Industry.objects.create(code=code, name=name, parent=parent)
                else:
                    parent = Industry.objects.create(code=code, name=name)
                if children:
                    save_obj(children, parent)

        save_obj(industries)

        for i in Industry.objects.all()[:50]:
            print(f'行业:{i}, 上级行业:{i.parent}')

        print(f"查询:{Industry.objects.get(code='0111')}")