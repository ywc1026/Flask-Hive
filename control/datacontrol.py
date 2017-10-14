# coding:utf-8
from basecontrol import BaseControl
from common.response import Response
from dbmodel.datamodel import DataModel


class DataControl(BaseControl):

    def __init__(self, *args, **kwargs):
        super(DataControl, self).__init__(*args, **kwargs)
        self.datamodel = DataModel()

    def user_get_data(self):

        dims = self.args.get('dims', None)
        if not None:
            return Response.responseJson(Response.INPUT_EMPTY, 'input zhibiao is None')

        params = {
            'sdate': self.args.get('sdate', ''),
            'edate': self.args.get('edate', '')
        }
        data = self.datamodel.get_data(dims=dims, args=params)

        # option = {
        #     'title': 'ECharts 入门示例',
        #     'xAxis': ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        #     'series': [{
        #         'name': '销量',
        #         'type': 'bar',
        #         'data': [5, 20, 36, 10, 10, 20]
        #     }]
        # }

        return Response.responseJson(Response.SUCCESS, data=option, msg='success')
