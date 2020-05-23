(function ($) {
  'use strict';

  $(document).ready(function() {
    var salesTotalEventProceedChartDom = $('#widget-sales-total-chart-event-proceed');

    if (salesTotalEventProceedChartDom.length) {
      var salesTotalEventProceedChartOptions = {
        tooltip: {
          trigger: 'axis'
        },
        title: null,
        legend: null,
        toolbox: null,
        grid: {
          top: 0,
          right: 0,
          left: 0,
          bottom: 0
        },
        xAxis: [{
          data: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
          axisLine: {
            show: false
          },
          axisTick: {
            show: false
          },
          axisLabel: {
            show: false
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
          data: [0, 30, 12, 36, 24, 30, 20, 38, 51, 38, 35, 24, 36, 51, 37],
          lineStyle: {
            normal: {
              color: {
                type: 'linear',
                colorStops: [{
                  offset: 1, color: '#1ed2ff' // 0% 处的颜色
                }, {
                  offset: 0, color: '#269af1' // 100% 处的颜色
                }]
              }
            }
          },
          areaStyle: {
            normal: {
              color: 'transparent',
              opacity: 0
            }
          }
        }]
      };
      var salesTotalEventProceedChart = echarts.init(salesTotalEventProceedChartDom.get(0));
      salesTotalEventProceedChart.setOption(salesTotalEventProceedChartOptions, true);
    }

    var salesTotalActionExecutedChartDom = $('#widget-sales-total-chart-action-executed');

    if (salesTotalActionExecutedChartDom.length) {
      var salesTotalActionExecutedChartOptions = {
        tooltip: {
          trigger: 'axis'
        },
        title: null,
        legend: null,
        toolbox: null,
        grid: {
          top: 0,
          right: 0,
          left: 0,
          bottom: 0
        },
        xAxis: [{
          data: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
          axisLine: {
            show: false
          },
          axisTick: {
            show: false
          },
          axisLabel: {
            show: false
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
          data: [0, 30, 12, 36, 24, 30, 20, 38, 51, 38, 35, 24, 36, 51, 37],
          lineStyle: {
            normal: {
              color: {
                type: 'linear',
                colorStops: [{
                  offset: 1, color: '#25d33f'
                }, {
                  offset: 0, color: '#35ae47'
                }]
              }
            }
          },
          areaStyle: {
            normal: {
              color: 'transparent',
              opacity: 0
            }
          }
        }]
      };
      var salesTotalActionExecutedChart = echarts.init(salesTotalActionExecutedChartDom.get(0));
      salesTotalActionExecutedChart.setOption(salesTotalActionExecutedChartOptions, true);
    }

    var salesTotalCustomersChartDom = $('#widget-sales-total-chart-customers');

    if (salesTotalCustomersChartDom.length) {
      var salesTotalCustomersChartOptions = {
        tooltip: {
          trigger: 'axis'
        },
        title: null,
        legend: null,
        toolbox: null,
        grid: {
          top: 0,
          right: 0,
          left: 0,
          bottom: 0
        },
        xAxis: [{
          data: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
          axisLine: {
            show: false
          },
          axisTick: {
            show: false
          },
          axisLabel: {
            show: false
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
          data: [0, 30, 12, 36, 24, 30, 20, 38, 51, 38, 35, 24, 36, 51, 37],
          lineStyle: {
            normal: {
              color: {
                type: 'linear',
                colorStops: [{
                  offset: 1, color: '#a486ff'
                }, {
                  offset: 0, color: '#7552e0'
                }]
              }
            }
          },
          areaStyle: {
            normal: {
              color: 'transparent',
              opacity: 0
            }
          }
        }]
      };
      var salesTotalCustomersChart = echarts.init(salesTotalCustomersChartDom.get(0));
      salesTotalCustomersChart.setOption(salesTotalCustomersChartOptions, true);
    }

    var customersChartDom = $('#widget-sales-customers-chart');

    if (customersChartDom.length) {
      var customersChartData = [
        ["2017/06/05",40],
        ["2017/06/06",30],
        ["2017/06/07",90],
        ["2017/06/08",70],
        ["2017/06/09",40],
        ["2017/06/10",60],
        ["2017/06/11",55],
        ["2017/06/12",30],
        ["2017/06/13",50]
      ];
      var customersChartDateList = customersChartData.map(function (item) {
        return item[0];
      });
      var customersChartValueList = customersChartData.map(function (item) {
        return item[1];
      });
      var customersChartOptions = {
        tooltip: {
          trigger: 'axis'
        },
        title: null,
        legend: null,
        toolbox: null,
        grid: {
          top: 10,
          right:15,
          left: 45,
          bottom: 35,
          borderColor: 'red'
        },
        xAxis: [{
          data: customersChartDateList,
          axisLine: {
            show: false
          },
          axisTick: {
            show: false
          },
          axisLabel: {
            margin: 20,
            fontFamily: 'Open Sans',
            fontSize: 14,
            color: '#939daa',
            showMinLabel: false,
            showMaxLabel: false
          }
        }],
        yAxis : [
          {
            axisLine: {
              show: false
            },
            axisTick: {
              show: false
            },
            max: 100,
            min: 0,
            splitNumber: 10,
            axisLabel: {
              margin: 20,
              fontFamily: 'Open Sans',
              fontSize: 14,
              color: '#939daa',
              showMinLabel: false,
              showMaxLabel: false
            }
          }
        ],
        series: [{
          type: 'line',
          showSymbol: false,
          data: customersChartValueList,
          lineStyle: {
            normal: {
              color: '#9CEBD4'
            }
          },
          areaStyle: {
            normal: {
              color: '#9CEBD4',
              opacity: .7
            }
          }
        }]
      };
      var customersChart = echarts.init(customersChartDom.get(0));
      customersChart.setOption(customersChartOptions, true);
    }

    var stepDistributionChartDom = $('#widget-step-distribution-chart');

    if (stepDistributionChartDom.length) {
      var stepDistributionChart = echarts.init(stepDistributionChartDom.get(0));
      var stepDistributionChartOptions = {
        legend: {
          show: false
        },
        series: [
          {
            type:'pie',
            hoverAnimation: false,
            radius: ['60%', '90%'],
            avoidLabelOverlap: false,
            label: {
              normal: {
                show: false,
                position: 'center'
              },
              emphasis: {
                show: true,
                textStyle: {
                  fontFamily: 'Open Sans',
                  fontSize: '20'
                }
              }
            },
            labelLine: {
              normal: {
                show: false
              }
            },
            data:[
              {
                value:140,
                name:'Pending',
                itemStyle: {
                  normal: {
                    color: '#ff6384'
                  }
                }
              },
              {
                value:50,
                name:'Arrived',
                itemStyle: {
                  normal: {
                    color: '#4bc0c0'
                  }
                }
              },
              {
                value:100,
                name:'Canceled',
                itemStyle: {
                  normal: {
                    color: '#ffcd56'
                  }
                }
              },
              {
                value:130,
                name:'Walk In',
                itemStyle: {
                  normal: {
                    color: '#ad7cf9'
                  }
                }
              },
              {
                value:301,
                name:'Confirm',
                itemStyle: {
                  normal: {
                    color: '#ff9f40'
                  }
                }
              }
            ]
          }
        ]
      };

      stepDistributionChart.setOption(stepDistributionChartOptions, true);
    }

    var salesEventStatsChartDom = $('#widget-sales-event-stats-chart');

    if (salesEventStatsChartDom.length) {
      var salesEventStatsChart = echarts.init(salesEventStatsChartDom.get(0));
      var salesEventStatsChartOptions = {
        legend: {
          show: false
        },
        grid: {
          top: 0,
          right: 0,
          left: 0,
          bottom: 0
        },
        series: [
          {
            type:'pie',
            radius: ['70%', '100%'],
            selectedOffset: 0,
            hoverAnimation: false,
            avoidLabelOverlap: false,
            label: {
              normal: {
                show: false,
                position: 'center'
              },
              emphasis: {
                show: true,
                textStyle: {
                  fontFamily: 'Open Sans',
                  fontSize: '15'
                }
              }
            },
            labelLine: {
              normal: {
                show: false
              }
            },
            data:[
              {
                value:140,
                name:'Pending',
                itemStyle: {
                  normal: {
                    color: '#ff6384'
                  }
                }
              },
              {
                value:50,
                name:'Arrived',
                itemStyle: {
                  normal: {
                    color: '#4bc0c0'
                  }
                }
              },
              {
                value:100,
                name:'Canceled',
                itemStyle: {
                  normal: {
                    color: '#ffcd56'
                  }
                }
              },
              {
                value:130,
                name:'Walk In',
                itemStyle: {
                  normal: {
                    color: '#ad7cf9'
                  }
                }
              },
              {
                value:301,
                name:'Confirm',
                itemStyle: {
                  normal: {
                    color: '#ff9f40'
                  }
                }
              }
            ]
          }
        ]
      };

      salesEventStatsChart.setOption(salesEventStatsChartOptions, true);
    }

    var salesActionStatsChartDom = $('#widget-sales-action-stats-chart');

    if (salesActionStatsChartDom.length) {
      var salesActionStatsChart = echarts.init(salesActionStatsChartDom.get(0));
      var salesActionStatsChartOptions = {
        legend: {
          show: false
        },
        grid: {
          top: 0,
          right: 0,
          left: 0,
          bottom: 0
        },
        series: [
          {
            type:'pie',
            radius: ['70%', '100%'],
            selectedOffset: 0,
            hoverAnimation: false,
            avoidLabelOverlap: false,
            label: {
              normal: {
                show: false,
                position: 'center'
              },
              emphasis: {
                show: true,
                textStyle: {
                  fontFamily: 'Open Sans',
                  fontSize: '15'
                }
              }
            },
            labelLine: {
              normal: {
                show: false
              }
            },
            data:[
              {
                value:140,
                name:'Pending',
                itemStyle: {
                  normal: {
                    color: '#ff6384'
                  }
                }
              },
              {
                value:50,
                name:'Arrived',
                itemStyle: {
                  normal: {
                    color: '#4bc0c0'
                  }
                }
              },
              {
                value:100,
                name:'Canceled',
                itemStyle: {
                  normal: {
                    color: '#ffcd56'
                  }
                }
              },
              {
                value:130,
                name:'Walk In',
                itemStyle: {
                  normal: {
                    color: '#ad7cf9'
                  }
                }
              },
              {
                value:301,
                name:'Confirm',
                itemStyle: {
                  normal: {
                    color: '#ff9f40'
                  }
                }
              }
            ]
          }
        ]
      };

      salesActionStatsChart.setOption(salesActionStatsChartOptions, true);
    }
  });
})(jQuery);
