# Digital_wallet
Description
You are supposed to make a digital wallet system that allows people to transfer money among their 
wallets. The wallet system uses its own currency called FkRupee (F). No account can contain 
balance less than 0.
Requirements:
1. The smallest amount that the users can transfer is F* 0.0001. The description of the wallet 
operations follows.
2. The command CreateWallet <accountHolder1> <amount> creates a new wallet with a 
balance of F* <amount> in the name of <accountHolder1>.
3. The command TransferMoney <accountHolder1> <accountHolder2> <amount> would 
decrease F* <amount> from accountHolderi's account and add the same amount in account 
Holder2's account.
4. The command Statement <accountHolder1> should display the account statement for 
account Holderi's account. The account statement should contain all the transactions made in
that account.
5. The command Overview should display the current balance of all the accounts. Your wallet 
system also provides some offers to the customers.
6. Offer 1: When customer A transfers money to customer B and both the account holders have
the same balance after the transaction then both the customers get F* 10 as a reward.
7. Offer 2: Whenever the command Offer2 is fired 3 customers with the highest number of 
transactions will get F10, F* 5, and F* 2 as rewards. If there is a tie (customers having the 
same number of transactions) then the customer having higher account balance 
should be given preference. If there is still a tie then the customer whose account was
created first should be given preference.
