import Chart from "chart.js/auto";

(async function () {
  const data = [
    { year: 2010, count: 10 },
    { year: 2011, count: 20 },
    { year: 2012, count: 15 },
    { year: 2013, count: 25 },
    { year: 2014, count: 22 },
    { year: 2015, count: 30 },
    { year: 2016, count: 28 },
  ];

  new Chart(document.getElementById("acquisitions"), {
    type: "doughnut",
    data: {
      labels: [
        "Groceries",
        "Eating out",
        "Entertainment",
        "Transport",
        "Health",
        "Shopping",
        "Bills",
        "Other",
      ],
      datasets: [
        {
          data: [3, 3, 6, 7, 2, 9, 4, 1],
          backgroundColor: [
            "#ADD8E6",
            "#00008B",
            "#FF69B4",
            "#FFA500",
            "#008000",
            "#800080",
            "#A52A2A",
            "#D3D3D3",
          ],
          hoverOffset: 4,
          display: false,
        },
      ],
    },
  });
})();
