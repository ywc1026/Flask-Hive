/**
 * Created by ywc on 10/10/17.
 */



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