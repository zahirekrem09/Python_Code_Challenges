f=lambda x:-1 if int(x)%2==1 else 1
def kontrol(x):
    return all([ f(x[i])+f(x[i+1]) == 0 for i in range(len(x)-1)])
def longest_substring(data):
	res =[data[i:j] for i in range(len(data)-1) for j in range(i+1,len(data)+1)]
	res=max(list(filter(kontrol,res)),key=len)
	return res



"""Longest Alternating Substring

Given a string of digits, return the longest substring with alternating odd/even or even/odd digits. 
If two or more substrings have the same length, return the substring that occurs first.
Examples

longest_substring("225424272163254474441338664823") ➞ "272163254"
# substrings = 254, 272163254, 474, 41, 38, 23

longest_substring("594127169973391692147228678476") ➞ "16921472"
# substrings = 94127, 169, 16921472, 678, 476

longest_substring("721449827599186159274227324466") ➞ "7214"
# substrings = 7214, 498, 27, 18, 61, 9274, 27, 32
# 7214 and 9274 have same length, but 7214 occurs first."""