document.addEventListener("DOMContentLoaded", function () {
    const snowContainer = document.querySelector(".snow-container");
    const poemContainer = document.querySelector(".poem-container");

    const particlesPerThousandPixels = 0.1;
    const fallSpeed = 0.75;
    const pauseWhenNotActive = true;
    const maxSnowflakes = 200;
    const snowflakes = [];

    const poemLines = [
        "Aller liefste Suus,",
        "De papieren gedichten zullen al snel vergaan,",
        "maar dit technisch ingestoken stukje poetisch epos, blijft langer bestaan.",
        "Een vleugje attentie van jou is hierbij onontbeerlijk,",
        "geen zorgen, dit kan met een glas wijn vanuit je luie stoel, heerlijk.",
        "Zie hoe op het scherm, iconen neerdwarrelen als in een winters tafereel,",
        "Klik op de iconen en genereer het gedicht manueel.",
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
        }
    }, 3000);

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