console.log('helloo to questions list')

const url = window.location.href
const questionsBox = document.getElementById('questions-box')
let data
const timerBox = document.getElementById('timer-box')

const activateTimer = (time) => {
    console.log(time)
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`
    }

    let minutes = time - 1
    let seconds = 60
    let displaySecond
    let displayMinutes

    const timerGo = setInterval(() => {
        seconds--
        if (seconds < 0) {
            seconds = 59
            minutes--
        }
        if (minutes.toString().length < 2) {
            displayMinutes = '0' + minutes
        } else {
            displayMinutes = minutes
        }
        if (seconds.toString().length < 2) {
            displaySecond = '0' + seconds
        } else {
            displaySecond = seconds
        }
        if (minutes === 0 && seconds === 0) {
            console.log('time over')
            clearInterval(timerGo)
            alert('Нажаль Ваш час було вичерпано! Ваші відповіді автоматично відправлені на перевірку! Зараз Ви будете перенаправлені на головну сторінку сервісу!')
            sendData()
            window.location.href = '/'

        }
        timerBox.innerHTML = `<b>${displayMinutes}:${displaySecond}</b>`
    }, 1000)

}

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response) {
        data = response.data   //'data': questions, в файле views.py метод - questions_data_list
        data.forEach(element => {
            for (const [question, answers] of Object.entries(element)) {
                questionsBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}
                    </div>    
                `
                answers.forEach(answer => {
                    questionsBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}">${answer}</label>
                        </div>    
                    `
                })

            }
        });
        activateTimer(response.time) //'time': test.time, в файле views.py метод - questions_data_list
    },
    error: function (error) {
        console.log(error)
    }
})

const testForm = document.getElementById('questions-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const modalBtn = document.getElementsByClassName('modal-button')
const modalBody = document.getElementById('modal-send-result')
const sendButton = document.getElementById('send-button')

const modalWindow = () => {
    modalBody.innerHTML = `Після підтвердження Ви будете перенаправлені
     на головну сторінку атестаційної системи.
     В разі відмови, ви можете переглянуи Ваші відповіді, 
     якщо час, відведенний на проходження тестування не вичерпано.`
    sendButton.addEventListener('click', () => {
        testForm.classList.add('not-visible')
        sendData()
        window.location.href = '/'
    })
}

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })



    $.ajax({
        type: 'POST',
        url: `${url}save`,
        data: data,
        success: function (response) {
            const results = response.results
            console.log(results)
            // const resDiv = document.createElement("div")
            // const cls = ['col-md-8', 'mx-auto', 'my-font', 'text-center']
            // resDiv.classList.add(...cls)
            // resDiv.innerHTML = `Дакуємо за проходження атестації. 
            // Ваші відповіді успішно відправлені. Про результати проходження тесту ві зможете дізнатись в адміністрації після обробки відповідей.`
            // const body = document.getElementsByTagName('body')[0]
            // body.append(resDiv)
        },
        error: function (error) {
            console.log(error)
        }
    })
}

testForm.addEventListener('submit', e => {
    e.preventDefault()
    modalWindow()

})