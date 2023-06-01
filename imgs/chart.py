
const colors = ['#5470C6', '#91CC75', '#EE6666'];
option = {
  color: colors,
  tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'cross'
    }
  },
  grid: {
    right: '20%'
  },
  toolbox: {
    feature: {
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  legend: {
    data: ['Universities','Rows',"Increment" ]
  },
  xAxis: [
    {
      type: 'category',
      axisTick: {
        alignWithLabel: true
      },
      // prettier-ignore
      data: ['5/29','5/30','5/31', '6/1', '6/2', '6/3', '6/4', '6/5']
    }
  ],
  yAxis: [
    {
      type: 'value',
      name: 'Rows',
      position: 'right',
      alignTicks: true,
      axisLine: {
        show: true,
        lineStyle: {
          color: colors[0]
        }
      },
      axisLabel: {
        formatter: '{value}'
      }
    },

    {
      type: 'value',
      name: 'Universities',
      position: 'left',
      alignTicks: true,
      axisLine: {
        show: true,
        lineStyle: {
          color: colors[2]
        }
      },
      axisLabel: {
        formatter: '{value}'
      }
      
    },

  ],
  series: [
    {
      name: 'Rows',
      type: 'bar',
      data: [1022, 7349, 14592,18236]
    },

    {
      name: 'Universities',
      type: 'line',
      color:"#EE6666",
      yAxisIndex: 1,
      data: [5,10,30,37]
    },
        {
      name: 'Increment',
      type: 'bar',
      color:"#91CC75",
      data: [0,6327,7243,3644]
    }
  ]
};
