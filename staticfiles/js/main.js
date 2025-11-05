// static/js/main.js

console.log("Slooze Dashboard JavaScript loaded.");

// Firebase login popup
signInWithPopup(auth, provider)
  .then((result) => {
    const user = result.user;
    alert(`Welcome ${user.displayName}!`);
    console.log(user);
  })
  .catch((error) => {
    if (error.code === 'auth/popup-closed-by-user') {
      alert('Login cancelled. Please try again.');
    } else {
      console.error(error);
      alert('An error occurred. Check console.');
    }
  });

// Chart.js sales chart
document.addEventListener("DOMContentLoaded", () => {
  const ctx = document.getElementById("salesChart");
  if (ctx) {
    new Chart(ctx, {
      type: "bar",
      data: {
        labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep"],
        datasets: [{
          label: "Sales",
          data: [1200, 2400, 1800, 3000, 2600, 3100, 2800, 3400, 3900],
          backgroundColor: "rgba(54, 162, 235, 0.6)",
          borderRadius: 6
        }]
      },
      options: {
        plugins: {
          legend: { display: false }
        },
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
  }
});

