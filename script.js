document.getElementById('predict-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = {
        GrLivArea: parseFloat(document.getElementById('GrLivArea').value),
        OverallQual: parseInt(document.getElementById('OverallQual').value),
        GarageCars: parseInt(document.getElementById('GarageCars').value),
        TotalBsmtSF: parseFloat(document.getElementById('TotalBsmtSF').value)
        // Add other fields as needed!
    };

    // Show loading message
    document.getElementById('result').textContent = 'Predicting...';

    try {
        // Replace '/predict' with your actual backend endpoint URL if different
        const response = await fetch('http://localhost:5000/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });
        const data = await response.json();

        if (response.ok && data.prediction) {
            document.getElementById('result').textContent = `Estimated Price: $${parseInt(data.prediction).toLocaleString()}`;
        } else {
            document.getElementById('result').textContent = 'Prediction failed. Please check your input or try again.';
        }
    } catch (error) {
        document.getElementById('result').textContent = 'Error connecting to server.';
    }
});
