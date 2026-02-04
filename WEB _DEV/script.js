let count = 0;

const Button = document.getElementById("myBtn");
const msg= document.getElementById("message");
const timePara = document.getElementById("time");
const greetingPara = document.getElementById("greeting");

function updateGreeting() {
    const hour = new Date().getHours();
    const name = "Shreyansh Gupta";

    if (hour < 12) {
        greetingPara.textContent = `Good Morning, ${name}!`;
        greetingPara.style.color = "gold";
        document.body.style.backgroundColor = "#FFF9C4";
    }  
    else if (hour < 18) {
        greetingPara.textContent = `Good Afternoon, ${name}!`;
        greetingPara.style.color = "orange";
        document.body.style.backgroundColor = "#FFE0B2";
    }
     else {
        greetingPara.textContent = `Good Evening, ${name}!`;
        greetingPara.style.color = "darkblue";
        document.body.style.backgroundColor = "#BBDEFB";
    }
}
updateGreeting();
setInterval(updateGreeting, 60000);

let clockInterval = null;
const clock = document.getElementById("liveClock");
const startBtn = document.getElementById("startClock");
const stopBtn = document.getElementById("stopClock");

startBtn.addEventListener("click", () =>{
    if (!clockInterval) {
        clockInterval = setInterval(() =>{
            clock.textContent = new Date().toLocaleTimeString();
    }, 1000);
    startBtn.disabled = true;
    stopBtn.disabled = false;
    }
});
    
stopBtn.addEventListener("click", () => {
    clearInterval(clockInterval);
    clockInterval = null;

    startBtn.disabled = false;
    stopBtn.disabled = true;
});


Button.addEventListener("click", () =>{
    count++;

    const currentTime = new Date().toLocaleTimeString();
    msg.textContent = `Button clicked ${count} times`;
    timePara.textContent = `Current Time: ${currentTime}`;
});