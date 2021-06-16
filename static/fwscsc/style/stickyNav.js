let header = document.querySelector("header")
let nav = document.querySelector("header nav")
let logo = document.querySelector("header nav div a")
let aTag = document.getElementsByClassName("toWhite")
let dropDownATag = document.getElementsByClassName("stay-grey")

console.log(dropDownATag)
console.log(aTag)


logo.src = "{% static 'fwscsc/img/logo中文 1.png'%}"

window.addEventListener("scroll", e => {
    if (window.pageYOffset != 0) {
        header.style.backgroundColor = "rgba(0, 0, 0, 0.4)";
        header.style.top = "0";
        header.style.position = "sticky";
        header.style.zIndex = "9999";
        logo.remove();
        Array.from(document.getElementsByClassName('toWhite')).forEach(a => {
            a.style.color = "white";
        })
        Array.from(document.getElementsByClassName('stay-grey')).forEach(a => {
            a.style.color = "#7a7a7a";
        })
        // aTag.forEach(a => {
        //     a.style.color = "white";
        // })
        // dropDownATag.forEach(a => {
        //     a.style.color = "#7a7a7a";
        // })

    } else {
        header.style = "";
        nav.style = "";
        document.getElementById("addImg").appendChild(logo)
        // document.getElementById("stayGrey").style = "";
        Array.from(document.getElementsByClassName('toWhite')).forEach(a => {
            a.style.color = "";
        })
        // aTag.forEach(a => {
        //     a.style.color = "";
        // })
    }
})
