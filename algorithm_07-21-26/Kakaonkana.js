// REAL LIFE EXAMPLE: KAKAON?
// Busog Ko, Hindi na ako mag kaon 
// Gutom Ko, Kaon na
// Pro kung nauhaw ka, Inom ka tubig

let busog = true;
let gutom = true;
let nauhaw = true;

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("Busog ka? (huo/indi): ", (answer) => {
    busog = answer.toLowerCase() === "huo";

    if (busog) {
        console.log("Hindi nako mag kaon.");
        rl.close();
    } else {
        rl.question("Gutom ka? (huo/indi): ", (answer) => {
            gutom = answer.toLowerCase() === "huo";
            
            if (gutom) {
                console.log("Kaon na!");
                rl.close();
            } else {
                rl.question("Nauhaw ka ba? (huo/indi): ", (answer) => {
                    nauhaw = answer.toLowerCase() === "huo";
                    
                    if (nauhaw) {
                        console.log("Inom ka tubig.");
                    } else {
                        console.log("Okay lang, indi ka gutom kag indi ka nauhaw.");
                    }
                    rl.close();
                });
            }
        });
    }
});