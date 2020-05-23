(function ($) {
  'use strict';

  $(document).ready(function() {
    var widgetHeartRateMaleChartDom = document.getElementById("widget-rate-male-chart");

    if (widgetHeartRateMaleChartDom) {
      var widgetHeartRateMaleChart = echarts.init(widgetHeartRateMaleChartDom);
      var widgetHeartRateMaleChartOptions = {
        title: null,
        legend: null,
        toolbox: null,
        tooltip: {
          show: false
        },
        grid: {
          left: 0,
          right: 0,
          bottom: 0,
          top: 0
        },
        label: false,
        xAxis: {
          type: 'category',
          show: false,
          boundaryGap: false,
          data : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
        },
        yAxis: {
          type: 'value',
          show: false
        },
        series: [
          {
            type:'line',
            showSymbol: false,
            lineStyle: {
              normal: {
                color: '#38c5d8',
                width: 3
              }
            },
            data:[0,0,0,0,14,0,0,-50,74,-34,0,0,24,0,0,0,0,14,0,0,-50,74,-34,0,0,24,0,0,0,0,14,0,0,-50,74,-34,0,0,24,0,0,0,0,0]
          }
        ]
      };
      widgetHeartRateMaleChart.setOption(widgetHeartRateMaleChartOptions, true);
    }

    var widgetHeartRateFemaleChartDom = document.getElementById("widget-rate-female-chart");

    if (widgetHeartRateFemaleChartDom) {
      var widgetHeartRateFemaleChart = echarts.init(widgetHeartRateFemaleChartDom);
      var widgetHeartRateFemaleChartOptions = {
        title: null,
        legend: null,
        toolbox: null,
        tooltip: {
          show: false
        },
        grid: {
          left: 0,
          right: 0,
          bottom: 0,
          top: 0
        },
        label: false,
        xAxis: {
          type: 'category',
          show: false,
          boundaryGap: false,
          data : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
        },
        yAxis: {
          type: 'value',
          show: false
        },
        series: [
          {
            type:'line',
            showSymbol: false,
            lineStyle: {
              normal: {
                color: '#fe6f60',
                width: 3
              }
            },
            data:[0,0,0,0,14,0,0,-50,74,-34,0,0,24,0,0,0,0,14,0,0,-50,74,-34,0,0,24,0,0,0,0,14,0,0,-50,74,-34,0,0,24,0,0,0,0,0]
          }
        ]
      };
      widgetHeartRateFemaleChart.setOption(widgetHeartRateFemaleChartOptions, true);
    }

    var widgetHeartRateBloodPressureChartDom = document.getElementById("widget-rate-blood-pressure-chart");

    if (widgetHeartRateBloodPressureChartDom) {
      var widgetHeartRateBloodPressureChart = echarts.init(widgetHeartRateBloodPressureChartDom);
      var widgetHeartRateBloodPressureChartOptions = {
        title: null,
        legend: null,
        toolbox: null,
        tooltip: {
          show: false
        },
        grid: {
          left: 0,
          right: 0,
          bottom: 0,
          top: 0
        },
        label: false,
        xAxis: {
          type: 'category',
          show: false,
          boundaryGap: false,
          data : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44]
        },
        yAxis: {
          type: 'value',
          show: false
        },
        series: [
          {
            type:'line',
            showSymbol: false,
            lineStyle: {
              normal: {
                color: '#ffaf50',
                width: 3
              }
            },
            data:[0,0,0,0,14,0,0,-50,74,-34,0,0,24,0,0,0,0,14,0,0,-50,74,-34,0,0,24,0,0,0,0,14,0,0,-50,74,-34,0,0,24,0,0,0,0,0]
          }
        ]
      };
      widgetHeartRateBloodPressureChart.setOption(widgetHeartRateBloodPressureChartOptions, true);
    }

    var widgetTemperatureLeftSideChartDom = document.getElementById("widget-temperature-left-side-chart");

    if (widgetTemperatureLeftSideChartDom) {
      var widgetTemperatureLeftSideChart = echarts.init(widgetTemperatureLeftSideChartDom);
      var widgetTemperatureLeftSideChartOptions = {
        title: null,
        legend: null,
        toolbox: null,
        tooltip: {
          show: false
        },
        grid: {
          left: 0,
          right: 0,
          bottom: 0,
          top: 0
        },
        label: false,
        xAxis: {
          type: 'category',
          show: false,
          boundaryGap: false,
          data : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        },
        yAxis: {
          type: 'value',
          show: false
        },
        series: [
          {
            type:'line',
            showSymbol: false,
            lineStyle: {
              normal: {
                color: '#4F9BF3',
                width: 3
              }
            },
            data:[0,0,0,0,14,0,0,-50,84,-34,0,0,24,0,0,0,0,14,0,0,0,0, 12]
          }
        ]
      };
      widgetTemperatureLeftSideChart.setOption(widgetTemperatureLeftSideChartOptions, true);
    }

    var widgetTemperatureRightSideChartDom = document.getElementById("widget-temperature-right-side-chart");

    if (widgetTemperatureRightSideChartDom) {
      var widgetTemperatureRightSideChart = echarts.init(widgetTemperatureRightSideChartDom);
      var widgetTemperatureRightSideChartOptions = {
        title: null,
        legend: null,
        toolbox: null,
        tooltip: {
          show: false
        },
        grid: {
          left: 0,
          right: 0,
          bottom: 0,
          top: 0
        },
        label: false,
        xAxis: {
          type: 'category',
          show: false,
          boundaryGap: false,
          data : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        },
        yAxis: {
          type: 'value',
          show: false
        },
        series: [
          {
            type:'line',
            showSymbol: false,
            lineStyle: {
              normal: {
                color: '#F145B5',
                width: 3
              }
            },
            data:[0,0,0,0,14,0,0,-50,84,-34,0,0,24,0,0,0,0,14,0,0,0,0, 12]
          }
        ]
      };
      widgetTemperatureRightSideChart.setOption(widgetTemperatureRightSideChartOptions, true);
    }

    var widgetBloodLevelsChartDom = document.getElementById("widget-blood-levels-chart");

    if (widgetBloodLevelsChartDom) {
      var widgetBloodLevelsChart = echarts.init(widgetBloodLevelsChartDom);
      var widgetBloodLevelsChartOptions = {
        title: null,
        legend: null,
        toolbox: null,
        tooltip: {
          show: false
        },
        grid: {
          left: -2,
          right: 23,
          bottom: 0,
          top: 0,
          containLabel: true
        },
        label: false,
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data : [55.2,43,73,51.6,69],
          axisTick: {
            show: false
          },
          axisLabel: {
            fontFamily: 'Open Sans',
            color: '#000',
            fontSize: 15
          },
          axisLine: {
            show: false
          }
        },
        yAxis: {
          type: 'value',
          show: false
        },
        series : [
          { // For shadow
            type: 'bar',
            itemStyle: {
              normal: {color: '#F4F5F6'}
            },
            barGap: '-100%',
            barWidth: 22,
            data: [180,180,180,180,180],
            animation: false
          },
          {
            type:'bar',
            barWidth: 22,
            itemStyle: {
              normal: {
                color: '#38c5d8'
              }
            },
            data:[100,40,130,110,140]
          }
        ]
      };
      widgetBloodLevelsChart.setOption(widgetBloodLevelsChartOptions, true);
    }

    var widgetRecentActivityChartDom = document.getElementById("widget-med-recent-activity-chart");

    if (widgetRecentActivityChartDom) {
      var widgetRecentActivityChart = echarts.init(widgetRecentActivityChartDom);
      var widgetRecentActivityChartOptions = {
        title: null,
        legend: null,
        toolbox: null,
        tooltip: {
          show: false
        },
        grid: {
          left: 0,
          right: 5,
          bottom: 0,
          top: 10,
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            axisTick: {
              show: false
            },
            axisLine: {
              show: false
            },
            axisLabel: {
              fontFamily: 'Open Sans',
              color: function (value, index) {
                if (index === 4 || index === 5 || index === 6) {
                  return '#fe6f60';
                }

                return '#000';
              },
              fontSize: 14
            },
            data: ['9AM','10AM','11AM','12AM','1PM','2PM','3PM','4PM','5PM']
          }
        ],
        yAxis: [
          {
            type: 'value',
            min: 0,
            max: 250,
            interval: 50,
            position: 'right',
            axisLabel: {
              fontFamily: 'Open Sans',
              color: '#939daa',
              fontSize: 12
            },
            axisTick: {
              show: false
            },
            axisLine: {
              show: false
            },
            splitLine: {
              show: false
            }
          }
        ],
        series: [
          {
            type:'bar',
            barGap: '-100%',
            itemStyle: {
              normal: {
                color: '#F4F5F6'
              }
            },
            barWidth: 12,
            data:[250, 250, 250, 250, 250, 250, 250, 250]
          },
          {
            type:'bar',
            itemStyle: {
              normal: {
                color: function (series) {
                  if (series.dataIndex === 4 || series.dataIndex === 5 || series.dataIndex === 6) {
                    return '#fe6f60';
                  }

                  return '#38c5d8';
                }
              }
            },
            barWidth: 12,
            data:[110, 60, 130, 120, 220, 240, 200, 130, 60]
          }
        ]
      };
      widgetRecentActivityChart.setOption(widgetRecentActivityChartOptions, true);
    }
  });
})(jQuery);
