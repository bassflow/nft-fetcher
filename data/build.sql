CREATE TABLE IF NOT EXISTS tokennfttx (
    blocknumber int,
    timestampint int,
    hashnr str,
    nonce int,
    blockhash str,
    fromaddress str,
    contractaddress str,
    toaddress str,
    tokenid int,
    tokenname str,
    tokensymbol str,
    tokendecimal int,
    transactionindex int,
    gas int,
    gasprice int,
    gasused int,
    cumulativegasused int,
    input str,
    confirmations,
    PRIMARY KEY (contractaddress, tokenid, toaddress, timestampint)
);

CREATE TABLE IF NOT EXISTS tokentx (
    blocknumber int,
    timestampint int,
    hashnr str,
    nonce int,
    blockhash str,
    fromaddress str,
    contractaddress str,
    toaddress str,
    value int,
    tokenname str,
    tokensymbol str,
    tokendecimal int,
    transactionindex int,
    gas int,
    gasprice int,
    gasused int,
    cumulativegasused int,
    input str,
    confirmations,
    PRIMARY KEY (contractaddress, toaddress, timestampint)
);

CREATE TABLE IF NOT EXISTS nftholdings (
    contractaddress str,
    tokenid int,
    tokenuri int
);