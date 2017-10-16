# coding:utf-8
from basecontrol import BaseControl
from common.response import Response
from dbmodel.datamodel import DataModel
from collections import defaultdict


class DataControl(BaseControl):

    def __init__(self, *args, **kwargs):
        super(DataControl, self).__init__(*args, **kwargs)
        self.datamodel = DataModel()

    def format_data(self, dims=None):

        data = dims.get('data', [])
        name = dims.get('name', '')

        dict_data = defaultdict(list)
        for item in data:
            key = item.get('fdate', None)
            dict_data[key].append(item.get(name))

        axis_x = []
        axis_y = []
        temp = sorted(dict_data.items(), key=lambda x: x[0], reverse=False)
        for key, obj in temp:
            axis_x.append(key)
            sum_data = sum([num for num in obj if isinstance(num, (float, int, long))])
            axis_y.append(sum_data)

        dims = {
            "xAxis": axis_x,
            "series": [{
                'name': name,
                'data': axis_y
            }]
        }
        
        return dims

    def user_get_data(self):

        dims = self.args.get('dims', None)
        if not dims:
            return Response.responseJson(Response.INPUT_EMPTY, 'input zhibiao is None')

        params = {
            'sdate': self.args.get('sdate', ''),
            'edate': self.args.get('edate', '')
        }
        data = self.datamodel.get_data(dims=dims, args=params)

        print data

        dims = {
            'name': dims,
            'data': data
        }
        res_data = self.format_data(dims=dims)
        print res_data
        # option = {
        #     'title': 'ECharts 入门示例',
        #     'xAxis': ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],
        #     'series': [{
        #         'name': '销量',
        #         'type': 'bar',
        #         'data': [5, 20, 36, 10, 10, 20]
        #     }]
        # }

        return Response.responseJson(Response.SUCCESS, data=res_data, msg='success')