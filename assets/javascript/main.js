// let style = document.querySelector("#cat2 h1")
// let styl = document.querySelector("#cat2 img")
// let cat_id = document.querySelector("#cat2 h3")

// document.querySelectorAll(".cat > a").forEach((item) => {
//     item.addEventListener("click", function(event) {
//         event.preventDefault()
//         style.innerText = item.innerText
//         styl.setAttribute('src', item.getAttribute("data-src"))
//         styl.classList.remove("d-none")
//         cat_id.innerText = item.getAttribute("c-id")
//         document.querySelector("#cat2 h5").innerHTML = item.getAttribute("href")
//     })
// })




// $(".cat > a, #cat2 a, .ggg > a").on("click", function() {
//     load_data($(this).attr("href"))
//     return false
// })


// document.querySelectorAll(".cat > a, #cat2, .ggg a").forEach((item)=>{
//     item.addEventListener("click",function(e){
//         load_data($(this).attr("href"))

//         e.preventDefault();
//     })
// })


// function load_data(url) {

//     fetch(url + "?is_ajax=1").then(r => r.text()).then((data) => {
//       window.history.pushState({}, "", url)
//       $("#ppp").html(data).children("a").on("click", function () {
//         load_data($(this).attr("href"))

//         return false;
//       })
//     })
//   }


function load_data(url) {
    // $("#cat2").html("Loading ...")

    fetch(url + "?is_ajax=1").then(r => r.text()).then((data) => {
        //document.title = response.pageTitle;
        window.history.pushState({}, "", url)

        $("#ppp").html(data).children("a").on("click", function () {
            load_data($(this).attr('href'))
            return false;
        })
    });
}

document.querySelectorAll(".cat > a, #ppp a, .ccc > a").forEach((item) => {
    item.addEventListener("click", function (e) {
        load_data($(this).attr("href"))

        e.preventDefault();
    })

})