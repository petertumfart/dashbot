import streamlit as st
from utils import extract_combination
import logon_data




st.title('Dashbot')

form_container = st.empty()
with form_container.form(key='my_form'):
    mail = st.text_input(label='Enter your email:')
    pwd = st.text_input(label='Enter you password:', type="password")
    submit_button = st.form_submit_button(label='Submit')


if submit_button:
    # Extract mail - password combination and decide:
    valid = extract_combination(mail, pwd)
    if valid:
        form_container.empty()
        st.success('Successful authentication')
        if mail == logon_data.mail_data[0]:
            st.write('Seas Peda!')

        elif mail == logon_data.mail_data[1]:
            st.write('Seas Flo!')
            st.image('img/flo.jpeg')
            st.balloons()
        elif mail == logon_data.mail_data[2]:
            st.write('Seas Bisi!')
            st.image('img/bisi.jpg')
            st.balloons()
        elif mail == logon_data.mail_data[2]:
            st.write('Seas Hannes!')
            st.image('img/hannes.jpeg')
            st.balloons()
    else:
        st.error('Ups, didn\'t recognize you..')

st.write('Stay tuned...')
st.write('Shoutouts to: [Flothohub](https://github.com/FloThoHub) and [geilertyp.at](http://geilertyp.at)')