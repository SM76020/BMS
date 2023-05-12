const form = document.querySelector('form');

form.addEventListener('submit', (e) => {
  e.preventDefault();

  const accountNumber = document.getElementById('account').value;
  const amount = document.getElementById('amount').value;
  const pin = document.getElementById('pin').value;

  // Perform withdrawal logic here

  alert(`Withdrawal of ${amount} was successful`);
});
