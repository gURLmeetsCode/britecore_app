import React from 'react'
import { shallow } from 'enzyme'
import JumboTron from '../src/components/Header/index'

describe('<JumboTron />', () =>{
  it('renders 1 <JumboTron /> component', () => {
    const component = shallow(<JumboTron />)
    expect(component).toHaveLength(1);
  });
});
