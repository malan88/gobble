# gobble

***Please note! I am not a security expert! Use this script at your own risk!***

Generate a gobbledy-gook-secure password for security questions and passwords.

The script will by default choose one word from the [EFF's large diceware
list][0] and append random characters (using Python's `secrets` library) to pad
up to 25 characters. The single word should serve to mitigate the gobbledy-gook
social engineering hack: I can't imagine a phone support person accepting the
answer "it's just a bunch of gobbledy-gook" when there is clearly at least one
recognizable English word at the beginning of the password. If they do, then
there are more serious security issues at the organization than can be solved by
a secure password. Since a single word can't be brute-forced in a phone
conversation from the EFF word list, and a 25 character password isn't going to
be brute-forced by a computer (granted, it is technically 25-characters less one
word (the max being 9 characters, resulting in a minimum gobbledy-gook password
of 16 characters) so it seems to me to be pretty secure.

I use these only for security questions and passwords at sites and services
where I don't trust the company to be quite so technologically saavy. This
includes, sadly, my bank.

The script will also generate a  normal diceware password of arbitrary
word-length. If a max length of the password is set and the number of words is
specified, the password may end up compromised or truncated. This is because I
will not spend the time to write logic that will choose shorter words based on
the max-password length. That would be non-trivial and compromise the
entropy-level.

For more information on operations and flags, see the `-h` or `--help` flag.

## Background

Lately I've been getting really into security, especially regarding passwords,
encryption, and 2FA/U2f with YubiKeys. It seems to help me get and stay
organized. Helpfully, I stumbled on [this comment thread][1] on a Hacker News
article titled ["Everything you ever wanted to know about building a secure
password reset (2012)"][2]:
	
> ***TimTheTinker*** 25 days ago [-]
> 
> I just generate more passwords for the security questions. Since I’m using a
> reliable, backed-up password manager, my primary concern is protecting my
> account from would-be hijackers, not resetting a potentially lost password.
> 
> ***twothamendment*** 25 days ago [-]
> 
> Yes, because there is no way I'm answering what city I was married in. It
> is public record. A password-like "nonsense" answer is the only way to go.
> 
> ***WorldMaker*** 24 days ago [-]
> 
> The one thing I try to do is make sure whatever password generator I
> use for these produces pronounceable passwords in English that are
> relatively easy to spell, because so many of the places that want
> these really mean "Phone password".
> 
> ***TimTheTinker*** 24 days ago [-]
> 
> 1Password integrates with the iPhone's built-in password manager,
> so I'm never stuck typing in passwords anymore.
> 
> ***WorldMaker*** 24 days ago [-]
> 
> The issue isn't typing them. The issue is that many "Security
> Questions" are secretly "Phone Passwords" because customer
> service representatives can see them in plaintext and will ask
> you them if you ever have reason to call them over the phone.
> Making sure that they are pronounceable (mostly) English words
> avoids some of the potential awkwardness of reading them out
> of your password manager over the phone, even if they are
> intentional random gibberish. It also partly avoids the social
> engineering trap of "it's just random garbage" because at
> least if it looks like words a customer service rep may still
> ask for them anyway rather than not bother to one-at-a-time
> review a series of random characters.
> 
> ***TimTheTinker*** 23 days ago [-]
> 
> Ok, gotcha. 1Password can also generate passphrases from
> dictionary words.
> 
> Agreed, the “it’s a bunch of gobbledygook” social
> engineering hack is a really serious vulnerability. 


[0]: https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
[1]: https://news.ycombinator.com/item?id=19051562
[2]: https://news.ycombinator.com/item?id=19046952
