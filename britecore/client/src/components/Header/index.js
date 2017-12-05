import React, { Component } from 'react'
import {Jumbotron, Button} from 'react-bootstrap'
import { Link } from 'react-router-dom'




export default class JumboTron extends Component {
  constructor(props) {
    super(props)
  }

  render() {

    return(
      <Jumbotron>
        <h1>Welcome to BriteCore!</h1>
        <p>This is a simple insurance form that will allow you to store information regarding your current policy. To learn more about the company, click the button below.</p>
        <p><Button bsStyle="primary"><Link to="https://www.britecore.com/"></Link>Learn more</Button></p>
      </Jumbotron>
    )
  }
}
