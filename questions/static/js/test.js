console.log('helloo to questions list')

const url = window.location.href
const questionsBox = document.getElementById('questions-box')
let data


$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response){
        data = response.data
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
    },
    error: function (error) {
        console.log(error)
    }
})

const testForm = document.getElementById('questions-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


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
            console.log(response)
        },
        error: function (error) {
        console.log(error)
        }

    })
}

testForm.addEventListener('submit', e => {
    e.preventDefault()

    sendData()
})