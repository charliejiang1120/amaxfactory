from amaxfactory.beans.base.amcli import runaction
from amaxfactory.beans.base.baseClass import baseClass

class hotpottoken(baseClass):
	# contract = 'htoken'
	contract = 'hotpotatoken'
	def burnfee(self,account='user1',quantity="0.10000000 AMAX",memo='x',suber='user1'):
		self.response = runaction(self.contract + f""" burnfee '["{account}","{quantity}","{memo}"]' -p {suber}""") 
		return self

	def close(self,owner='user1',symbol='8,AMAX',suber='user1'):
		self.response = runaction(self.contract + f""" close '["{owner}","{symbol}"]' -p {suber}""") 
		return self

	def create(self,issuer='user1',maximum_supply="0.10000000 AMAX",fee_ratio=1,gas_ratio=1,suber='user1'):
		self.response = runaction(self.contract + f""" create '["{issuer}","{maximum_supply}",{fee_ratio},{gas_ratio}]' -p {suber}""") 
		return self

	def feeexempt(self,symbol='8,AMAX',account='user1',is_fee_exempt='true',suber='user1'):
		self.response = runaction(self.contract + f""" feeexempt '["{symbol}","{account}",{is_fee_exempt}]' -p {suber}""") 
		return self

	def feereceiver(self,symbol='8,AMAX',fee_receiver='user1',suber='user1'):
		self.response = runaction(self.contract + f""" feereceiver '["{symbol}","{fee_receiver}"]' -p {suber}""") 
		return self

	def freezeacct(self,symbol='8,AMAX',account='user1',is_frozen='true',suber='user1'):
		self.response = runaction(self.contract + f""" freezeacct '["{symbol}","{account}","{is_frozen}"]' -p {suber}""") 
		return self

	def issue(self,to='user1',quantity="0.10000000 AMAX",memo='x',suber='user1'):
		self.response = runaction(self.contract + f""" issue '["{to}","{quantity}","{memo}"]' -p {suber}""") 
		return self

	def minfee(self,symbol='8,AMAX',min_fee_quantity="0.10000000 AMAX",suber='user1'):
		self.response = runaction(self.contract + f""" minfee '["{symbol}","{min_fee_quantity}"]' -p {suber}""") 
		return self

	def notifypayfee(self,fromx='user1',to='user1',fee="0.10000000 AMAX",memo='x',suber='user1'):
		self.response = runaction(self.contract + f""" notifypayfee '["{fromx}","{to}","{fee}","{memo}"]' -p {suber}""") 
		return self

	def open(self,owner='user1',symbol='8,AMAX',ram_payer='user1',suber='user1'):
		self.response = runaction(self.contract + f""" open '["{owner}","{symbol}","{ram_payer}"]' -p {suber}""") 
		return self

	def pause(self,symbol='8,AMAX',is_paused='true',suber='user1'):
		self.response = runaction(self.contract + f""" pause '["{symbol}","{is_paused}"]' -p {suber}""") 
		return self

	def ratio(self,symbol='8,AMAX',fee_ratio=1,gas_ratio=1,suber='user1'):
		self.response = runaction(self.contract + f""" ratio '["{symbol}",{fee_ratio},{gas_ratio}]' -p {suber}""") 
		return self

	def retire(self,quantity="0.10000000 AMAX",memo='x',suber='user1'):
		self.response = runaction(self.contract + f""" retire '["{quantity}","{memo}"]' -p {suber}""") 
		return self

	def transfer(self,fromx='user1',to='user1',quantity="0.10000000 AMAX",memo='x',suber='user1'):
		self.response = runaction(self.contract + f""" transfer '["{fromx}","{to}","{quantity}","{memo}"]' -p {suber}""") 
		return self

