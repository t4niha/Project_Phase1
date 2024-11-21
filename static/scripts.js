document.addEventListener("DOMContentLoaded", () => {
  // Access the arrow element
  const arrowElement = document.getElementById("arrow");

  // Check if the arrow element exists on the page
  if (arrowElement) {
      // Retrieve the arrow position value passed from the backend
      const arrowPosition = parseFloat(arrowElement.dataset.position);

      console.log("Arrow Position from Backend:", arrowPosition); // Debugging

      // Validate the arrowPosition before applying it
      if (!isNaN(arrowPosition) && arrowPosition >= 0 && arrowPosition <= 100) {
          // Set the left position of the arrow
          arrowElement.style.left = `${arrowPosition}%`;
      } else {
          console.error("Invalid arrow position value:", arrowPosition);
      }
  } else {
      console.error("Arrow element not found on the page.");
  }
});