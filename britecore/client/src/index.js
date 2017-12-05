import React from 'react'
import ReactDOM from 'react-dom'
import { BrowserRouter as Router } from 'react-router-dom'
require('./global.scss')



import JumboTron from './components/Header'


ReactDOM.render (
    <Router>
      <JumboTron />
    </Router>,
  document.getElementById('container')
)
