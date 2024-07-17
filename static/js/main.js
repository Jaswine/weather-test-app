document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('#weatherForm')
    const div = document.querySelector('#weather')
    let timeout = null

    const renderLoader = (place) => {
        place.innerHTML = '<div class="loader"></div>'
    }

    const renderError = (place, error) => {
        place.innerHTML = error
    }

    const renderWeather = (place, data) => {
        let img = document.createElement('img')
        img.src = `https://openweathermap.org/img/wn/${data.weather_icon}@2x.png`

        let div_content = document.createElement('div')
        div_content.classList.add('weather__content')
        let h2 = document.createElement('h2')
        h2.innerHTML = `${data.temp}℃`
        let p = document.createElement('p')
        p.innerHTML = `${data.weather_main}: ${data.weather_description}`
        div_content.appendChild(h2)
        div_content.appendChild(p)

        div.appendChild(img)
        div.appendChild(div_content)

        place.innerHTML = ''
        place.appendChild(img)
        place.appendChild(div_content)
    }

    const getData = async (city) => {
        renderLoader(div)
        const response = await fetch(`/api/weather/${city}`)
        const data = await response.json()

        if (response.status == 200) {
            renderWeather(div, data)
        } else {
            renderError(div, data.message)
            console.log(data)
        }
    }

    form.addEventListener('input', (e) => {
        let search = e.target.value

        clearTimeout(timeout);

        timeout = setTimeout(() => {
            if (search.length > 0) {
                getData(search);
            }
        }, 500);
    })

    form.addEventListener('submit', (e) => {
        e.preventDefault()

        let search = e.target.querySelector('input').value

        if (search.length > 0) {
            getData(search)
        }
    })
})