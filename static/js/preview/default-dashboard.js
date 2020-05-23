(function ($) {
  'use strict';

  $(document).ready(function () {
    var widgetIndexChartDom = document.getElementById("widget-index-chart-container");

    if (widgetIndexChartDom) {
      var widgetIndexChart = echarts.init(widgetIndexChartDom);
      var widgetIndexChartOptions = {
        title: null,
        legend: null,
        toolbox: null,
        tooltip: {
          trigger: 'axis'
        },
        grid: {
          top: 0,
          right: 0,
          left: 0,
          bottom: 30
        },
        xAxis : [
          {
            type : 'category',
            boundaryGap : false,
            data : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],
            axisLine: {
              show: false,
              lineStyle: {

              }
            },
            axisTick: {
              show: false
            },
            axisLabel: {
              margin: 10,
              fontFamily: 'Open Sans',
              color: function (value, index) {
                if (((index + 1) % 7 === 0) || (index + 1 === 1)) {
                  return '#111111';
                }

                return '#939daa';
              },
              fontSize: 12
            }
          }
        ],
        yAxis : [
          {
            show: false
          }
        ],
        series : [
          {
            name:'Foreign',
            type:'line',
            stack: 'Foreign',
            showSymbol: false,
            areaStyle: {
              normal: {
                color: '#ECEDED',
                opacity: 1
              }
            },
            lineStyle: {
              normal: {
                color: '#ECEDED'
              }
            },
            data:[242, 232, 251, 264, 320, 360, 390, 250, 232, 211, 264, 390, 360, 410, 260, 282, 271, 264, 360, 380, 410, 350, 232, 241, 354, 340, 370, 410, 290, 330, 350]
          },
          {
            name:'Another Index',
            type:'line',
            stack: 'Another Index',
            showSymbol: false,
            areaStyle: {
              normal: {
                color: '#50D586',
                opacity: 1
              }
            },
            lineStyle: {
              normal: {
                color: '#50D586'
              }
            },
            data:[220, 182, 191, 234, 290, 330, 310, 220, 182, 191, 234, 290, 330, 310, 220, 232, 241, 244, 290, 330, 310, 220, 182, 191, 234, 290, 330, 310, 220, 182, 191]
          },
          {
            name:'Your Index',
            type:'line',
            showSymbol: false,
            stack: 'Your Index',
            areaStyle: {
              normal: {
                color: '#FFD580',
                opacity: 1
              }
            },
            lineStyle: {
              normal: {
                color: '#FFD580'
              }
            },
            data:[120, 132, 101, 134, 90, 230, 210, 120, 132, 101, 134, 90, 230, 210, 134, 90, 230, 210, 120, 132, 101, 132, 101, 134, 90, 230, 210, 120, 132, 101, 134]
          }
        ]
      };
      widgetIndexChart.setOption(widgetIndexChartOptions, true);
    }

      /**
       * Donut chart
       * @type {Element}
       */
    var stepGoalChartDom = document.getElementById("widget-step-goal-donut-chart");

    if (stepGoalChartDom) {
      var stepGoalChart = echarts.init(stepGoalChartDom);
      var stepGoalChartOptions = {
        legend: null,
        series: [
          {
            name:'1',
            type:'pie',
            hoverAnimation: false,
            radius: ['85%', '100%'],
            avoidLabelOverlap: false,
            label: false,
            labelLine: {
              normal: {
                show: false
              }
            },
            data:[
              {
                value:25,
                name:'1',
                itemStyle: {
                  normal: {
                    color: '#ffd875'
                  }
                }
              },
              {
                value:25,
                name:'2',
                itemStyle: {
                  normal: {
                    color: '#5fd47e'
                  }
                }
              },
              {
                value:50,
                name:'3',
                itemStyle: {
                  normal: {
                    color: '#fe7645'
                  }
                }
              }
            ]
          }
        ]
      };
      stepGoalChart.setOption(stepGoalChartOptions, true);
    }

    var stepGoalBarChartDom = document.getElementById("widget-step-goal-bar");

    if (stepGoalBarChartDom) {
      var stepGoalBarChart = echarts.init(stepGoalBarChartDom);
      var posList = [
        'left', 'right', 'top', 'bottom',
        'inside',
        'insideTop', 'insideLeft', 'insideRight', 'insideBottom',
        'insideTopLeft', 'insideTopRight', 'insideBottomLeft', 'insideBottomRight'
      ];
      var stepGoalBarConfigParameters = {
        rotate: {
          min: -90,
          max: 90
        },
        align: {
          options: {
            left: 'left',
            center: 'center',
            right: 'right'
          }
        },
        verticalAlign: {
          options: {
            top: 'top',
            middle: 'middle',
            bottom: 'bottom'
          }
        },
        position: {
          options: echarts.util.reduce(posList, function (map, pos) {
            map[pos] = pos;
            return map;
          }, {})
        },
        distance: {
          min: 0,
          max: 100
        }
      };
      var labelOption = {
        normal: {
          show: false
        }
      };
      var stepGoalBarOptions = {
        color: ['#5fd47e', '#ffd875', '#fe7645'],
        tooltip:null,
        legend: null,
        calculable: false,
        grid: {
          top: 0,
          right: 0,
          left: 0,
          bottom: 30
        },
        xAxis: [
          {
            type: 'category',
            axisTick: {show: false},
            data: ['7/01', '8/01', '9/01', '10/01', '11/01'],
            axisLine: {
              show: false
            },
            axisLabel: {
              margin: 15,
              fontFamily: 'Open Sans',
              color: '#939daa',
              fontSize: 15
            }
          }
        ],
        yAxis : [
          {
            show: false
          }
        ],
        series: [
          {
            name: 'APPL',
            type: 'bar',
            barGap: 1,
            label: labelOption,
            data: [94, 34, 14, 44, 34],
            barWidth: 8,
            itemStyle: {
              normal: {
                barBorderRadius: 8
              }
            }
          },
          {
            name: 'MSFT',
            type: 'bar',
            label: labelOption,
            data: [64, 44, 13, 24, 54],
            barWidth: 8,
            barGap: 1,
            itemStyle: {
              normal: {
                barBorderRadius: 8
              }
            }
          },
          {
            name: 'FB',
            type: 'bar',
            label: labelOption,
            data: [24, 34, 11, 74, 44],
            barWidth: 8,
            barGap: 1,
            itemStyle: {
              normal: {
                barBorderRadius: 8
              }
            }
          }
        ]
      };
      stepGoalBarChart.setOption(stepGoalBarOptions, true);
    }

    var sparkLineNewClientsDom = $('#sparkline-chart-new-clients');

    if (sparkLineNewClientsDom.length) {
      sparkLineNewClientsDom.sparkline([
        16,16,26,26,11,11,21,21,8,8,21,21,19,19,21,21,11,11,10,10,
        16,16,26,26,11,11,21,21,8,8,21,21,19,19,21,21,11,11,8,8,
        16,16,26,26,11,11,21,21,8,8,21,21,19,19,21,21,11,11,10,10,
        16,16,26,26,11,11,21,21,8,8,21,21,19,19,21,21,11,11,8,8
      ], {
        height: 26,
        type: 'bar',
        barWidth: 4,
        barColor: '#7FC48A'
      });
    }

    var sparkLineTotalSalesDom = $('#sparkline-chart-total-sales');

    if (sparkLineTotalSalesDom.length) {
      sparkLineTotalSalesDom.sparkline([
        16,16,26,26,11,11,21,21,8,8,21,21,19,19,21,21,11,11,10,10,
        16,16,26,26,11,11,21,21,8,8,21,21,19,19,21,21,11,11,8,8,
        16,16,26,26,11,11,21,21,8,8,21,21,19,19,21,21,11,11,10,10,
        16,16,26,26,11,11,21,21,8,8,21,21,19,19,21,21,11,11,8,8
      ], {
        height: 26,
        type: 'bar',
        barWidth: 4,
        barColor: '#B979CB'
      });

      sparkLineTotalSalesDom.sparkline([4,1,5,7,9,9,8,7,6,6,4,7,8,4,3,2,2,5,6,7], {
        height: 26,
        composite: true,
        fillColor: false,
        lineColor: '#fff',
        spotRadius: 3,
        spotColor: '#4baf57',
        highlightSpotColor: '#f93329',
        highlightLineColor: '#f93329',
        minSpotColor: '#fff',
        maxSpotColor: '#4baf57'
      });
    }

    var sparkLineTotalSales2Dom = $('#sparkline-chart-total-sales2');

    if (sparkLineTotalSales2Dom.length) {
      sparkLineTotalSales2Dom.sparkline([1,1,0,1,-1,-1,1,-1,1,1,0,1,-1,-1,1,1,0,1,-1,-1,1,-1,1,1,-1,1], {
        height: 26,
        type: 'tristate',
        fillColor: false,
        barWidth: 11,
        barSpacing: 2,
        posBarColor: '#7C9BA7',
        negBarColor: '#7C9BA7',
        zeroBarColor: '#7C9BA7'
      });
    }

    var sparkLineNewInvoicesDom = $('#sparkline-chart-new-invoices');

    if (sparkLineNewInvoicesDom.length) {
      sparkLineNewInvoicesDom.sparkline([
          1,4,5,7,9,9,8,7,6,6,4,4,8,4,3,2,2,5,6,7,
          1,4,5,7,9,9,8,7,6,6,4,7,8,4,3,2,2,5,6,7,
          1,4,5,7,9,9,8,7,6,6,4,7,8,4,3,2,2,5,6,7,
          1,4,5,7,9,9,8,7,6,6,4,7,8,4,3,2,2,5,6,7,
          1,4,5,7,9,9,8,7,6,6,4,7,8,4,3,2,2,5,6,7,
          1,4,5,7,9,9,8,7,6,6,7,6,6,1
        ], {
        height: 26,
        fillColor: false,
        lineColor: '#fff',
        spotRadius: 3,
        spotColor: '#4baf57',
        highlightSpotColor: '#f93329',
        highlightLineColor: '#f93329',
        minSpotColor: '#fff',
        maxSpotColor: '#4baf57',
        normalRangeMin: 10
      });
    }

    var brandsChartDom = $('#widget-brands-chart');

    if (brandsChartDom.length) {
      var brandsChartData = [["2017/06/05",116],["2017/06/06",129],["2017/06/07",135],["2017/06/08",86],["2017/06/09",73],["2017/06/10",85],["2017/06/11",73],["2017/06/12",68],["2017/06/13",92],["2017/06/14",130],["2017/06/15",245],["2017/06/16",139],["2017/06/17",115],["2017/06/18",111],["2017/06/19",309],["2017/06/20",206],["2017/06/21",137],["2017/06/22",128],["2017/06/23",85],["2017/06/24",94],["2017/06/25",71],["2017/06/26",106],["2017/06/27",84],["2017/06/28",93],["2017/06/29",85],["2017/06/30",73],["2017/07/01",83],["2017/07/02",125],["2017/07/03",107],["2017/07/04",82],["2017/07/05",44],["2017/07/06",72],["2017/07/07",106],["2017/07/08",107],["2017/07/09",66],["2017/07/10",91],["2017/07/11",92],["2017/07/12",113],["2017/07/13",107],["2017/07/14",131],["2017/07/15",111],["2017/07/16",64],["2017/07/17",69],["2017/07/18",88],["2017/07/19",77],["2017/07/20",83],["2017/07/21",111],["2017/07/22",57],["2017/07/23",55],["2017/07/24",60]];
      var brandsChartDateList = brandsChartData.map(function (item) {
        return item[0];
      });
      var brandsChartValueList = brandsChartData.map(function (item) {
        return item[1];
      });

      var brandsChartOptions = {
        tooltip: {
          trigger: 'axis'
        },
        title: null,
        legend: null,
        toolbox: null,
        grid: {
          top: 0,
          right: 0,
          left: -4,
          bottom: 30
        },
        xAxis: [{
          data: brandsChartDateList,
          axisLine: {
            show: false
          },
          axisTick: {
            show: false
          },
          axisLabel: {
            margin: 10,
            fontFamily: 'Open Sans',
            fontSize: 12,
            color: '#111',
            showMinLabel: false,
            showMaxLabel: false
          }
        }],
        yAxis : [
          {
            show: false
          }
        ],
        series: [{
          type: 'line',
          showSymbol: false,
          data: brandsChartValueList,
          lineStyle: {
            normal: {
              color: '#0094f2'
            }
          },
          areaStyle: {
            normal: {
              color: '#F3F9FC',
              opacity: 1
            }
          }
        }]
      };
      var brandsChart = echarts.init(brandsChartDom.get(0));
      brandsChart.setOption(brandsChartOptions, true);
    }
  });
})(jQuery);
