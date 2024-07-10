async function getWeatherData() {
    const apiKey = 'ff13222f452ad448227993242c3afbec';
    const city = document.getElementById('city').value;

    if (!city) {
        alert('Please enter a city');
        return;
    }

    const currentWeatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;
    console.log(`Fetching weather data from URL: ${currentWeatherUrl}`);

    await fetchWeather(currentWeatherUrl);
}

async function fetchWeather(url) {
    try {
        console.log('Starting fetch...');
        const response = await fetch(url);
        console.log('Fetch completed.');

        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }

        console.log('Response OK');
        const data = await response.json();
        console.log('Data received:', data);
        // displayWeather(data); // Uncomment and implement this function to display the weather data
    } catch (error) {
        console.error('Error fetching current weather data:', error);
        alert('Error fetching current weather data. Please try again.');
    }
}
