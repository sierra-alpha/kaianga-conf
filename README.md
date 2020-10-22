This is the configuration file to bootstrap a system the way I like it.
Commands expect to be in a `bash` shell, default is `sh` enter bash then,
Copy and paste the following into a containers shell. the &&'s allow for commands requiring input.

```bash
sudo apt-get update && sudo apt-get install -y python3 python3-pip git \
&& sudo pip3 install pipenv pyscaffold \
&& git clone https://github.com/sierra-alpha/kainga-conf.git \
&& mkdir wakahiki \
&& cd wakahiki \
&& virtualenv venv \
&& . venv/bin/activate \
&& git clone https://github.com/sierra-alpha/wakahiki.git \
&& cd wakahiki/ \
&& python setup.py develop \
&& python src/wakahiki -c ~/kainga-conf/kainga.conf -l debug -o ~/.wakahiki.log -u shaun
```

Or the following
```bash
sudo apt-get update && sudo apt-get install -y python3 python3-pip git \
&& git clone https://github.com/sierra-alpha/kainga-conf.git \
&& export PATH="$(python3 -m site --user-base)/bin:$PATH" \
&& pip3 install -U wakahiki \
&& wakahiki -c ~/kainga-conf/kainga.conf -l debug -o ~/.wakahiki.log -u shaun
```

or in an .xinitrc
```bash
xterm -bg grey19 -fg grey70  -fa 'Source Code Pro' -fs 10 -maximize  -bc -e bash -c "sudo apt-get update \
&& sudo apt-get install -y python3 python3-pip git \
&& git clone https://github.com/sierra-alpha/kainga-conf.git \
|| cd kainga-conf && git pull \
&& export PATH=\"$(python3 -m site --user-base)/bin:$PATH\" \
&& pip3 install -U wakahiki \
&& wakahiki -c ~/kainga-conf/kainga.conf -l debug -o ~/.wakahiki.log -u shaun \
&& emacsclient -c -a emacs \
|| echo Failure, enter to exit && read ; bash"
```
