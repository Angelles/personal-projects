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
                <li><a href="about.html#about">About</a></li>
                <li><a href="contact.html">Contact Us</a></li>
                <li><a href="about.html#service-areas">Service Areas</a></li>
                <li><a href="about.html#services">Services</a></li>
                <li><a href="about.html#testimonials">Testimonials</a></li>
            </ul>
        </nav>`
        ;
    }
  }

   // Define the custom element in terms of the DOM.
  customElements.define("navigation-component", Navigation);