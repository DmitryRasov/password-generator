const pass = document.getElementById('pass')

pass.onclick = () => {
    document.execCommand('copy')
}

pass.addEventListener('copy', (e) => {
    e.preventDefault()
    if (e.clipboardData) {
        e.clipboardData.setData('text/plain', pass.textContent)
        console.log(e.clipboardData.getData('text'))
    }
})