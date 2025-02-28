import os
from amaxfactory.core.account import CreateAccount
import amaxfactory.shell.account as account
import amaxfactory.shell.contract as contract
from amaxfactory.bean.bean_init import *

Contract = contract.Contract

new_account = account.new_account
create_master_account = account.create_master_account
new_master_account = account.new_master_account

class AMAX_MSIG(CreateAccount):
	def __init__(self,contract_name="amax.msig"):
		self.name = contract_name
		master = new_master_account()
		amax_msig = new_account(master,contract_name,factory=True)
		smart = Contract(amax_msig, 
			wasm_file=os.getenv("FACTORY_DIR") + "/templates/wasm/" + "amax.msig/amax.msig.wasm",
			abi_file=os.getenv("FACTORY_DIR") + "/templates/wasm/" + "amax.msig/amax.msig.abi")
		smart.deploy()
		self = amax_msig
		self.set_account_permission(add_code=True)
    
	def setup(self):
		amax_msig_init(self)
		return self

	def __str__(self):
		return self.name
            

	def approve(self,proposer='user1',proposal_name='user1',level=[],proposal_hash=[],submitter_="admin",expect_asset=True):
		self.pushaction("approve",{"proposer":proposer,"proposal_name":proposal_name,"level":level,"proposal_hash":proposal_hash,},submitter_,expect_asset=expect_asset) 

	def cancel(self,proposer='user1',proposal_name='user1',canceler='user1',submitter_="admin",expect_asset=True):
		self.pushaction("cancel",{"proposer":proposer,"proposal_name":proposal_name,"canceler":canceler,},submitter_,expect_asset=expect_asset) 

	def exec(self,proposer='user1',proposal_name='user1',executer='user1',submitter_="admin",expect_asset=True):
		self.pushaction("exec",{"proposer":proposer,"proposal_name":proposal_name,"executer":executer,},submitter_,expect_asset=expect_asset) 

	def invalidate(self,account='user1',submitter_="admin",expect_asset=True):
		self.pushaction("invalidate",{"account":account,},submitter_,expect_asset=expect_asset) 

	def propose(self,proposer='user1',proposal_name='user1',requested=[],trx=[],submitter_="admin",expect_asset=True):
		self.pushaction("propose",{"proposer":proposer,"proposal_name":proposal_name,"requested":requested,"trx":trx,},submitter_,expect_asset=expect_asset) 

	def unapprove(self,proposer='user1',proposal_name='user1',level=[],submitter_="admin",expect_asset=True):
		self.pushaction("unapprove",{"proposer":proposer,"proposal_name":proposal_name,"level":level,},submitter_,expect_asset=expect_asset) 

	def get_approvals2(self,scope):
		return self.table("approvals2",scope).json

	def get_invals(self,scope):
		return self.table("invals",scope).json

	def get_proposal(self,scope):
		return self.table("proposal",scope).json
