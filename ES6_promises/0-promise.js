class APIHandler {
    getResponseFromAPI() {
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          const randomInt = Math.floor(Math.random() * 100);
          if (randomInt < 50) {
            resolve({ status: "success", data: { message: "API call successful" } });
          } else {
            reject(new Error("API call failed"));
          }
        }, 2000); // Simulate API delay
      });
    }
  }
  
  // Usage example
  const apiHandler = new APIHandler();
  
  apiHandler.getResponseFromAPI()
    .then(response => {
      console.log("API Response:", response);
    })
    .catch(error => {
      console.error("Error:", error.message);
    });
  
  console.log