// const DateTime = luxon.DateTime;

// flatpickr("#datetime", {
//   enableTime: true,
//   dateFormat: "Y-m-d H:i",
//   defaultDate: new Date()
// });

// Telegram.WebApp.ready();

// function handleSend() {
//   const dateInput = document.getElementById("datetime").value;
//   const zone = document.getElementById("timezone").value;

//   if (!dateInput) {
//     alert("Выберите дату и время");
//     return;
//   }


//   const localDT = DateTime.fromISO(dateInput);
//   const zoned = localDT.setZone(zone);
//   const result = {
//     original: localDT.toISO(),
//     inZone: zoned.toFormat("yyyy-LL-dd HH:mm ZZZZ"),
//     timezone: zone
//   };

//   // Отправить данные в Telegram
//   Telegram.WebApp.sendData(JSON.stringify(result));

//   // Построить график (рандомные данные, как пример)
//   drawChart(zoned);

// function drawChart(dt) {
//   const ctx = document.getElementById('myChart').getContext('2d');
//   new Chart(ctx, {
//     type: 'line',
//     data: {
//       labels: ['-2ч', '-1ч', 'Сейчас', '+1ч', '+2ч'],
//       datasets: [{
//         label: 'Событие (время)',
//         data: [5, 6, 8, 6, 4],
//         fill: false,
//         tension: 0.3
//       }]
//     },
//     options: {
//       plugins: {
//         title: {
//           display: true,
//           text: 'График около ' + dt.toFormat("HH:mm ZZZZ")
//         }
//       },
//       scales: {
//         y: {
//           beginAtZero: true
//         }
//       }
//     }
//   });
// }
// const tg = window.Telegram.WebApp;

//   // document.getElementById("submitBtn").addEventListener("click", () => {
//   //   const date = document.getElementById("dateInput").value;
//   //   const time = document.getElementById("timeInput").value;

//   //   if (!date || !time) {
//   //     alert("Пожалуйста, выберите дату и время");
//   //     return;
//   //   }

//     const datetimeString = `${date} ${time}`;
//     const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;

//     tg.sendData(JSON.stringify(payload));
//     tg.close(); // Закрыть WebApp
const tg = window.Telegram.WebApp;
const { DateTime } = luxon;

document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("submitBtn");

  button.addEventListener("click", () => {
    const date = document.getElementById("dateInput").value;
    const time = document.getElementById("timeInput").value;
    const zone = document.getElementById("timezone").value;

    if (!date || !time || !zone) {
      alert("Пожалуйста, выберите дату, время и таймзону");
      return;
    }

    const datetimeString = `${date}T${time}`;
    const localDT = DateTime.fromISO(datetimeString);
    const zoned = localDT.setZone(zone);

    const result = {
      original: localDT.toISO(),
      inZone: zoned.toFormat("yyyy-LL-dd HH:mm ZZZZ"),
      timezone: zone
    };

    drawChart(zoned);

    // Подождём 1 секунду для визуального эффекта графика
    setTimeout(() => {
      tg.sendData(JSON.stringify(result));
      tg.close();
    }, 1000);
  });
});

function drawChart(dt) {
  const ctx = document.getElementById("myChart").getContext("2d");

  // Удалим предыдущий график, если он был
  if (window.myChart) {
    window.myChart.destroy();
  }

  window.myChart = new Chart(ctx, {
    type: "line",
    data: {
      labels: ["-2ч", "-1ч", "Сейчас", "+1ч", "+2ч"],
      datasets: [{
        label: "Событие (пример)",
        data: [5, 6, 8, 6, 4],
        borderColor: "rgba(75, 192, 192, 1)",
        backgroundColor: "rgba(75, 192, 192, 0.2)",
        fill: true,
        tension: 0.4
      }]
    },
    options: {
      plugins: {
        title: {
          display: true,
          text: "График около " + dt.toFormat("HH:mm ZZZZ")
        }
      },
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
}




