# Prints out the function / signature of Solidity functions

from sha3 import keccak_256

functions = []

# function = "changeMasterCopy(address)"
# function = "execTransaction(address,uint256,bytes,uint8,uint256,uint256,uint256,address,address,bytes)"
# function = 'executeTransaction(uint256)'
# function = 'Execution(uint256)'
# function = 'Execution(bytes32)'
# function = 'Confirmation(address,uint256)'
# function = 'Transfer(address,address,uint256)'
# function = 'WalletCreated(address,address)'
# function = 'Invoked(address,address,uint256,bytes)'
# function = 'createProxy(address,bytes)'
# function = 'createProxyWithNonce(address,bytes,uint256)'
# function = 'WalletCreated(address,address,bool)'
# function = 'CloneCreated(address,address)'
# function = 'InvocationSuccess(bytes32,uint256,uint256)'
# function = 'deployCloneWallet(address,address,uint256)' #0x62f62535
# function = 'deployFullWallet(address,address,uint256)' #0x6f437320
# function = 'deployCloneWallet2(address,address,uint256,bytes32)' #0xf65d2f9b
# function = 'deployFullWallet2(address,address,uint256,bytes32)' #0xc4ac1896
# function = 'WalletDeployed(address,address)'
# function = 'ExecutedTransaction(address,uint256,bytes)' # 0xaf022f6b
# function = 'Transferred(address,address,uint256)'  # 0xd1ba4ac2e2a11b5101f6cb4d978f514a155b421e8ec396d2d9abaf0bb02917ee
# function = 'BulkTransferred(address,address[])'# 0xd4f62f23021706247dcffea245d104ae7ddaec7f23acf3d11d7136d5de6a69ad
# function = 'isUnderLimit(uint256)'
# function = 'changeDailyLimit(uint256)'
# function = 'setup(address[],uint256,address,bytes,address,address,uint256,address)'
# function = 'createProxyWithNonce(address,bytes,uint256)'
# function = '_validateActionAndIncrementNonce(uint8,bytes,uint256,bytes,bytes)'
# function = 'withdrawDai(uint256,address,uint256,bytes,bytes)'
# function = 'executeMultipleAuthKeyMetaTransactions(bytes[],uint256,uint256,address,uint256,bytes)'
# function = 'executeMultipleLoginKeyMetaTransactions(bytes[],uint256,uint256,bytes,address,uint256,bytes,bytes)'
# function = 'changeDailyLimit(uint256)'
# function = 'transfer(address,uint256)'
# function = 'sign_szabo_bytecode(bytes16,uint128)'
# function = 'createProxyAndExecTransaction(address,uint256,address,address,uint256,bytes,uint8)'
# function = 'SubmitProposal(address,uint256,uint256,uint256,address,uint256,address,string,bool[6],uint256,address,address)'
# function = 'ProcessProposal(uint256,uint256,bool)'
# function = 'Ragequit(address,uint256,uint256)'
# function = 'Mint(address,uint256)'
# function = 'EnabledModule(address)'
# function = 'DisabledModule(address)'
# function = 'ExecutionFromModuleSuccess(address)'
# function = 'ExecutionFromModuleFailure(address)'
# function = 'execTransactionFromModule(address,uint256,bytes,uint8)'
# functions.append('Approval(address,address,uint256)')
# function = 'transferFrom(address,address,uint256)'
# function = 'Upgraded(address)'
# function = 'redeem(uint256)'
# function = 'createSalary(address,uint256,address,uint256,uint256)'
# function = 'issueSynths(uint256)'
# function = 'burnSynths(uint256)'
# function = 'claimFees()'
# function = 'borrow(address,uint256,uint256,uint16)'
# function = 'repay(address,uint256,address)'
# function = 'redeem(uint256)'
# function = 'redeemIdleToken(uint256,bool,uint256[])'
# functions.append('batchEthInSwapExactIn((address,uint256,uint256,uint256)[],address,uint256)')
# functions.append('batchEthOutSwapExactIn((address,uint256,uint256,uint256)[],address,uint256,uint256)')
# functions.append('batchSwapExactIn((address,uint256,uint256,uint256)[],address,address,uint256,uint256)')
# functions.append('batchSwapExactOut((address,uint256,uint256,uint256)[],address,address,uint256)')
# functions.append('batchEthInSwapExactOut((address,uint256,uint256,uint256)[],address)')
# functions.append('batchEthOutSwapExactOut((address,uint256,uint256,uint256)[],address,uint256)')
# functions.append('redeemUnderlying(address,address,uint256,uint256)')
# functions.append('LogAddAuth(address,address)')
# functions.append('LogRemoveAuth(address,address)')
# functions.append('approve(address,uint256)')
# functions.append('TransferSingle(address,address,address,uint256,uint256)')
# functions.append('TransferBatch(address,address,address,uint256[],uint256[])')
# functions.append('SetDelegate(address,bytes32,address)')
# functions.append('ClearDelegate(address,bytes32,address)')

# functions.append('AddDelegate(address,address)')
# functions.append('RemoveDelegate(address,address)')
# functions.append('ExecuteAllowanceTransfer(address,address,address,address,uint96,uint16)')
# functions.append('PayAllowanceTransfer(address,address,address,address,uint96)')
# functions.append('SetAllowance(address,address,address,uint96,uint16)')
# functions.append('ResetAllowance(address,address,address)')
# functions.append('DeleteAllowance(address,address,address)')

functions.append('RelayerInstalled(address)')
functions.append('RelayerUninstalled(address)')
functions.append('RelayExecuted(bytes32,bool,address,uint256,uint256)')
functions.append('OutOfCoins()')
functions.append('Deposit(address,uint256,uint256)')
functions.append('Withdraw(address,address,uint256)')


encoded_functions = []
for func in functions:
    encoded_functions.append(func.encode('utf-8'))

for efunc in encoded_functions:
    sha3_hash = keccak_256(efunc).hexdigest()
    method_id = "0x"+sha3_hash
    print(efunc)
    print(method_id)
    print(method_id[:10])
    print('')