###############################################################################################################
# Developing a chatbot that will generate a weighted investment portfolio based on the user's risk tolerance  # 
# and age, utilizing Streamlit, Python, Machine Learning, & Traditional Financial Metrics.                    #
###############################################################################################################

# import libraries 
import streamlit as st
from streamlit_chat import message
import pandas as pd

from chatbot_functions import verifyUserAge
from chatbot_functions import determine_weights
from chatbot_functions import allocate_portfolio
from chatbot_functions import display_portfolio_allocation
from chatbot_functions import display_forecasts
from chatbot_functions import run_MC_simulation

st.markdown("## Investment Portfolio Generator")

# chatbot function
def chatbot():
    # Use the message function to create a chat-like UI
    message("Hello, I'm a chatbot that can generate a weighted investment portfolio for you!", seed=21, key=10)
    message("Please enter your age", seed=21, key=11)

    # Ask the user for their age
    user_age = st.text_input(' ', placeholder='Enter your age')
    message(user_age, is_user=True, seed=1, key=12)

    user_age = user_age.strip() 

    # Check if the user has entered a response
    if user_age:
    
        if user_age.isdigit() == False: 
            message("I'm sorry, but it looks like you entered an invalid number. Please enter a valid whole number!", seed=21, key=13)
    
        else:
            # Convert the user's age to an integer
            age = float(user_age)
            
            # verify the user's age 
            verifyUserAge(age)

            if age >= 18 and age <= 110: 

                # Ask the user for their desired investment amount 
                message("Please enter your desired investment amount in RS", seed=21, key=14)
                user_investment_amount = st.text_input(' ', placeholder='Enter investment amount in RS')
                message(user_investment_amount, is_user=True, seed=1, key=15)

                user_investment_amount = user_investment_amount.strip() 

                # Ask the user for their desired portfolio type (risk tolerance)
                if user_investment_amount: 
                    if user_investment_amount.isnumeric():
                        message("Please enter a portfolio type that matches your risk tolerance (High Risk Portfolio, Low Risk Portfolio, Moderate Risk Portfolio)", seed=21, key=16)
                        portfolio_type = st.text_input(' ', placeholder='Enter portfolio type')

                        valid_portfolio_types = ['high risk portfolio', 'low risk portfolio', 'moderate risk portfolio']

                        if portfolio_type: 
                            if str(portfolio_type).lower().strip() in valid_portfolio_types: 
                                if str(portfolio_type).lower().strip() == 'high risk portfolio': 

                                    # generate a High Risk Portfolio based on expected return vs risk (MPT)
                                    # stocks --> 'TSLA', 'NVDA', 'LLY', 'AAPL', 'UNH', 'MA'
                                    # bonds --> Treasury Yield 10yr 
                                    # crypto --> ETH

                                    df = pd.DataFrame(
                                        {'Stocks': ['TSLA', 'NVDA', 'LLY', 'AAPL', 'UNH', 'MA'],
                                         'Bonds': ['10yr Treasury Yield', '-', '-', '-', '-', '-'], 
                                         'Crypto': ['ETH', '-', '-', '-', '-', '-']
                                        })
                                    message('Your High-Risk Portfolio contains the following assets: ', seed=21, key=17)
                                    st.table(df) 

                                    #message(f'{portfolio_table}', seed=21, key=7)

                                    # calculate weights for portfolio
                                    determine_weights(age)
                                    allocate_portfolio(user_investment_amount)
                                    
                                    # display portfolio allocation pie chart 
                                    display_portfolio_allocation(portfolio_type)

                                    # Ask the user for their desired investment amount 
                                    message("Would you like me to display forecasts of each asset in your portfolio?", seed=21, key=30)
                                    user_input = st.text_input(' ', placeholder='Display forecasts? (enter yes/no)')
                                    message(user_input, is_user=True, seed=1, key=31)
                 
                                    # display prophet model forecasts
                                    display_forecasts(user_input, portfolio_type)

                                    # run MC simulation
                                    if user_input.lower().strip() == 'no' or user_input.lower().strip() == 'n': 
                                        st.warning('Monte Carlo Simulation, also known as the Monte Carlo Method or a multiple probability simulation, is a mathematical technique, which is used to estimate the possible outcomes of an uncertain event, in this case projecting cumulative returns for a selected portfolio!', icon="💡") 
                                        user_input_MC = st.text_input(' ', placeholder='Run Monte Carlo Simulation? (enter yes/no)')
                                        message(user_input_MC, is_user=True, seed=1, key=46)
                                        run_MC_simulation(user_input_MC, portfolio_type)


                                if str(portfolio_type).lower().strip() == 'low risk portfolio': 

                                    # generate a Low Risk Portfolio based on expected return vs risk 
                                    # stocks --> 'PEP', 'PG', 'JNJ', 'KO', 'JPM', 'BAC', 'BRK-B'
                                    # bonds --> Treasury Yield 30yr 
                                    # crypto --> BTC

                                    df = pd.DataFrame(
                                        {'Stocks': ['PEP', 'PG', 'JNJ', 'KO', 'JPM', 'BAC', 'BRK-B'], 
                                         'Bonds': ['30yr Treasury Yield', '-', '-', '-', '-', '-', '-'], 
                                         'Crypto': ['BTC', '-', '-', '-', '-', '-', '-']
                                        })
                                    message('Your Low-Risk Portfolio contains the following assets: ', seed=21, key=18)
                                    st.table(df) 
                                
                                    #message(f'{portfolio_list}', seed=21, key=13)
                                

                                    # calculate weights for portfolio
                                    determine_weights(age)                               
                                    allocate_portfolio(user_investment_amount)
    
                                    # display portfolio allocation pie chart 
                                    display_portfolio_allocation(portfolio_type)

                                    # Ask the user for their desired investment amount 
                                    message("Would you like me to display forecasts of each asset in your portfolio?", seed=21, key=35)
                                    user_input = st.text_input(' ', placeholder='Display forecasts? (enter yes/no)')
                                    message(user_input, is_user=True, seed=1, key=36)

                                    # display prophet model forecasts
                                    display_forecasts(user_input, portfolio_type)

                                    # run MC simulation
                                    if user_input.lower().strip() == 'no' or user_input.lower().strip() == 'n': 
                                        st.warning('Monte Carlo Simulation, also known as the Monte Carlo Method or a multiple probability simulation, is a mathematical technique, which is used to estimate the possible outcomes of an uncertain event, in this case projecting cumulative returns for a selected portfolio!', icon="💡") 
                                        user_input_MC = st.text_input(' ', placeholder='Run Monte Carlo Simulation? (enter yes/no)')
                                        message(user_input_MC, is_user=True, seed=1, key=48)
                                        run_MC_simulation(user_input_MC, portfolio_type)

                                if str(portfolio_type).lower().strip() == 'moderate risk portfolio': 

                                    # generate a Moderate Risk Portfolio portfolio based on expected return vs risk 
                                    # stocks --> 'MRK', 'V', 'HD', 'PFE', 'ABBV', 'AMZN'
                                    # bonds --> Treasury Yield 30yr 
                                    # crypto --> BTC

                                    df = pd.DataFrame(
                                        {'Stocks': ['MRK', 'V', 'HD', 'PFE', 'ABBV','AMZN'], 
                                         'Bonds': ['30yr Treasury Yield', '-', '-', '-', '-', '-'],
                                         'Crypto': ['BTC', '-', '-', '-', '-', '-']
                                        })
                                    message('Your Moderate-Risk Portfolio contains the following assets: ', seed=21, key=19)
                                    st.table(df) 

                                    #message(f'{portfolio_list}', seed=21, key=15)

                                    # calculate weights for portfolio
                                    determine_weights(age)
                                    allocate_portfolio(user_investment_amount)

                                    # display portfolio allocation pie chart 
                                    display_portfolio_allocation(portfolio_type)

                                    # Ask the user for their desired investment amount 
                                    message("Would you like me to display forecasts of each asset in your portfolio?", seed=21, key=37)
                                    user_input = st.text_input(' ', placeholder='Display forecasts? (enter yes/no)')
                                    message(user_input, is_user=True, seed=1, key=38)

                                    # display prophet model forecasts
                                    display_forecasts(user_input, portfolio_type)

                                    # run MC simulation
                                    if user_input.lower().strip() == 'no' or user_input.lower().strip() == 'n': 
                                        st.warning('Monte Carlo Simulation, also known as the Monte Carlo Method or a multiple probability simulation, is a mathematical technique, which is used to estimate the possible outcomes of an uncertain event, in this case projecting cumulative returns for a selected portfolio!', icon="💡") 
                                        user_input_MC = st.text_input(' ', placeholder='Run Monte Carlo Simulation? (enter yes/no)')
                                        message(user_input_MC, is_user=True, seed=1, key=50)
                                        run_MC_simulation(user_input_MC, portfolio_type)

                            else: 
                                message("I'm sorry, but it looks like you entered an invalid portfolio type. Please enter a valid portfolio type!", seed=21, key=20)
                    else:
                        message("I'm sorry, but it looks like you entered an invalid number. Please enter a valid whole number!", seed=21)
    else:
        # The user hasn't entered a response yet, so don't show any messages in the chat widget
        pass

# call chatbot function 
chatbot() 