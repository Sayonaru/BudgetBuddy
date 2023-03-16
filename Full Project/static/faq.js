function faq1(){
    const p = document.getElementById("faq1");
    if (p.children.length < 2){
        const pans = document.createElement("p");
        pans.innerHTML = "The protection of user data is very important to us, due to this we have used a number of techniques to ensure security of your data. We are compliant with GDPR . "
        p.appendChild(pans);
    } else if (p.children.length = 2) {
        const c = p.childNodes[2]
        p.removeChild(c)
    }
}

function faq2(){
    const p = document.getElementById("faq2");
    if (p.children.length < 2){
        const pans = document.createElement("p");
        pans.innerHTML = "We are constantly working on improving our current services and consider all suggestions given, you can leave your suggestion by contacting us."
        p.appendChild(pans);
    } else if (p.children.length = 2) {
        const c = p.childNodes[2]
        p.removeChild(c)
    }
}
