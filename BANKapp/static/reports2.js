const depositsTable = document.getElementById('deposits-table');

// Replace this with your deposit data
const depositData = [  { accountNumber: '123456', amount: 1000, date: '2022-04-25' },  { accountNumber: '234567', amount: 2000, date: '2022-04-26' },  { accountNumber: '345678', amount: 500, date: '2022-04-27' },  { accountNumber: '456789', amount: 1500, date: '2022-04-28' },  { accountNumber: '567890', amount: 3000, date: '2022-04-29' }];

// Loop through the deposit data and add it to the table
for (let i = 0; i < depositData.length; i++) {
  const depositRow = `
    <tr>
      <td>${depositData[i].accountNumber}</td>
      <td>${depositData[i].amount}</td>
      <td>${depositData[i].date}</td>
    </tr>
  `;
  depositsTable.innerHTML += depositRow;
}

