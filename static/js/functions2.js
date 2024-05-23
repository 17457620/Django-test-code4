    function checkForm(theForm) {
      var invalid = false;

      // Validate name
      if (requiredFieldEmpty(theForm.name)) {
        document.getElementById("nameError").textContent = "Please enter employee's name.";
        document.getElementById("nameError").style.display = 'inline';
        invalid = true;
      } else {
        document.getElementById("nameError").style.display = 'none';
      }

      
        // Validate employeeID
        if (requiredFieldEmpty(theForm.employeeID)) {
        document.getElementById("employeeIDError").textContent = 'Please enter employeeID';
        document.getElementById("employeeIDError").style.display = 'inline';
        invalid = true;
      } else {
        document.getElementById("employeeIDError").style.display = 'none';
      }

        // Validate position
        if (requiredFieldEmpty(theForm.position)) {
        document.getElementById("positionError").textContent = "Please enter employee's position";
        document.getElementById("positionError").style.display = 'inline';
        invalid = true;
        } else {
        document.getElementById("positionError").style.display = 'none';
        }

        // Validate review date
        if (requiredFieldEmpty(theForm.reviewdate)) {
            document.getElementById("reviewdateError").textContent = "Please set review date";
            document.getElementById("reviewdateError").style.display = 'inline';
            invalid = true;
            } else {
            document.getElementById("reviewdateError").style.display = 'none';
            }

        // Validate review time
        if (requiredFieldEmpty(theForm.reviewtime)) {
            document.getElementById("reviewtimeError").textContent = "Please set review time";
            document.getElementById("reviewtimeError").style.display = 'inline';
            invalid = true;
            } else {
            document.getElementById("reviewtimeError").style.display = 'none';
            }

        // Validate Job Knowledge
        if (requiredFieldEmpty(theForm.job_knowledge)) {
            document.getElementById("job_knowledgeError").textContent = "Select Job Knowledge rating";
            document.getElementById("job_knowledgeError").style.display = 'inline';
            invalid = true;
            } else {
            document.getElementById("job_knowledgeError").style.display = 'none';
            }

        // Validate Work Quality
        if (requiredFieldEmpty(theForm.work_quality)) {
            document.getElementById("work_qualityError").textContent = "Select Work Quality rating";
            document.getElementById("work_qualityError").style.display = 'inline';
            invalid = true;
            } else {
            document.getElementById("work_qualityError").style.display = 'none';
            }

        // Validate Initiative
        if (requiredFieldEmpty(theForm.initiative)) {
            document.getElementById("initiativeError").textContent = "Select Initiative rating";
            document.getElementById("initiativeError").style.display = 'inline';
            invalid = true;
            } else {
            document.getElementById("initiativeError").style.display = 'none';
            }

        // Validate Communication
        if (requiredFieldEmpty(theForm.communication)) {
            document.getElementById("communicationError").textContent = "Select Communication rating";
            document.getElementById("communicationError").style.display = 'inline';
            invalid = true;
            } else {
            document.getElementById("communicationError").style.display = 'none';
            }

        // Validate Dependability
        if (requiredFieldEmpty(theForm.dependability)) {
            document.getElementById("dependabilityError").textContent = "Select Dependability rating";
            document.getElementById("dependabilityError").style.display = 'inline';
            invalid = true;
            } else {
            document.getElementById("dependabilityError").style.display = 'none';
            }
      
      

        if (invalid) {
            document.getElementById("form-error").style.display = "inline";
            document.getElementById("submitButtonError").style.display = "inline"; // Show submit button error message
            return false; // Do not allow form to submit
        }

      return true; //Allows form to submit
    }

    function requiredFieldEmpty(element) {
      return !element.value.trim();
    }

    
    function checkName(inputElement) {
        var errorMessageElement = inputElement.nextElementSibling; // Get the next sibling, which should be the error message element
        
        if (inputElement.value.trim() === '') {
            inputElement.style.border = "3px solid red"; // Change border color to red
            errorMessageElement.textContent = 'Please enter a name'; // Set error message
            errorMessageElement.style.color = 'red'; // Set error message color
            errorMessageElement.style.display = 'inline'; // Show the error message
        } else if (/\d/.test(inputElement.value.trim())) { // Check if input contains any number
            inputElement.style.border = "3px solid red"; // Change border color to red
            errorMessageElement.textContent = 'Please use letters only'; // Set error message for numbers
            errorMessageElement.style.color = 'red'; // Set error message color
            errorMessageElement.style.display = 'inline'; // Show the error message
        } else {
            inputElement.style.border = ''; // Reset border color
            errorMessageElement.textContent = ''; // Clear error message
            errorMessageElement.style.display = 'none'; // Hide the error message
        }
    }

    function checkPosition(inputElement) {
        var errorMessageElement = inputElement.nextElementSibling; // Get the next sibling, which should be the error message element
        
        if (inputElement.value.trim() === '') {
            inputElement.style.border = "3px solid red"; // Change border color to red
            errorMessageElement.textContent = 'Please enter a position'; // Set error message
            errorMessageElement.style.color = 'red'; // Set error message color
            errorMessageElement.style.display = 'inline'; // Show the error message
        } else {
            inputElement.style.border = ''; // Reset border color
            errorMessageElement.textContent = ''; // Clear error message
            errorMessageElement.style.display = 'none'; // Hide the error message
        }
    }

    function checkRD(inputElement) {
        var errorMessageElement = inputElement.nextElementSibling; // Get the next sibling, which should be the error message element
        
        if (inputElement.value.trim() === '') {
            inputElement.style.border = "3px solid red"; // Change border color to red
            errorMessageElement.textContent = 'Please select a date'; // Set error message
            errorMessageElement.style.color = 'red'; // Set error message color
            errorMessageElement.style.display = 'inline'; // Show the error message
        } else {
            inputElement.style.border = ''; // Reset border color
            errorMessageElement.textContent = ''; // Clear error message
            errorMessageElement.style.display = 'none'; // Hide the error message
        }
    }

    function checkRT(inputElement) {
        var errorMessageElement = inputElement.nextElementSibling; // Get the next sibling, which should be the error message element
        
        if (inputElement.value.trim() === '') {
            inputElement.style.border = "3px solid red"; // Change border color to red
            errorMessageElement.textContent = 'Please enter a time'; // Set error message
            errorMessageElement.style.color = 'red'; // Set error message color
            errorMessageElement.style.display = 'inline'; // Show the error message
        } else {
            inputElement.style.border = ''; // Reset border color
            errorMessageElement.textContent = ''; // Clear error message
            errorMessageElement.style.display = 'none'; // Hide the error message
        }
    }
    
    
    function checkValue(number) {
        var errorMessageElement = document.getElementById("employeeIDError"); // Get the error message element
        
        if (isNaN(number.value.trim())) {
            errorMessageElement.textContent = "Enter numbers only"; // Set error message
            errorMessageElement.style.color = "red"; // Set error message color
            errorMessageElement.style.display = "inline"; // Show the error message
            number.style.border = "2px solid red"; // Apply red border
        } else if (number.value.trim().length === 0) {
            errorMessageElement.textContent = "Please input a number"; // Set error message for empty input
            errorMessageElement.style.color = "red"; // Set error message color
            errorMessageElement.style.display = "inline"; // Show the error message
            number.style.border = "2px solid red"; // Apply red border
        } else {
            errorMessageElement.textContent = ""; // Clear error message
            errorMessageElement.style.display = "none"; // Hide the error message
            number.style.border = ""; // Reset border
        }
    }

    function checkEmployeeID(inputElement) {
        var errorMessageElement = inputElement.nextElementSibling; // Get the next sibling, which should be the error message element
        
        if (inputElement.value.trim() === '') {
            inputElement.style.border = "3px solid red"; // Change border color to red
            errorMessageElement.textContent = 'Please enter an emloyeeID'; // Set error message
            errorMessageElement.style.color = 'red'; // Set error message color
            errorMessageElement.style.display = 'inline'; // Show the error message
        } else {
            inputElement.style.border = ''; // Reset border color
            errorMessageElement.textContent = ''; // Clear error message
            errorMessageElement.style.display = 'none'; // Hide the error message
        }
    }

    /*
    function checkJobK(inputElement) {
        var errorMessageElement = inputElement.nextElementSibling; // Get the next sibling, which should be the error message element
        
        if (inputElement.value.trim() === '') {
            inputElement.style.border = "3px solid red"; // Change border color to red
            errorMessageElement.textContent = 'Select Job Knowledge rating'; // Set error message
            errorMessageElement.style.color = 'red'; // Set error message color
            errorMessageElement.style.display = 'inline'; // Show the error message
        } else if (/\d/.test(inputElement.value.trim())) { // Check if input contains any number
            inputElement.style.border = "3px solid red"; // Change border color to red
            errorMessageElement.textContent = 'Please use letters only'; // Set error message for numbers
            errorMessageElement.style.color = 'red'; // Set error message color
            errorMessageElement.style.display = 'inline'; // Show the error message
        } else {
            inputElement.style.border = ''; // Reset border color
            errorMessageElement.textContent = ''; // Clear error message
            errorMessageElement.style.display = 'none'; // Hide the error message
        }
    }
    */
    
    