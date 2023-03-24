# 导入框架
from amaxfactory.core.logger import Verbosity
from amaxfactory.eosf import *

# 日志打印
# verbosity([Verbosity.INFO,Verbosity.DEBUG,Verbosity.COMMENT,Verbosity.TRACE, Verbosity.OUT,Verbosity.ERROR])
verbosity([Verbosity.INFO, Verbosity.OUT,Verbosity.ERROR])

# 启动节点
reset()

# 创建钱包
create_wallet()

# 获取amax账号
amax = new_master_account()

# 创建账号
user1 = new_account(amax) # 随机账号名
user2 = new_account(user1,"user2") # 指定账号名

# 找回账号
user2_ = new_account("user2",restore=True)

# 批量创建账号
user_list = []
for i in range(10):
    tmp_user = new_account(amax,factory=True)
    user_list.append(tmp_user)

# 合约编译
# contracts_path = "fufi.contracts" # CONTRACT_WORKSPACE不为空
contracts_path = "/Users/charlie/cdt/contracts/fufi.contracts"
init.build(contracts_path) # 编译，根据abi创建合约class文件
# init.build(contracts_path,build=False) # 不编译，根据abi创建合约class文件

# 部署合约
burnpool = init.DEX_BURNPOOL()
# burnpool = init.DEX_BURNPOOL("poll1") #指定合约名
amax_token  = init.AMAX_TOKEN().setup()
amax_mtoken = init.AMAX_MTOKEN().setup()
amax_mtoken2 = init.AMAX_MTOKEN("mtoken2").setup()

admin = new_account("admin",restore=True) 

# 合约的调用
amax_token.create(issuer=admin,maximum_supply="1000000000.00000000 FFT",submitter_=amax_token)
amax_token.issue(to=admin,quantity="800000000.00000000 FFT",memo="",submitter_=admin)


burnpool.setsympair('6,MUSDT', "amax.mtoken", '100000.00000000 FFT', burnpool)
fee = new_account(amax, "fee")

# 转账
admin.transfer(fee,"10000.000000 MUSDT") # AMAX 和 M开头的映射币可以用
amax_token.transfer(admin,user1,"200000.00000000 FFT","",admin) # 其他币调用合约的transfer


oooo = new_account(amax, "oooo")

# 合约print
fee.transfer(burnpool,"1000.000000 MUSDT")
amax_token.transfer(user1,burnpool,"100.00000000 FFT","6,MUSDT",user1)

admin.transfer(user1,"1.00000000 AMAX")
amax_token.transfer(user1,burnpool,"1.00000000 AMAX","6,MUSDT",user1)


