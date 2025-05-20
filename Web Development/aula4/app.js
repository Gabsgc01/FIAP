const form = document.getElementById('form')
const inputNome = document.getElementById('nome')
const inputEmail = document.getElementById('email')
const inputAssunto = document.getElementById('assunto')
const inputMensagem = document.getElementById('mensagem')
const inputEnviar = document.getElementById('btnClicar')
const mensagemErro = document.getElementById('mensagem-erro')
const cadastroUsuario = document.getElementById('cadastroUsuarios')

btnEnviar.addEventListener("click", function (event) {
    event.preventDefault()

    const nome = inputNome.value
    const email = inputEmail.value

    if (nome === "" || email === "") {
        mensagemErro.textContent = "Preencha os campos Vazios"
        mensagemErro.style.color = "#ff0000"
        // mensagemErro.classList.add('mensagemAlerta')
        // mensagemErro.src = ""
        return
    }

    let cardUsuario = document.createElement('div')
    cardUsuario.innerHTML = `
    <h3> Nome: ${nome}</h3>
    <p> E-mail: ${email}</p>
    `
    cadastroUsuario.append(cardUsuario)

    form.reset()
})



