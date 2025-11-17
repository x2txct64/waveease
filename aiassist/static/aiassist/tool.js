document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("teach-form");
    const outputDiv = document.querySelector(".output");

    form.addEventListener("submit", function(e) {
        e.preventDefault();

        // Create loading screen
        const loading = document.createElement("div");
        loading.className = "dynamic-loading";
        loading.innerHTML = '<div class="spinner"></div>';
        document.body.appendChild(loading);

        const formData = new FormData(form);

        fetch(form.action, {
            method: "POST",
            body: formData,
            headers: {
                "X-Requested-With": "XMLHttpRequest"
            }
        })
        .then(response => response.text())
        .then(html => {
            // Remove loading screen
            document.body.removeChild(loading);

            // Insert AI-generated output
            outputDiv.innerHTML = html;
        })
        .catch(err => {
            console.error(err);
            document.body.removeChild(loading);
            alert("Error occurred, try again.");
        });
    });
});