// # ----- static/js/script.js -----
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('prediction-form');
    const resultsContainer = document.getElementById('results-container');
    const predictionResult = document.getElementById('prediction-result');
    
    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Récupérer les valeurs du formulaire
        const feature1 = parseFloat(document.getElementById('feature1').value);
        const feature2 = parseFloat(document.getElementById('feature2').value);
        const feature3 = parseFloat(document.getElementById('feature3').value);
        
        // Préparer les données pour l'API
        const data = {
            feature1: feature1,
            feature2: feature2,
            feature3: feature3
        };
        
        try {
            // Faire la requête à l'API
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data)
            });
            
            // Traiter la réponse
            if (response.ok) {
                const result = await response.json();
                
                if (result.success) {
                    // Afficher la prédiction
                    predictionResult.innerHTML = `
                        <p><strong>Prédiction:</strong> ${result.prediction}</p>
                    `;
                    
                    // Afficher les résultats
                    resultsContainer.style.display = 'block';
                    
                    // Ici, vous pourriez ajouter du code pour visualiser les résultats
                    // avec des bibliothèques comme Chart.js, D3.js, etc.
                } else {
                    alert(`Erreur: ${result.error}`);
                }
            } else {
                alert('Erreur lors de la communication avec le serveur');
            }
        } catch (error) {
            console.error('Erreur:', error);
            alert('Erreur lors de la prédiction');
        }
    });
});