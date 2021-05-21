mkdir -p ~/.streamlit/
echo "\
[gereral]\n\
email=\"your-email@domain.com\"n\
" > ~/.streamlit/creadentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml