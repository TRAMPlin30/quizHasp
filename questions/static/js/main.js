console.log('Hello World')


const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-test-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href



modalBtns.forEach(modalBtns => modalBtns.addEventListener('click', () => {
    const pk = modalBtns.getAttribute('data-pk')
    const name = modalBtns.getAttribute('data-name')
    const questions = modalBtns.getAttribute('data-questions')
    const time = modalBtns.getAttribute('data-time')
    const pass = modalBtns.getAttribute('data-pass')

    modalBody.innerHTML = `
        <div class="h5 mb-3">Почати наступний тест: "<b>${name}</b>"<div>
        <div class="text-muted">
            <ul>
                <li>Кількість питань: <b>${questions}</b></li>
                <li>Прохідний бал: <b>${pass} %</b></li>
                <li>Обмеження часу: <b>${time} хвл.</b></li>
            </ul>
        </div>
    `

    startBtn.addEventListener('click', () => {
        window.location.href = url + pk
        console.log(time)
    })
}))