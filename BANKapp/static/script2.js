const editUsername = document.querySelector('#edit-fullname');
const editaccount_number = document.querySelector('#edit-account_number');
const editEmail = document.querySelector('#edit-email');
const editphonenumber = document.querySelector('#edit-phonenumber');
const editaddress = document.querySelector('#edit-address');
const editpincode = document.querySelector('#edit-pincode');
const editdob = document.querySelector('#edit-dob');
// const editdob = document.querySelector('#edit-dob');
// const editPassword = document.querySelector('#edit-password');

editUsername.addEventListener('click', () => {
  const usernameInput = document.querySelector('#fullname');
  usernameInput.removeAttribute('disabled');
  usernameInput.focus();
});


editaccount_number.addEventListener('click', () => {
    const account_numberInput = document.querySelector('#account_number');
    account_numberInput.removeAttribute('disabled');
    account_numberInput.focus();
  });

editEmail.addEventListener('click', () => {
  const emailInput = document.querySelector('#email');
  emailInput.removeAttribute('disabled');
  emailInput.focus();
});

editphonenumber.addEventListener('click', () => {
    const phonenumberInput = document.querySelector('#phonenumber');
    phonenumberInput.removeAttribute('disabled');
   phonenumberInput.focus();
  });

editaddress.addEventListener('click', () => {
    const addressInput = document.querySelector('#address');
    addressInput.removeAttribute('disabled');
    addressInput.focus();
  });

editpincode.addEventListener('click', () => {
    const pincodeInput = document.querySelector('#pincode');
    pincodeInput.removeAttribute('disabled');
    pincodeInput.focus();
  });

editdob.addEventListener('click', () => {
    const dobInput = document.querySelector('#dob');
    dobInput.removeAttribute('disabled');
    dobInput.focus();
  });

// editaccount_number.addEventListener('click', () => {
//     const account_numberInput = document.querySelector('#account_number');
//     account_numberInput.removeAttribute('disabled');
//     account_numberInput.focus();
//   });







// editPassword.addEventListener('click', () => {
//   const passwordInput = document.querySelector('#password');
//   passwordInput.removeAttribute('disabled');
//   passwordInput.focus();
// });
