let features = [];
        
        function showTab(tabName) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active'));
            document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
            
            document.getElementById(tabName).classList.add('active');
            document.querySelector(`[onclick="showTab('${tabName}')"]`).classList.add('active');
        }

        document.getElementById('upload-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData();
            const file = document.getElementById('file').files[0];
            const target = document.getElementById('target').value;
            
            formData.append('file', file);
            formData.append('target', target);
            
            try {
                const response = await fetch('/upload', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    features = data.features.filter(f => f !== target);
                    document.getElementById('upload-message').innerHTML = 
                        `<div class="success">${data.message}</div>`;
                    createFeatureInputs(features);
                } else {
                    document.getElementById('upload-message').innerHTML = 
                        `<div class="error">${data.error}</div>`;
                }
            } catch (error) {
                document.getElementById('upload-message').innerHTML = 
                    `<div class="error">Error uploading file</div>`;
            }
        });

        document.getElementById('file').addEventListener('change', async (e) => {
            const file = e.target.files[0];
            if (file) {
                const formData = new FormData();
                formData.append('file', file);
                
                try {
                    const response = await fetch('/upload', {
                        method: 'POST',
                        body: formData
                    });
                    
                    const data = await response.json();
                    
                    if (response.ok) {
                        const targetSelect = document.getElementById('target');
                        targetSelect.innerHTML = '';
                        data.features.forEach(feature => {
                            const option = document.createElement('option');
                            option.value = feature;
                            option.textContent = feature;
                            targetSelect.appendChild(option);
                        });
                        document.getElementById('target-select').style.display = 'block';
                    }
                } catch (error) {
                    document.getElementById('upload-message').innerHTML = 
                        `<div class="error">Error reading file</div>`;
                }
            }
        });

        document.getElementById('train-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const modelType = document.getElementById('model-type').value;
            
            try {
                const response = await fetch('/train', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ model_type: modelType })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    document.getElementById('train-message').innerHTML = 
                        `<div class="success">${data.message}</div>`;
                    
                    // Display metrics
                    const metricsHtml = `
                        <h3>Model Performance Metrics</h3>
                        <p>Accuracy: ${(data.metrics.accuracy * 100).toFixed(2)}%</p>
                        <p>Precision: ${(data.metrics.precision * 100).toFixed(2)}%</p>
                        <p>Recall: ${(data.metrics.recall * 100).toFixed(2)}%</p>
                        <p>F1 Score: ${(data.metrics.f1_score * 100).toFixed(2)}%</p>
                    `;
                    document.getElementById('metrics').innerHTML = metricsHtml;
                } else {
                    document.getElementById('train-message').innerHTML = 
                        `<div class="error">${data.error}</div>`;
                }
            } catch (error) {
                document.getElementById('train-message').innerHTML = 
                    `<div class="error">Error training model</div>`;
            }
        });

        function createFeatureInputs(features) {
            const container = document.getElementById('feature-inputs');
            container.innerHTML = '';
            
            features.forEach(feature => {
                const div = document.createElement('div');
                div.className = 'form-group';
                
                const label = document.createElement('label');
                label.htmlFor = feature;
                label.textContent = feature;
                
                const input = document.createElement('input');
                input.type = 'number';
                input.id = feature;
                input.name = feature;
                input.required = true;
                input.step = 'any';
                
                div.appendChild(label);
                div.appendChild(input);
                container.appendChild(div);
            });
        }

        document.getElementById('predict-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const featureInputs = {};
            features.forEach(feature => {
                featureInputs[feature] = parseFloat(document.getElementById(feature).value);
            });
            
            try {
                const response = await fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ features: featureInputs })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    const resultHtml = `
                        <div class="success">
                            <h3>Prediction Result</h3>
                            <p>Downtime Prediction: ${data.prediction}</p>
                            <p>Confidence: ${(data.confidence * 100).toFixed(2)}%</p>
                        </div>
                    `;
                    document.getElementById('predict-message').innerHTML = resultHtml;
                } else {
                    document.getElementById('predict-message').innerHTML = 
                        `<div class="error">${data.error}</div>`;
                }
            } catch (error) {
                document.getElementById('predict-message').innerHTML = 
                    `<div class="error">Error making prediction</div>`;
            }
        });
        document.getElementById('generate-data-btn').addEventListener('click', async () => {
    try {
        // Generate the data by calling the backend
        const response = await fetch('/generate-data', {
            method: 'POST',
        });

        if (response.ok) {
            // Process the response and trigger the download
            const data = await response.blob(); // Get the response as a Blob (file)
            const link = document.createElement('a');
            link.href = URL.createObjectURL(data);
            link.download = 'synthetic_manufacturing_data.csv';  // File name to download
            link.click();  // Trigger the download
        } else {
            const error = await response.json();
            throw new Error(error.error || 'Error generating data');
        }
    } catch (error) {
        document.getElementById('upload-message').innerHTML =
            `<div class="error">${error.message || 'Error generating and downloading synthetic data'}</div>`;
    }
});