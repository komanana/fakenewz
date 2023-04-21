<template>
  <div>
    <div class="question-box">
      <div class="word">
        <h1 class="questionNumber" v-model="index">
          Q{{ index + 1 }} {{ questionData.type }}
        </h1>
        <h2 class="questionName" v-model="questionData">
          {{ questionData.title }}
        </h2>
        <select
          name="category"
          id="category"
          ref="category"
          v-model="selectedOption"
          @change="onSelected"
        >
          <!-- <option>Chart Category</option> -->
          <option value="barChart">BarChart</option>
          <option value="pieChart">PieChart</option>
        </select>
      </div>
      <div id="chart">
        <apexchart
          v-if="selectedOption == 'barChart'"
          type="bar"

          :options="barChartOptions"
          :series="barChartSeries"
        ></apexchart>
        <apexchart
          v-else-if="selectedOption == 'pieChart'"
          type="pie"
          :options="pieChartOptions"
          :series="pieChartSeries"
        ></apexchart>
        <!-- <apexchart type="bar" height="350" :options="chartOptions" :series="series"></apexchart> -->
      </div>
    </div>
  </div>
</template>

<script>
import VueApexCharts from "vue-apexcharts";

export default {
  name: "MultipleChoiceResult",
  props: {
    question: Object,
    index: Number,
  },
  data() {
    return {
      selectedOption: "barChart",
      //chartCategory: barChart,
      questionData: "",
      number: 0,
      barChartSeries: [
        {
          data: [],
        },
      ],
      pieChartSeries: [],
      // series: [],
      pieChartOptions: {
        chart: {
          type: "pie",
          height: 250,
        },
        plotOptions: {
          pie: {
            borderRadius: 4,
            horizontal: true,
            dataLabels: {
              position: "top",
            },
          },
        },
        dataLabels: {
          enabled: true,
          offsetX: -6,
          style: {
            fontSize: "12px",
            colors: ["#fff"],
          },
        },
        labels: [],
      },
      barChartOptions: {
        chart: {
          type: "bar",
          height: 150,
        },
        plotOptions: {
          bar: {
            borderRadius: 4,
            horizontal: true,
            dataLabels: {
              position: "top",
            },
          },
        },
        dataLabels: {
          enabled: true,
          offsetX: -6,
          style: {
            fontSize: "12px",
            colors: ["#fff"],
          },
        },
        xaxis: {
          categories: [],
        },
      },
    };
  },
  methods: {
    onSelected() {},
  },
  created() {
    this.number = this.index;
    this.questionData = this.question;

    function string2int(list) {
      let res = [];
      for (let i = 0; i < list.length; i++) {
        res[i] = Number(list[i]);
      }
      return res;
    }

    this.barChartOptions.xaxis.categories = this.question.x;
    this.pieChartOptions.labels = this.question.x;
    this.barChartSeries[0].data = string2int(this.question.y);
    this.pieChartSeries = string2int(this.question.y);
  },
  // data() {
  //   return {
  //     questions: {
  //       "id": 3,
  //       "block": 2,
  //       "name": "How esay does it use?",
  //       "type": "Multiple choice",
  //       "description": "",
  //       "order": 2,
  //       "count": 60,
  //       "choices": [
  //         {
  //           "id": 4,
  //           "question": 2,
  //           "order": 1,
  //           "title": "A",
  //           "number": 20,
  //           "percentage": 0.2
  //         },
  //         {
  //           "id": 5,
  //           "question": 2,
  //           "order": 2,
  //           "title": "B",
  //           "number": 80,
  //           "percentage": 0.8
  //         }
  //       ]
  //     },
  //     series: [{
  //       data: [44.4, 33.3, 11.1, 11.1]
  //     }],
  //     chartOptions: {
  //       chart: {
  //         type: 'bar',
  //         height: 350
  //       },
  //       plotOptions: {
  //         bar: {
  //           borderRadius: 4,
  //           horizontal: true,
  //           dataLabels: {
  //             position: 'top',
  //           }
  //         }
  //       },
  //       dataLabels: {
  //         enabled: true,
  //         offsetX: -6,
  //         style: {
  //           fontSize: '12px',
  //           colors: ['#fff']
  //         }
  //       },
  //       xaxis: {
  //         categories: ['Super easy', 'Easy enough', 'A tad difficult', 'Way to difficult'],
  //       }
  //     }
  //   }
  // }
};
</script>
<style>
@media (min-width: 890px){
  .questionAVG {
    color: red;
    font-size: 20px;
    margin-left: 370px;
  }

  .question-box {
    width: 550px;
    border: 2px solid #eff2f5;
    border-radius: 4px;
    margin: 20px;
    padding: 8px;
  }
  .chart{
    width:350px;
    height:350px
  }
}

@media (max-width: 889px) {
  .question-box {
  width: 280px;
  border: 2px solid #eff2f5;
  border-radius: 4px;
  margin: 20px;
  padding: 8px;
  }
  .chart{
    width:250px;
    height:150px
  }
  .quesionNumber{
  font-size: 25px;
  }
  .questionName{
    font-size: 20px;
  }
}
</style>