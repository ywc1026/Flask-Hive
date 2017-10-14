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
            minDate:"2014-09-19 00:00:00",
            okfun:function(obj) {
                var sdate = $("#sdate").val();
                var edate = $("#edate").val();

                charlist.forEach(function (value, index, array) {

                    var elem = value['elemid'];
                    var dims = value["dims"];
                    flushchart(sdate, edate, elem, dims);
                })

            }
    })

    $("#edate").jeDate({
            format:"YYYY-MM-DD",
            isTime:false,
            isinitVal: true,
            minDate:"2014-09-19 00:00:00",
            okfun:function(obj) {
                var sdate = $("#sdate").val();
                var edate = $("#edate").val();

                charlist.forEach(function (value, index, array) {

                    var elem = value['elemid'];
                    var dims = value["dims"];
                    flushchart(sdate, edate, elem, dims);
                })
            }
    })

}




function flushchart(sdate, edate, elem, dims) {

    var url = "";
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


    var title = data["data"];
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
                data:['销量']
            },
            xAxis: {
                data: xAxis
            },
            yAxis: {},
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