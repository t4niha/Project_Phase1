// Redirects to result.html with the URL as a parameter
function redirectToResultPage() {
    const articleUrl = document.getElementById("article-url").value;
    window.location.href = `/frontend/pages/results.html?articleUrl=${encodeURIComponent(articleUrl)}`;
}

// Extracts URL parameter and makes a prediction
async function displayPrediction() {
    const urlParams = new URLSearchParams(window.location.search);
    const articleUrl = urlParams.get('articleUrl');

    if (articleUrl) {
        // Call your prediction API (dummy function here)
        const bias = await predictBiasFromUrl(articleUrl);

        // Display the prediction result
        document.getElementById("result-box").style.display = "block";
        document.getElementById("prediction-result").innerText = bias;
    }
}

// Dummy prediction function (replace with actual API call)
async function predictBiasFromUrl(articleUrl) {
    // Replace with your actual model inference or API call logic
    // Here, just return "left", "right", or "center" for demo
    const biases = ["left", "right", "center"];
    return biases[Math.floor(Math.random() * biases.length)];
}

// Automatically run displayPrediction when on result page
if (window.location.pathname.includes("result.html")) {
    displayPrediction();
}
