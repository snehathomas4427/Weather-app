
    //const jsonString = '{"coord":{"lon":-0.1257,"lat":51.5085},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04n"}],"base":"stations","main":{"temp":288.44,"feels_like":287.88,"temp_min":287.38,"temp_max":289.16,"pressure":1011,"humidity":71,"sea_level":1011,"grnd_level":1007},"visibility":10000,"wind":{"speed":7.2,"deg":240},"clouds":{"all":57},"dt":1720135690,"sys":{"type":2,"id":2075535,"country":"GB","sunrise":1720151449,"sunset":1720210746},"timezone":3600,"id":2643743,"name":"London","cod":200}';
 function getWeatherData() {
    const apiKey = 'ff13222f452ad448227993242c3afbec';
    const city = document.getElementById('city').value;
    const currentWeatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;
    console.log(currentWeatherUrl);
    if (!city) {
        alert('Please enter a city');
        return;
    }
    fetch(currentWeatherUrl)
      .then( response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
        //   const result = await response.json();
        //   console.log(result);
         return response.json();
      })
      .then(data => {
          console.log(data);
          //displayWeather(data);
      })
      .catch(error => {
          console.log(error);
          console.error('Error fetching current weather data:', error);
          alert('Error fetching current weather data. Please try again.');
      });
    }

function displayWeather(data) {
    const tempDivInfo = document.getElementById('temp-div');
    const weatherInfoDiv = document.getElementById('weather-info');
    const weatherIcon = document.getElementById('weather-icon');
    const hourlyForecastDiv = document.getElementById('hourly-forecast');

    // Clear previous content
    weatherInfoDiv.innerHTML = '';
    hourlyForecastDiv.innerHTML = '';
    tempDivInfo.innerHTML = '';

    if (data.cod === '404') {
        weatherInfoDiv.innerHTML = `<p>${data.message}</p>`;
    } else {
        const cityName = data.name;
        const temperature = Math.round(data.main.temp - 273.15); // Convert to Celsius
        const description = data.weather[0].description;
        const iconCode = data.weather[0].icon;
        const iconUrl = `https://openweathermap.org/img/wn/${iconCode}@4x.png`;

        const temperatureHTML = `
            <p>${temperature}°C</p>
        `;

        const weatherHtml = `
            <p>${cityName}</p>
            <p>${description}</p>
        `;

        tempDivInfo.innerHTML = temperatureHTML;
        weatherInfoDiv.innerHTML = weatherHtml;
        weatherIcon.src = iconUrl;
        weatherIcon.alt = description;

        showImage();
    }
}

function showImage() {
    const weatherIcon = document.getElementById('weather-icon');
    weatherIcon.style.display = 'block'; // Make the image visible once it's loaded
}