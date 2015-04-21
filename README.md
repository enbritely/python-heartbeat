# python-heartbeat

Example

    virtualenv -p python virtualenv
    source virtualenv/bin/activate
    
    pip install git+https://github.com/enbritely/python-heartbeat
    
    echo 'git_sha="'"$(git rev-parse HEAD)"'"' > example/git_sha.py
    
    python example/example.py 
    
    curl localhost:8888/heartbeat
    
