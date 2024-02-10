document.addEventListener("DOMContentLoaded", function () {
    const allDropdownMenus = document.querySelectorAll('.day');

    allDropdownMenus.forEach(function (dropdownMenu) {
        const hourlyForecast = dropdownMenu.querySelector('.hourly-forecast');

        function showHourlyForecast() {
            hourlyForecast.style.opacity = '0'; // Set initial opacity to 0
            hourlyForecast.style.display = 'grid';
            setTimeout(() => {
                hourlyForecast.style.opacity = '1'; // Fade in by setting opacity to 1
            }, 10); // Set a small timeout for smoother animation
        }

        function hideHourlyForecast() {
            hourlyForecast.style.opacity = '0'; // Fade out by setting opacity to 0
            setTimeout(() => {
                hourlyForecast.style.display = 'none';
            }, 500); // Wait for the animation to complete before hiding the forecast
        }

        dropdownMenu.addEventListener('mouseenter', showHourlyForecast);
        dropdownMenu.addEventListener('mouseleave', hideHourlyForecast);
    });
});