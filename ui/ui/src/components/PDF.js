import React from "react";
import SinglePagePDFViewer from "./pdf/single-page";
import AllPagesPDFViewer from "./pdf/all-pages";
// import Segment from "./pdf/segment";

/* This is required only if the project file is located 
inside the app. Otherwise you can use the external link of the pdf file*/
import samplePDF from "./pdf/sample.pdf";


function PDF() {
  return (
    // <div className="box">
    //     <span><SinglePagePDFViewer pdf={samplePDF} /></span>
    //     <span><AllPagesPDFViewer pdf={samplePDF} /></span>


    //     {/* <h4>Single Page</h4>
    //     <SinglePagePDFViewer pdf={samplePDF} />

    //     <hr />

    //     <h4>All Pages</h4>
    //     {/* <div className="rowC">       */}
    //     <AllPagesPDFViewer pdf={samplePDF} />
    //     {/* </div> */}

  
    // </div>

    <div className="flexbox-container">
        <div><SinglePagePDFViewer pdf={samplePDF} /></div>
        <div><AllPagesPDFViewer pdf={samplePDF} /></div>
        {/* <div><Segment/></div> */}
    </div>



  );
}

export default PDF;