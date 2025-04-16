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

  document.getElementById("submitBtn").addEventListener("click", () => {
    const date = document.getElementById("dateInput").value;
    const time = document.getElementById("timeInput").value;
    const zone = document.getElementById("timezoneSelect").value;

    if (!date || !time || !zone) {
      alert("Пожалуйста, выберите дату, время и таймзону");
      return;
    }

    // 1. Собираем ISO дату
    const datetimeString = `${date}T${time}`;
    const localDT = DateTime.fromISO(datetimeString);
    const zoned = localDT.setZone(zone);

    // 2. Отправка данных в Telegram
    const result = {
      original: localDT.toISO(),
      inZone: zoned.toFormat("yyyy-LL-dd HH:mm ZZZZ"),
      timezone: zone
    };

    // 3. Строим график
    drawChart(zoned);

    // 4. Отправляем в бота (можно поставить setTimeout, если нужно визуально показать график перед закрытием)
    setTimeout(() => {
      tg.sendData(JSON.stringify(result));
      tg.close();
    }, 1000);
  });

  function drawChart(dt) {
    const ctx = document.getElementById('myChart').getContext('2d');

    // Удаляем предыдущий график, если он есть
    if (window.myChart) {
      window.myChart.destroy();
    }

    window.myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['-2ч', '-1ч', 'Сейчас', '+1ч', '+2ч'],
        datasets: [{
          label: 'Активность (пример)',
          data: [5, 6, 8, 6, 4],
          borderColor: 'rgba(0, 136, 204, 1)',
          backgroundColor: 'rgba(0, 136, 204, 0.2)',
          tension: 0.3
        }]
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: 'График около ' + dt.toFormat("HH:mm ZZZZ")
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



