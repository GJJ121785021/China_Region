from django.db import models

# Create your models here.



class Industry(models.Model):
    """
    该行业表的设计能让有上下级关系的行业依靠parent字段产生关联
    譬如，查询某三级行业，能根据parent字段往上查询到该行业的上级行业(二级)
    """
    code = models.CharField('编号', max_length=12)
    name = models.CharField('行业名称', max_length=100)
    parent = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True,
        verbose_name="父级代码"
    )
    listorder = models.IntegerField('排序', default=999)
    status = models.BooleanField('是否使用', default=True)

    def __str__(self):
        return self.name


class ChinaRegions(models.Model):
    # TODO 中国地区表，请参照Industry表，用上自己的脑子思考如何设计中国地区的表
    #  譬如：你要根据某一个市，要查询出它是属于哪个省，有哪些区
    #  该表的可应用场景：http://wecatch.me/china_regions/

    code = models.CharField(default=None, verbose_name='编号', max_length=12)
    name = models.CharField(max_length=30, verbose_name='地区的名字(例如：广州市)')
    belong_to = models.ForeignKey('self',  on_delete=models.SET_NULL, null=True, related_name='under_region',
                                  verbose_name='上级地区(反向关联为下级)')
    old_name = models.CharField(default=None, null=True,  max_length=30, verbose_name='曾使用过的旧名称')
    status = models.BooleanField('是否使用', default=True)

    def __str__(self):
        return self.name
