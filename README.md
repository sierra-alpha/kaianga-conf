This is the configuration file to bootstrap a system the way i like it.
Commands expect to be in a `bash` shell, default is `sh` enter bash then,
Copy and paste the following into a containers shell. the &&'s allow for commands requiring input.

```bash
sudo apt-get update && sudo apt-get install -y python3 python3-pip git \
&& sudo pip3 install pipenv pyscaffold \
&& git clone https://github.com/sierra-alpha/kaianga-conf.git \
&& mkdir wakahiki \
&& cd wakahiki \
&& virtualenv venv \
&& . venv/bin/activate \
&& git clone https://github.com/sierra-alpha/wakahiki.git \
&& cd wakahiki/ \
&& python setup.py develop \
&& python src/wakahiki -c ~/kaianga-conf/kaianga.conf -i -l debug -u shaun
```

Or the following
```bash
sudo apt-get update && sudo apt-get install -y python3 python3-pip git \
&& git clone https://github.com/sierra-alpha/kaianga-conf.git \
&& export PATH="$(python3 -m site --user-base)/bin:$PATH" \
&& pip3 install -U -i wakahiki \
&& wakahiki -c ~/kaianga-conf/kaianga.conf -l debug -o .wakahik.log -u shaun
```

or in an .xinitrc
```bash
xterm -bg grey19 -fg grey70  -fa 'Source Code Pro' -fs 10 -maximize  -bc -e bash -c "sudo apt-get update \
&& sudo apt-get install -y python3 python3-pip git \
&& git clone https://github.com/sierra-alpha/kaianga-conf.git \
|| cd kaianga-conf && git pull \
&& export PATH=\"$(python3 -m site --user-base)/bin:$PATH\" \
&& pip3 install -U -i wakahiki \
&& wakahiki -c ~/kaianga-conf/kaianga.conf -l debug -o .wakahiki.log -u shaun \
&& emacsclient -c -a emacs \
|| echo Failure, enter to exit && read ; bash"
```
