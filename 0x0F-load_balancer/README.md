# Load Balancer

## Mandatory

### 0-custom_http_response_header
- Sets up server and adds custom header containing hostname
    - This is setup so load balancer will be able to tell which web server is used
    - NB: Make sure web01 (existing) and web02 (new) are identical 

### 1-install_load_balancer
- Sets up load balancer (new) to roundrobin between web01 and web02
