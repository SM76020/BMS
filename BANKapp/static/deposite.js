const form = document.querySelector("form");
      form.addEventListener("submit", handleSubmit);

      function handleSubmit(event) {
        event.preventDefault();
        const accountNumber = document.getElementById("account-number").value;
        const depositAmount = document.getElementById("deposit-amount").value;
        const depositDate = document.getElementById("deposit-date").value;
        const depositMethod = document.getElementById("deposit-method").value;

        // Code to submit the form data to the server goes here
        console.log({
          accountNumber,
          depositAmount,
          depositDate,
          depositMethod,
        });
      }