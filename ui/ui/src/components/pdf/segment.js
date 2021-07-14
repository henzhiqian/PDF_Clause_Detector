import React, { Component } from 'react';

import Page from './sample.html';
var htmlDoc = {__html: Page};

export default class Segment extends Component {
  constructor(props){
    super(props);
  }

  render(){
    return (<div dangerouslySetInnerHTML={htmlDoc} />)
}}