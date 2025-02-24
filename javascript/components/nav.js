// Create new class for the navigation bar.
class Navigation extends HTMLElement {
    constructor() {
      super();
    }
  
  connectedCallback(){ // uses a template literal
    this.innerHTML = `
        <nav class="nav-menu">
            <ul>
                <li><a href="index.html">Home</a></li>
                <li>About</li>
                <li><a href="contact.html">Contact Us</a></li>
                <li>Locations Served</li>
                <li>Services</li>
                <li>Testimonials</li>
            </ul>
        </nav>`
        ;
    }
  }

   // Define the custom element in terms of the DOM.
  customElements.define("navigation-component", Navigation);