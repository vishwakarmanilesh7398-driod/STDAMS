// Chart.js CDN loader and fallback
(function() {
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/chart.js';
    script.onload = function() {
        if (typeof Chart === 'undefined') {
            alert('Chart.js failed to load.');
        }
    };
    document.head.appendChild(script);
})();

// --- FULL JS FOR ALERTS HISTORY ---
function updateDashboardAlerts() {
    fetch('/api/alerts')
        .then(response => response.json())
        .then(data => {
            const alertContainer = document.getElementById('system-alerts'); 
            
            // Check if alert container exists to avoid errors
            if (!alertContainer) return;

            // Anomaly detect hone par logic
            if (data.level !== 'NORMAL' && data.type !== 'None') {
                
                const alertDiv = document.createElement('div');
                alertDiv.className = `alert-box ${data.level.toLowerCase()}`;
                
                // Style set karna taaki critical aur warning alag dikhein
                alertDiv.style.borderLeft = data.level === 'CRITICAL' ? '5px solid #ff0059' : '5px solid #ffe600';
                alertDiv.style.marginBottom = "10px";
                alertDiv.style.padding = "10px";
                alertDiv.style.background = "rgba(255, 255, 255, 0.05)";
                alertDiv.style.borderRadius = "5px";

                alertDiv.innerHTML = `
                    <h3 style="margin: 0; font-size: 1rem; color: #fff;">🚨 ${data.type} DETECTED</h3>
                    <p style="margin: 5px 0; font-size: 0.9rem;">${data.message}</p>
                    <small style="opacity: 0.6; font-size: 0.75rem;">Time: ${new Date().toLocaleTimeString()}</small>
                `;

                // Purana "Safe Message" hatana
                const safeMsg = alertContainer.querySelector('.safe-msg');
                if (safeMsg) safeMsg.remove();

                // Naya alert list mein sabse upar (Prepend)
                alertContainer.prepend(alertDiv);

                // History limit: Latest 5 alerts tak
                if (alertContainer.children.length > 5) {
                    alertContainer.removeChild(alertContainer.lastChild);
                }

                console.log("Anomaly Logged:", data.type);

            } else if (alertContainer.children.length === 0) {
                // Agar koi alert nahi hai toh safe message dikhana
                alertContainer.innerHTML = '<p class="safe-msg" style="color: #00ffe7;">✅ All Systems Operational</p>';
            }
        })
        .catch(error => console.error('Error fetching alerts:', error));
}

// Refresh interval - 2 seconds for better sync with simulator
setInterval(updateDashboardAlerts, 2000);