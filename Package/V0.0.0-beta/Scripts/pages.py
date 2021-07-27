import streamlit as st

import Scripts.data as data
import Scripts.regression as algo
import Scripts.settings as setting_info


class MultiPage(object):
    def __init__(self):
        self.pages = []

    def add_page(self, title, func):
        self.pages.append({
            'title': title,
            'function': func
        })

    def run(self):

        page = st.sidebar.radio(
            'App Navigation',
            self.pages,
            format_func = lambda page: page['title'],
            index = 1
        )

        page['function']()


# Formatting methods
def footer():
    st.write("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
footer :after {
	content:'Thank you for using Stock Search.'; 
	visibility: visible;
	display: block;
	position: relative;
	padding: 5px;
	top: 2px;
}
</style>
""", unsafe_allow_html=True)

    st.write('''
<br/>
<hr/>

###### All data has been aqquired from [Quandl](https://www.quandl.com/) and [Yahoo! Finance](https://finance.yahoo.com/). 

<br/>
<br/>

##### Disclaimer
###### The creator of Stock Search is by no means a financial expert of any kind; this is just a visualisation of a project. Use this data and predictions at your own risk. The models may not be accurate and have wide error margins. Furthermore, some data may not be accurate to that minute, as the data interval times vary on the dataset.

###### The creator recommends that:

> ***Stock Search should not be used for any real financial situations. Any use is at the user's own risk.***

###### Thanks to Numpy, Pandas, Quandl, Streamlit and Python.
''', unsafe_allow_html=True)

    # Get your free Quandl API key there too to allow for more frequent download of real time data when using Stock Share. Currently, only a few datasets are


def title_func(title_name):
    title, logo = st.beta_columns([5, 1])

    title.title(title_name)
    logo.image('Images/Logo.png', width=100)


# Pages
def welcome():
    st.image('Images/logo.png', width=520)
    st.write(f'''
# Stock Search

<br/>
''', unsafe_allow_html=True)
    
    # if not st.checkbox('Show Welcome Screen on Startup', value=True):
    #     setting_info.set_welcome_screen(False)

    st.markdown('''Welcome! Stock Search is the latest, innovative way to explore stocks and prices
throughout time, back into the past and into the future. By using detailed
machine learning models and deep neural networks, Stock Search's free AI
tools will outline estimates for rates in the future.

Use the left hand side sidebar to navigate through the pages. There are currently
{len(data.datasets)} datasets you can browse and analyse, with more added every update.

With interactive graphs and data visualization, stock predictions and searching
has never been so easy. Visualize financial data, such as the Apple stocks below:
<br/>
''', unsafe_allow_html=True)
    st.area_chart(data.get_data('Stocks: Apple Inc.')['Adj Close'])
    st.write('''
Then, you can have access to machine learning algorithms that allow you to
receive AI\'s predictions of future prices and trends.

<br/>
<br/>
<hr/>

### Coming Soon
 + Stock Search API for developers
 + Regular updates to the application, user interface and algorithms
 + Any necessary bug fixes, interface changes, etc.

<br/>

##### END OF ARTICLE
''', unsafe_allow_html=True)

    footer()


def all_data():
    title_func('All Data')

    left_col, right_col = st.beta_columns([1, 1])

    data_name = left_col.selectbox('Choose Dataset', [
                                   key for key in data.datasets], help='Choose dataset from a wide variety from Quandl.com and Yahoo! Finance.')

    data_data = data.get_data(data_name)

    data_type = right_col.selectbox('Data Type', list(
        data_data), help='Choose which column of data to display. E.g. "Value", "High" or "Low"')

    st.markdown('<br/><br/>', unsafe_allow_html=True)

    st.area_chart(data_data[data_type])

    algo.get_preds_wrapper(data_data, data_type)

    footer()


def exchange_rates_data():
    title_func('Exchange Rates Data')

    data_name = st.selectbox(
        'Choose Dataset', [key for key in data.exchange_rates])

    data_data = data.get_data('Exchange Rates: ' + data_name)

    data_type = st.selectbox('Data Type', list(
        data_data), help='Choose which column of data to display. E.g. "Value", "High" or "Low"')

    st.area_chart(data_data[data_type])

    footer()


api_key_string = ''


def settings():
    st.write('''
## Stock Search Settings

There are currently no settings yet. Quandl API keys will be introduced in later updates.
''')
    global api_key_string
    api_key_string = 0
    # api_key_string = st.text_input(
    #     'Quandl API Key',
    #     type='password',
    #     help='Choose Quandl API key. Fill this with your API key for more data downloads per timeframe. Without API key, max is 20 downloads per 10 minutes.'
    # )

    footer()