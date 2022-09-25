const rangeValue = document.getElementById('rangeValue')
const range = document.getElementById('range')

rangeValue.innerText = "Длина " + range.value + ' символов'

range.addEventListener('change', () => {
    rangeValue.innerText = "Длина " + range.value + ' символов'
})