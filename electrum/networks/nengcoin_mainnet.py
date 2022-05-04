from electrum.bitcoin import base_decode, base_encode, Hash, is_address
from electrum.exceptions import MissingHeader
from ..bitcoin import hash_encode
from electrum.util import inv_dict, read_json, bfh, to_bytes, BitcoinException
from .abstract_network import AbstractNet
from .auxpow_mixin import AuxPowMixin
from .stake_mixin import StakeMixin

class NengcoinMainnet(AbstractNet, StakeMixin):

    NAME = 'Nengcoin'
    NAME_LOWER = 'nengcoin'
    SHORT_CODE = 'SCA'
    DATA_DIR = 'nengcoin'
    OPEN_ALIAS_PREFIX = 'sca'
    PAYMENT_URI_SCHEME = 'nengcoin'
    PAYMENT_REQUEST_PKI_TYPE = "dnssec+sca"
    APPLICATION_PAYMENT_REQUEST_TYPE = 'application/nengcoin-paymentrequest'
    APPLICATION_PAYMENT_TYPE = 'application/nengcoin-payment'
    APPLICATION_PAYMENT_ACK_TYPE = 'application/nengcoin-paymentack'
    BASE_UNITS = {'SCA': 8, 'mSCA': 5, 'uSCA': 2, 'swartz': 0}
    BASE_UNITS_INVERSE = inv_dict(BASE_UNITS)
    BASE_UNITS_LIST = ['SCA', 'mSCA', 'uSCA', 'swartz']
    TESTNET = False

    WIF_PREFIX = 0x9a
    ADDRTYPE_P2PKH = 63
    ADDRTYPE_P2SH = 23
    XPRV_HEADERS = {
        'standard': 0x0488ade4,
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard': 0x0488b21e,
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BIP44_COIN_TYPE = 921

    GENESIS = "000003bf95cf7875987b333cc8e49a7c1a83583e5f5039b9af9555a92cb29651"

    DEFAULT_PORTS = {'t': '10001', 's': '10002'}
    DEFAULT_SERVERS = read_json('servers/Nengcoin-Mainnet.json', {})
    CHECKPOINTS = read_json('checkpoints/Nengcoin-Mainnet.json', [])

    LN_REALM_BYTE = 0
    LN_DNS_SEEDS = []

    COINBASE_MATURITY = 100
    COIN = 100000000
    TOTAL_COIN_SUPPLY_LIMIT = 999999999999
    SIGNED_MESSAGE_PREFIX = b"\x18Nengcoin Signed Message:\n"

    DECIMAL_POINT_DEFAULT = 8 # SCA
    TARGET_SPACING = int(2 * 60)
    DGW_FORK_BLOCK = 0

    BLOCK_EXPLORERS = {
        'explorer.nengcoin.info': ('https://explorer.nengcoin.info', {'tx': '/tx/', 'addr': '/address/'}),
        'openchains.info': ('https://openchains.info', {'tx': '/coin/nengcoin/tx/', 'addr': '/coin/nengcoin/address/'}),
    }

    @classmethod
    def hash_raw_header(cls, header):
        import algomodule
        return hash_encode(algomodule._quark_hash(bfh(header)))


    @classmethod
    def get_target(cls, height: int, blockchain) -> int:
        index = height // 2016 - 1
        if index == -1:
            return cls.MAX_TARGET

        # Blockchain is PURE POS so we dont have the info needed to
        # calculate the targets required
        return 0
