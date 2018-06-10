# UberEAt_auto
Here is a simple framework to test ubereat.com. 
This framework is following the page object design pattern. As a POC, it has only one test case which use data driver testing concept.

## Pre-requestes:
- Python3
- Chrome (tested with Chromium 65.0.3325.162 Built on Ubuntu , running on Ubuntu 16.04)
- Firefox (tested with Mozilla Firefox 53.0.0)
- GeckoDriver (testd with geckodriver 0.16.0)

## Get it on your machine:
just fire the following bash script:
```bash
git clone https://github.com/islamTaha12/ubereat_auto.git
cd ubereat_auto
pip3 install -r requirements.txt
nosetests-3.4 -vs  --logging-level=WARNING testcases/basics/unregistered/test_home_page.py --tc-file=config.ini
```

## Output: 
You should get something like that,
```bash
╭─xtremx@xtrem-x ~/PycharmProjects/ubereat_auto  
╰─$ nosetests-3.4 -vs  --logging-level=WARNING testcases/basics/unregistered/test_home_page.py --tc-file=config.ini
UEA-002 [with location='Cairo', restaurant='Pizza Milano', assertion=True] ... ok
UEA-002 [with location='Cairo', restaurant='RANDAM', assertion=False] ... ok

----------------------------------------------------------------------
Ran 2 tests in 43.795s

OK

```