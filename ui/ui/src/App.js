import React from "react";


import "./styles.css";
import { BrowserRouter as Router, Route, Switch  } from "react-router-dom";
// import About from "./components/About";
// import PDF from "./components/PDF";
// import Navigation from "./components/Navigation";
// import Footer from "./components/Footer";
// import Home from "./components/Home";
// import Contact from "./components/Contact"; 
import { Navigation, Footer, Home, About, Contact, PDF } from "./components";

function App() {
  return (
    <div className="App">
      <Router>
        <Navigation />
        <Switch>
          <Route path="/" exact component={() => <Home />} />
          <Route path="/pdf" exact component={() => <PDF />} />
          <Route path="/about" exact component={() => <About />} />
          <Route path="/contact" exact component={() => <Contact />} />
        </Switch>
        <Footer />
      </Router>
    </div>
  );
}

export default App;