# coding:utf-8
from basecontrol import BaseControl
from common.response import Response
from dbmodel.datamodel import DataModel
from collections import defaultdict
from dbmodel.userinfomodel import UserInfoModel
from dbmodel.authtablemodel import AuthTableModel


class DataControl(BaseControl):

    def __init__(self, *args, **kwargs):
        super(DataControl, self).__init__(*args, **kwargs)
        self.datamodel = DataModel()
        self.userinfomodel = UserInfoModel()
        self.authtablemodel = AuthTableModel()

    def auth_require(self, dimsname=None):
        """
        identify the permission of the user
        :return:
        """

        # get the information of the user
        fworkid = self.session.get('fworkid', None)
        userinfo = self.userinfomodel.get_userinfo(fworkid=fworkid)
        flevel_id = userinfo.get('flevel_id', 0)

        levelinfo = self.authtablemodel.get_dims_levelinfo(dimsname=dimsname)
        dims_level_id = levelinfo.get('flevel_id', 10000)

        print userinfo
        print levelinfo

        if flevel_id<dims_level_id:
            return False

        return True

    def format_data(self, dims=None):

        data = dims.get('data', [])
        name = dims.get('name', '')
        type = dims.get('type', 'bar')

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
                'data': axis_y,
                'type': type
            }]
        }

        return dims

    def user_get_data(self):

        dims = self.args.get('dims', None)
        if not dims:
            return Response.responseJson(Response.INPUT_EMPTY, 'input zhibiao is None')

        isAuth = self.auth_require(dimsname=dims)
        if not isAuth:
            return Response.responseJson(Response.NO_AUTH)

        params = {
            'sdate': self.args.get('sdate', ''),
            'edate': self.args.get('edate', '')
        }
        data = self.datamodel.get_data(dims=dims, args=params)

        print data

        dims = {
            'name': dims,
            'type': 'line',
            'data': data
        }
        res_data = self.format_data(dims=dims)
        print res_data

        res_data['title'] = "Stock's Volume"
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
