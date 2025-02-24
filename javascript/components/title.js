// Create new class for the title.
class Title extends HTMLElement {
    constructor() {
      super();
    }
  
  connectedCallback(){ // uses a template literal
    this.innerHTML = `
        <title>Leger Construction</title
        `
        ;
    }
  }

   // Define the custom element in terms of the DOM.
  customElements.define("title-component", Title);