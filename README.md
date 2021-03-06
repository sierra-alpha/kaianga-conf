# Kainga-conf
[![Built with Spacemacs](https://cdn.rawgit.com/syl20bnr/spacemacs/442d025779da2f62fc86c2082703697714db6514/assets/spacemacs-badge.svg)](http://spacemacs.org)

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Kainga-conf](#kainga-conf)
    - [Description](#description)
    - [Quick Start](#quick-start)
    - [Configure](#configure)

<!-- markdown-toc end -->


## Description

This package contains all the config and required scripts to get an environment
set up how I like it, it is used in the parent package
[kainga](https://github.com/sierra-alpha/kainga) to supply details to
[matapihi](https://github.com/sierra-alpha/matapihi) and
[wakahiki](https://github.com/sierra-alpha/wakahiki) in order to achieve the
desired setup.

## Quick Start

Use the script found at
[kainga-bootsrap](https://github.com/sierra-alpha/kainga-conf/blob/master/kainga-bootstrap)
to setup the system in it's current configuration, it's intended to be decoupled
from the containerisation process of matapihi, so in theory you could run this
on any debian based linux system (in time i'd like to ad support for CentOS and
other flavours), physical, virtualised or containerised.


This is the configuration file to bootstrap a system the way I like it.
Commands expect to be in a `bash` shell, if your default is `sh` enter bash then,
Copy and paste the following into a shell. the &&'s allow for commands requiring input.

Or the following
```bash
sudo apt-get update && sudo apt-get install -y python3 python3-pip git \
&& git clone https://github.com/sierra-alpha/kainga-conf.git \
&& export PATH="$(python3 -m site --user-base)/bin:$PATH" \
&& pip3 install -U wakahiki \
&& wakahiki -c ~/kainga-conf/kainga.conf -l debug -o ~/.wakahiki.log -u shaun
```

or in an .xinitrc/.Xsession
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

## Configure

This is intended to be a starting point fo you to configure you're own
environment the way you like it, use the kainga.conf as a template to run any
custom setups or scripts of your own. more details can be found on the wkahiki
readme about config file formats.
