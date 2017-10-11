/**
 * Created by ywc on 10/10/17.
 */



function init_chart(chartlist){

    chartlist.forEach(function(value, index, array){

        var elem = value["elemid"];
        console.log(elem);

        echarts.init(document.getElementById(elem));

    });

}



function flushchart(elem) {

    option = {
    title: {
        text: 'The Price of Stock',
        subtext: '0000338'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross'
        }
    },
    toolbox: {
        show: true,
        feature: {
            saveAsImage: {}
        }
    },
    xAxis:  {
        type: 'category',
        boundaryGap: false,
        data: ['09:30', '09:40', '09:50', '10:00', '10:10', '10:20', '10:30', '10:40', '10:50', '11:00', '11:10', '11:20', '11:30', '13:00', '13:10', '13:20', '13:30', '13:40', '13:50', '14:00']
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            formatter: '{value} $'
        },
        axisPointer: {
            snap: true
        }
    },
    visualMap: {
        show: false,
        dimension: 0,
        pieces: [{
            lte: 6,
            color: 'red'
        }, {
            gt: 6,
            lte: 8,
            color: 'green'
        }, {
            gt: 8,
            lte: 14,
            color: 'green'
        }, {
            gt: 14,
            lte: 17,
            color: 'red'
        }, {
            gt: 17,
            color: 'green'
        }]
    },
    series: [
        {
            name:'Price',
            type:'line',
            smooth: true,
            data: [30, 28, 25, 26, 27, 30, 55, 50, 40, 39, 38, 39, 40, 50, 60, 75, 80, 70, 60, 40],
            markArea: {
                data: [ [{
                    name: 'AskVolume',
                    xAxis: '09:40'
                }, {
                    xAxis: '10:00'
                }], [{
                    name: 'AskVolume',
                    xAxis: '10:50'
                }, {
                    xAxis: '11:30'
                }], [{
                    name: 'AskVolume',
                    xAxis: '13:30'
                }, {
                    xAxis: '14:00'
                }] ]
            }
        }
    ]
};



    // 使用刚指定的配置项和数据显示图表。
    var chart = echarts.getInstanceByDom(document.getElementById(elem));
    chart.setOption(option);

}



