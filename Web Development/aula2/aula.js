import prompt from 'prompt';
// let nome = "Caio"

// const apiKey = "AOHPH"

// console.log("Mensagem")

// let nome = "outro"
// if (!nome){
//     console.log("É voce!")
// }
// else if (nome==="Fulano"){
//     console.log("QUem é voce?")
// }
//  else{
//     console.log("Não é voce ")
//  }

//  nome === "Caio"? console.log("é voce"): console.log("Não ée voce")


// let login = prompt("Digite seu Login:")
// let senha = (prompt("Digite sua senha:"))

// senha === "123" ? console.log("Login efetuado com sucesso") : console.log("Usuario ou Senha invalidos")

let login = prompt("Digite seu Login:")
let senha = (prompt("Digite sua senha:"))
if (
    (login ==="adm"&& senha==="123")
    (login ==="adm2"&& senha==="234")
    (login ==="adm3"&& senha==="345")
){
    console.log("Login efetuado com sucesso")
}else{
    console.log("Usuario ou Senha invalidos")
}