import os
from amaxfactory.core.account import CreateAccount
import amaxfactory.shell.account as account
import amaxfactory.shell.contract as contract
from amaxfactory.bean.bean_init import *

Contract = contract.Contract

new_account = account.new_account
create_master_account = account.create_master_account
new_master_account = account.new_master_account

class TG_REDPACK(CreateAccount):
	def __init__(self,contract_name="tg.redpack"):
		self.name = contract_name
		master = new_master_account()
		tg_redpack = new_account(master,contract_name,factory=True)
		smart = Contract(tg_redpack, 
			wasm_file=os.getenv("FACTORY_DIR") + "/templates/wasm/" + "tg.redpack/tg.redpack.wasm",
			abi_file=os.getenv("FACTORY_DIR") + "/templates/wasm/" + "tg.redpack/tg.redpack.abi")
		smart.deploy()
		self = tg_redpack
		self.set_account_permission(add_code=True)
    
	def setup(self):
		tg_redpack_init(self)
		return self

	def __str__(self):
		return self.name
            

	def addfee(self,fee="0.10000000 AMAX",contract='user1',min_unit=1,submitter_="admin",expect_asset=True):
		self.pushaction("addfee",{"fee":fee,"contract":contract,"min_unit":min_unit,},submitter_,expect_asset=expect_asset) 

	def cancel(self,pack_id=1,submitter_="admin",expect_asset=True):
		self.pushaction("cancel",{"pack_id":pack_id,},submitter_,expect_asset=expect_asset) 

	def claim(self,claimer='user1',pack_id=1,pwhash='x',tg_nickname='x',submitter_="admin",expect_asset=True):
		self.pushaction("claim",{"claimer":claimer,"pack_id":pack_id,"pwhash":pwhash,"tg_nickname":tg_nickname,},submitter_,expect_asset=expect_asset) 

	def delfee(self,coin='8,AMAX',submitter_="admin",expect_asset=True):
		self.pushaction("delfee",{"coin":coin,},submitter_,expect_asset=expect_asset) 

	def setconf(self,admin='user1',hours=1,submitter_="admin",expect_asset=True):
		self.pushaction("setconf",{"admin":admin,"hours":hours,},submitter_,expect_asset=expect_asset) 

	def get_claims(self,scope):
		return self.table("claims",scope).json

	def get_fees(self,scope):
		return self.table("fees",scope).json

	def get_global(self,scope):
		return self.table("global",scope).json

	def get_redpacks(self,scope):
		return self.table("redpacks",scope).json
