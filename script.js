async function updating() {
    try {
        const response = await fetch(`systemdata.json?timestamp=${Date.now()}`, {
            cache: "no-store"
        });

        const data = await response.json();
        const texts = document.querySelectorAll(".Infotext");

        console.log(data)

        texts.forEach((text, index) => {
            const value = data[index];

            text.textContent =
                typeof value === "object"
                    ? JSON.stringify(value)
                    : String(value ?? "");
        });
    } catch (error) {
        console.error(error);
    }
}


const interval =setInterval(updating, 1000)