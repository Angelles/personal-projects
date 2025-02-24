// Create new class for the navigation bar.
class Navigation extends HTMLElement {
    constructor() {
      super();
    }
  
  connectedCallback(){ // uses a template literal
    this.innerHTML = `
        <nav class="top-nav">
            <ul class="top-nav">
                <span><li class="top-nav"><a href="index.html" class="top-nav">Home</a></li></span>
                <span><li class="top-nav"><a href="about.html#about" class="top-nav">About</a></li></span>
                <span><li class="top-nav"><a href="contact.html" class="top-nav">Contact Us</a></li></span>
                <span><li class="top-nav"><a href="about.html#service-areas" class="top-nav">Service Areas</a></li></span>
                <span><li class="top-nav"><a href="about.html#services" class="top-nav">Services</a></li></span>
                <span><li class="top-nav"><a href="about.html#testimonials" class="top-nav">Testimonials</a></li></span>
            </ul>
        </nav>`
        ;
    }
  }

   // Define the custom element in terms of the DOM.
  customElements.define("navigation-component", Navigation);