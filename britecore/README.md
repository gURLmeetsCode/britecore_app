# BriteCore Coding Challenge

BriteCore Product Development Coding Challenge

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Please make sure you have these sources installed on your local machine

django1.11.7
python 2.7
pipenv
node

```
pip install --upgrade pip setuptools pipenv

To access the virtualenv:
pipenv --two
pipenv shell

pipenv install Django to install the latest version or
pipenv install Django==1.11.7

if you do not have pip installed:
sudo easy_install pip

brew update
brew install python 3 to install latest version or
brew install python 2.7
please make sure your .bash_file is properly configured for version 2.7.

To edit and save .bash_file:
touch ~/.bash_profile; open ~/.bash_profile

Add configuration for 2.7:

# Setting PATH for Python 2.7
export PATH=/usr/local/bin:/usr/local/sbin:$PATH
export PATH=/Users/enteryourusername/.local/bin:$PATH
export PATH=/Users/enteryourusername/Library/Python/2.7/bin:$PATH


check node version from terminal:
node --version

To download or update node:
https://nodejs.org/en/

```

### Installing

Get a clone of the repo

From terminal type:

`git clone  https://github.com/IntuitiveWebSolutions/ProductDevelopmentProject.git`

cd into the project folder

From the terminal type:
```
pipenv install -r requirements.txt
npm install
```

This will download the manifest for the python server and frontend client.


From the terminal type:

```
npm start
python manage.py runserver
```

You should now have a running server on http://127.0.0.1:8000/


## Running the tests

To run the Django test:

`python manage.py test`


To run React unit testing:

`npm run test`


### Break down into end to end tests


These test validate the model and the view. The test will illustrate a field creation, and vlaidate the post method.


```
def test_api_can_post_a_risk_field(self):
      """Test the api can post a given field to risk model."""
      client = APIClient()
      response = self.client.post('/', {'title': 'new idea'}, format="json")
      self.assertEqual(response.status_code, status.HTTP_200_OK)
```


This is a simple test to validate component rendering.

```
describe('<JumboTron />', () =>{
  it('renders 1 <JumboTron /> component', () => {
    const component = shallow(<JumboTron />)
    expect(component).toHaveLength(1);
  });
});

```


## Deployment

To run the AWS Lambda server, type the following:

"zappa deploy"

** Deployment will not work due to improper AWS IAM manage config. **


## Built With

* [React-Router](https://www.npmjs.com/package/react-router-dom)
* [React](https://reactjs.org)
* [React-Bootstrap](https://react-bootstrap.github.io)
* [Webpack](https://webpack.js.org)
* [Webpack-Dev-Server](https://webpack.github.io/docs/webpack-dev-server.html)
* [Django-webpack-loader](https://github.com/ezhome/django-webpack-loader)
* [PostCSS](http://postcss.org/)
* [Babel](https://babeljs.io)
* [Autoprefixer](https://github.com/postcss/autoprefixer)
* [Jest](https://facebook.github.io/jest/)
* [Enzyme](https://github.com/airbnb/enzyme)


## Author

* **Natasha Kelly** -- [gURLmeetsCode](https://github.com/gURLmeetsCode)

## Acknowledgments

* Thank you to BriteCore for allowing me the chance to showcase my skills.
