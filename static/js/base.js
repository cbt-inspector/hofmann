

var dark
let cookies = false

function darkmode() {

    var element = document.body;
    element.classList.toggle("dark");



    if (dark != true){

    if (cookies){
        Cookies.set('darkmode','true')
    }
    document.getElementById("darkbutton").innerHTML = "<img src=\"/static/assets/light.png\" class=\"darkswitchpic\">"

    document.getElementById("navicon").backgroundColor = "white"
    dark = true

    } else {
    if (cookies){
        Cookies.remove('darkmode')
    }
    dark = false
    document.getElementById("darkbutton").innerHTML = "<img src=\"/static/assets/dark.png\" class=\"darkswitchpic\">"

    }

    //window.location.reload()

}

function recoverDark() {

    //let cookie = document.cookie

    if(Cookies.get("cookies")=="true"){
        cookies=true
    }

    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches && darkmode === false){
        darkmode()
    }


    if(Cookies.get('darkmode') == "true"){
        var element = document.body;
        element.classList.toggle("dark");

        document.getElementById("darkbutton").innerHTML = "<img src=\"/static/assets/light.png\" class=\"darkswitchpic\">"

        dark = true
    }
    else {
        dark = false

    }

}

function togglePopup(){

    var popup = document.getElementById("Popup");
    popup.classList.toggle("show");

}

function acceptCookies(){
    togglePopup()

    Cookies.set('cookies', 'true')

    cookies=true
}

function onLoad(){
    recoverDark()

    if(!cookies){
        togglePopup()
    }
}
