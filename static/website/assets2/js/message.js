let id = (id) => document.getElementById(id);

let classes = (classes) => document.getElementsByClassName(classes);

let username = id("name"),
  phone = id("phone"),
  email = id("email-form"),  
  form = id("message-form"),
  
  errorMsg = classes("error"),
  successIcon = classes("success-icon"),
  failureIcon = classes("failure-icon");


let engine = (id, serial, message) => {

if (id.value.trim() === "") {
    errorMsg[serial].innerHTML = message;
} 

else {
    errorMsg[serial].innerHTML = "";
}
}

// form.addEventListener("submit", (e) => {
//     e.preventDefault();
//     console.log("hey!");
  
//     engine(name, 0, "Name cannot be blank");
//     engine(email, 1, "Email cannot be blank");
//     engine(text_message, 2, "Text message cannot be blank");
//   });

function toggleLoader() {
    const loader = document.getElementById('loader')
    loader.classList.toggle('hidden')
  }


document.addEventListener("DOMContentLoaded", function(){
    // let btn = document.querySelector('button[type="submit"]');    
    // btn.addEventListener("click", async function(event){
    form.addEventListener("submit", async function(event) {        
        event.preventDefault();
        if (username.value.trim() === "" || phone.value.trim() === "" || email.value.trim() === "") {
            engine(username, 0, "Поле Имя не может быть пустым") &
            engine(phone, 1, "Поле Телефон не может быть пустым") &
            engine(email, 2, "Поле Email не может быть пустым")
        } else {
            engine(username, 0, "");
            engine(phone, 1, "");
            engine(email, 2, "");
            toggleLoader()        
            console.log("Helllllooooo!!!");
            let response = await fetch("/", {
                method: "POST",
                body: new FormData(document.querySelector("form"))          
            });
            toggleLoader()
            document.querySelector('form').reset()
            message_success = '<h6 class="alert alert-info">Спасибо! Мы получили ваше сообщение и ответим в ближайшее время...</h6>'        

            // alert("Thanks! We received your message and will respond shortly...");

            function sleep(ms) {
            return new Promise(resolve => setTimeout(resolve, ms));
            }

            async function delayedMessage() {
            document.querySelector(".messages").innerHTML = message_success;
            await sleep(30000);
            document.querySelector(".messages").innerHTML = "";          
            }

            delayedMessage();

        }
        
        
      
    //   let response_text = await response.text();  // text
    //   console.log('response_text is', response_text);

    //   let response_json = await response.json();  // json
    //   console.log(response_json);
    })
  })