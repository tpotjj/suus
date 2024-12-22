document.addEventListener("DOMContentLoaded", function () {
    const snowContainer = document.querySelector(".snow-container");
    const poemContainer = document.querySelector(".poem-container");

    const particlesPerThousandPixels = 0.1;
    const fallSpeed = 0.75;
    const pauseWhenNotActive = true;
    const maxSnowflakes = 200;
    const snowflakes = [];
    const clickedIcons = new Set();

    const poemLines = [
        "Aller liefste Suus,",
        "De papieren gedichten zullen al snel vergaan,",
        "maar dit technisch ingestoken stukje poetisch epos, blijft langer bestaan.",
        "Een vleugje attentie van jou is hierbij onontbeerlijk,",
        "geen zorgen, dit kan met een glas wijn vanuit je luie stoel, heerlijk.",
        "Zie hoe op het scherm, iconen neerdwarrelen als in een winters tafereel,",
        "Klik op de iconen en genereer het gedicht manueel.",
    ];

    const icons = [
        "./media/renesse.png",
    ];

    let currentLine = 0;

    function revealNextLine() {
        if (currentLine < poemLines.length) {
            const lineElement = document.createElement("div");
            lineElement.textContent = poemLines[currentLine];
            lineElement.classList.add("falling-line");
            poemContainer.appendChild(lineElement);

            lineElement.style.left = `${Math.random() * 80}vw`;
            currentLine++;
        }
    }

    let poemInterval = setInterval(() => {
        if (currentLine < poemLines.length) {
            requestAnimationFrame(revealNextLine);
        } else {
            clearInterval(poemInterval);
            setTimeout(displayIcons, 3000);
        }
    }, 3000);

    function displayIcons() {
        const shuffledIcons = icons.sort(() => Math.random() - 0.5);
    
        shuffledIcons.forEach((iconPath) => {
            if (!clickedIcons.has(iconPath)) {
                displaySingleIcon(iconPath);
            }
        });
    }

    function displayIcons() {
        const shuffledIcons = icons.sort(() => Math.random() - 0.5);
    
        shuffledIcons.forEach((iconPath, index) => {
            const iconElement = document.createElement("img");
            iconElement.src = iconPath;
            iconElement.classList.add("falling-icon");
            iconElement.style.left = `${Math.random() * 80}vw`;
    
            iconElement.addEventListener("click", async () => {
                try {
                    // Make the API request
                    const response = await fetch("http://127.0.0.1:8000/get-llm-response-for-suus/", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            prompt: "Suus gaat graag naar Renesse, een weekend, een week of zelfs meer. Met Ger en Guus als buren is dat altijd een feestje & gezellig. Op het strand wandelen met loes, zonnen bij de kotjes of fietsen zijn o.a. activiteiten die ze graag doen. Daarnaast gaan ze ook graag een lekker hapje eten bij de nodige leuke restaurantjes in Renesse en omgeving.",
                        }),
                    });
            
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
            
                    // Parse the JSON response
                    const responseData = await response.json();
                    console.log("RESPONSE DATA: ", responseData);
            
                    // Extract the poem lines
                    const poemLines = responseData.poem_lines;
            
                    // Handle the poem lines (display them, log them, etc.)
                    if (poemLines) {
                        console.log("Poem Lines:", poemLines.join("\n")); // Logs the poem as a single block of text
            
                        // Example: Append the poem lines to an element in the DOM
                        const poemElement = document.createElement("div");
                        poemElement.classList.add("poem");
                        poemElement.textContent = poemLines.join("\n");
                        document.body.appendChild(poemElement); // Adds the poem to the page
                    } else {
                        console.error("No poem lines found in the response!");
                    }
            
                    // Trigger the fading animation
                    iconElement.classList.add("fading-out");
            
                    iconElement.addEventListener("animationend", () => {
                        iconElement.remove();
                    });
            
                    clickedIcons.add(iconPath);
            
                } catch (error) {
                    console.error("Error fetching the poem:", error);
                }
            });
            
    
            document.body.appendChild(iconElement);
    
            iconElement.style.animation = "text-fall 10s linear forwards";
    
            setTimeout(() => {
                if (icons.includes(iconPath) && !document.hidden) {
                    displaySingleIcon(iconPath);
                }
            }, 10000);
        });
    }

    function displaySingleIcon(iconPath) {
        const iconElement = document.createElement("img");
        iconElement.src = iconPath;
        iconElement.classList.add("falling-icon");
        iconElement.style.left = `${Math.random() * 80}vw`;
    
        // Add a click event listener with fade-out
        iconElement.addEventListener("click", () => {
            alert(`You clicked on ${iconPath}!`);
    
            // Mark the icon as clicked to avoid duplicates
            clickedIcons.add(iconPath);
    
            // // Add fade-out class
            // iconElement.classList.add("fading-out");
    
            // // Wait for the animation to finish before removing the element
            // iconElement.addEventListener("animationend", () => {
            //     iconElement.remove(); // Remove the element after fade-out
            // });
        });
    
        document.body.appendChild(iconElement);
    
        // Set animation for the icon falling
        iconElement.style.animation = "text-fall 10s linear forwards";
    
        // Allow the icon to fall again if not clicked
        setTimeout(() => {
            if (!clickedIcons.has(iconPath) && !document.hidden) {
                displaySingleIcon(iconPath); // Make it fall again if not clicked
            }
        }, 10000); // Match the animation duration (10s)
    }

    let snowflakeInterval;
    let isTabActive = true;

    function resetSnowflake(snowflake) {
        const size = Math.random() * 5 + 1;
        const viewportWidth = window.innerWidth - size;
        const viewportHeight = window.innerHeight;

        snowflake.style.width = `${size}px`;
        snowflake.style.height = `${size}px`;
        snowflake.style.left = `${Math.random() * viewportWidth}px`;
        snowflake.style.top = `-${size}px`;

        const animationDuration = (Math.random() * 3 + 2) / fallSpeed;
        snowflake.style.animationDuration = `${animationDuration}s`;
        snowflake.style.animationTimingFunction = "linear";
        snowflake.style.animationName =
            Math.random() < 0.5 ? "fall" : "diagonal-fall";

        setTimeout(() => {
            if (parseInt(snowflake.style.top, 10) < viewportHeight) {
                resetSnowflake(snowflake);
            } else {
                snowflake.remove();
            }
        }, animationDuration * 1000);
    }

    function createSnowflake() {
        if (snowflakes.length < maxSnowflakes) {
            const snowflake = document.createElement("div");
            snowflake.classList.add("snowflake");
            snowflakes.push(snowflake);
            snowContainer.appendChild(snowflake);
            resetSnowflake(snowflake);
        }
    }

    function generateSnowflakes() {
        const numberOfParticles =
            Math.ceil((window.innerWidth * window.innerHeight) / 1000) *
            particlesPerThousandPixels;
        const interval = 5000 / numberOfParticles;

        clearInterval(snowflakeInterval);
        snowflakeInterval = setInterval(() => {
            if (isTabActive && snowflakes.length < maxSnowflakes) {
                requestAnimationFrame(createSnowflake);
            }
        }, interval);
    }

    function handleVisibilityChange() {
        if (!pauseWhenNotActive) return;

        isTabActive = !document.hidden;
        if (isTabActive) {
            generateSnowflakes();
        } else {
            clearInterval(snowflakeInterval);
        }
    }

    generateSnowflakes();

    window.addEventListener("resize", () => {
        clearInterval(snowflakeInterval);
        setTimeout(generateSnowflakes, 1000);
    });

    document.addEventListener("visibilitychange", handleVisibilityChange);
});


// TODO: 