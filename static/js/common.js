/**
 * Created by ywc on 10/10/17.
 */


var upColor = '#ec0000';
var upBorderColor = '#8A0000';
var downColor = '#00da3c';
var downBorderColor = '#008F28';


function init_chart(chartlist){

    chartlist.forEach(function(value, index, array){

        var elem = value["elemid"];

        echarts.init(document.getElementById(elem));

    });

}


function init_date(charlist) {

    $("#sdate").jeDate({
            format:"YYYY-MM-DD",
            isTime:false,
            isinitVal: true,
            minDate:"2012-09-19 00:00:00",
            okfun:function(obj) {
                var sdate = $("#sdate").val();
                var edate = $("#edate").val();

                charlist.forEach(function (value, index, array) {

                    var elemid = value['elemid'];
                    var dims = value["dims"];
                    flushchart(sdate, edate, elemid, dims);
                })

            }
    })

    $("#edate").jeDate({
            format:"YYYY-MM-DD",
            isTime:false,
            isinitVal: true,
            minDate:"2012-09-19 00:00:00",
            okfun:function(obj) {
                var sdate = $("#sdate").val();
                var edate = $("#edate").val();

                charlist.forEach(function (value, index, array) {

                    var elemid = value['elemid'];
                    var dims = value["dims"];
                    flushchart(sdate, edate, elemid, dims);
                })
            }
    })

}


function flushchart(sdate, edate, elem, dims) {

    var url = "/data/get_data";
    var params = {
        "sdate": sdate,
        "edate": edate,
        "dims": dims
    };

    console.log(params);
    $.get(url, params, function (json_data) {

        if (json_data.code == 0){
            setChartData(elem, json_data.data);
        }
    });

}


function setChartData(elem, data) {


    var title = data["title"];
    var xAxis = data["xAxis"];
    var series = data["series"];
    // console.log(series[0].type)
    series[0].itemStyle = {
                normal: {
                    color: upColor,
                    color0: downColor,
                    borderColor: upBorderColor,
                    borderColor0: downBorderColor
                }
            };
    series[0].markPoint = {
                label: {
                    normal: {
                        formatter: function (param) {
                            return param != null ? Math.round(param.value) : '';
                        }
                    }
                },
                data: [
                    {
                        name: 'XX标点',
                        coord: ['2013/5/31', 2300],
                        value: 2300,
                        itemStyle: {
                            normal: {color: 'rgb(41,60,85)'}
                        }
                    },
                    {
                        name: 'highest value',
                        type: 'max',
                        valueDim: 'highest'
                    },
                    {
                        name: 'lowest value',
                        type: 'min',
                        valueDim: 'lowest'
                    },
                    {
                        name: 'average value on close',
                        type: 'average',
                        valueDim: 'close'
                    }
                ],
                tooltip: {
                    formatter: function (param) {
                        return param.name + '<br>' + (param.data.coord || '');
                    }
                }
            };
    var names = [];

    series.forEach(function (value, index, array) {
        names.push(value["name"]);
    })


    var option = {
            title: {
                text: title
            },
            tooltip: {},
            legend: {
                data:['日K']
            },
            grid: {
                left: '10%',
                right: '10%',
                bottom: '15%'
            },
            xAxis: {
                data: xAxis,
                scale: true,
                boundaryGap : false,
                axisLine: {onZero: false},
                splitLine: {show: false},
                splitNumber: 20,
                min: 'dataMin',
                max: 'dataMax'
            },
            yAxis: {
                scale: true,
                splitArea: {
                    show: true
        }
            },
            dataZoom: [
                {
                    type: 'inside',
                    start: 50,
                    end: 100
                },
                {
                    show: true,
                    type: 'slider',
                    y: '90%',
                    start: 50,
                    end: 100
                }
    ],
            series: series
        };

    var chart = echarts.getInstanceByDom(document.getElementById(elem));
    chart.setOption(option);
}


function login() {

    $("#btn").click(function () {

        var elem = $(this);

        if (elem.text() == "Sign in"){
            var url = "/user/login";
            var param = {
                "fworkid": $("#account").val(),
                "fpassword": $("#password").val()
            }

            $.post(url, param, function (json_data) {

                console.log(json_data);
                if (json_data.code == 0){
                    elem.text("Logout");
                }else{
                    alert(json_data.msg);
                }

            });
        }else{
            var url = "/user/logout";

            $.post(url, {}, function (json_data) {

                if (json_data.code == 0){
                    elem.text("Sign in");
                }else{
                    alert(json_data.msg);
                }

            });
        }
    })
}