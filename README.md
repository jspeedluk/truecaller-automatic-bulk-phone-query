# truecaller-automatic-bulk-phone-query
A Python and selenium tool to automatically fetching bulk phone numbers on web

## Does it work ?
It does but not really. It works end-to-end but since truecaller has limit on number of searches per day (current limit is 5 per day), this tool stops generatig results.
So you will require multiple accounts to do this. Earlier truecaller used to have limit of 150-160 per 10-15 mins, where if you had 4-5 multiple accounts then you could have fetched details continously. However with truecaller making change in its policies, this tools is no longer a very useful tool for bulk searching usecase. However, you can still go through the various features this tool supports like automatic sign-in using selenium and autmatically fetching details using XPATH for finding relevent html tags.

## If you are still reading this, then it means you are more interested in the working of this tool and some tips'n' tricks. Let me tell you a few
### Working of tool
The way it works is that it will open truecaller website, sign-in and then start fetching details. For each of these activvities, it finds the relevent elements from the page and either clicks them or put an input into them. 

### How to find an element
There are multiple ways. As this tool is using Selenium4, which is latest at this time, it can find elements on the page by ID, Class, Text, or XPATH. The most powerful among these is XPATH. It is basically a regex for HTML tags. So you can provide a lot of conditions and it will find an element that satisfies them. The best way to use it is:
- Open a webpage on chrome and open inspect
- Do a Ctlr+F on the inspect window where it shows the code
- The find feature supports XPATH. Read the syntax of XPATH online, and then try each of them to see if it is working fie or not. Example XPATH are shown in the code for reference.

If you are interested in making PR to this code, feel free to raise one and message me.
