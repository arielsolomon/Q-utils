create package:
-
python3 setup.py bdist_wheel

run rabbitmq container:
-
sudo docker run --rm -d -p 5672:5672 --hostname my-rabbit --name some-rabbit rabbitmq:latest

github repository of this package:
-
url - https://github.com/arielsolomon/Q-utils

