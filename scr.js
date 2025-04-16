const DateTime = luxon.DateTime;

flatpickr("#datetime", {
  enableTime: true,
  dateFormat: "Y-m-d H:i",
  defaultDate: new Date()
});

Telegram.WebApp.ready();

function handleSend() {
  const dateInput = document.getElementById("datetime").value;
  const zone = document.getElementById("timezone").value;

  if (!dateInput) {
    alert("Выберите дату и время");
    return;
  }

  const localDT = DateTime.fromISO(dateInput);
  const zoned = localDT.setZone(zone);
  const result = {
    original: localDT.toISO(),
    inZone: zoned.toFormat("yyyy-LL-dd HH:mm ZZZZ"),
    timezone: zone
  };

  // Отправить данные в Telegram
  Telegram.WebApp.sendData(JSON.stringify(result));

  // Построить график (рандомные данные, как пример)
  drawChart(zoned);
}

function drawChart(dt) {
  const ctx = document.getElementById('myChart').getContext('2d');
  new Chart(ctx, {
    type: 'line',
    data: {
      labels: ['-2ч', '-1ч', 'Сейчас', '+1ч', '+2ч'],
      datasets: [{
        label: 'Событие (время)',
        data: [5, 6, 8, 6, 4],
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
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
