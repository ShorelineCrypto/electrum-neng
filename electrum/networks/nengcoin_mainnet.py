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
    SHORT_CODE = 'NENG'
    DATA_DIR = 'nengcoin'
    OPEN_ALIAS_PREFIX = 'neng'
    PAYMENT_URI_SCHEME = 'nengcoin'
    PAYMENT_REQUEST_PKI_TYPE = "dnssec+neng"
    APPLICATION_PAYMENT_REQUEST_TYPE = 'application/nengcoin-paymentrequest'
    APPLICATION_PAYMENT_TYPE = 'application/nengcoin-payment'
    APPLICATION_PAYMENT_ACK_TYPE = 'application/nengcoin-paymentack'
    BASE_UNITS = {'NENG': 8, 'mNENG': 5, 'uNENG': 2, 'swartz': 0}
    BASE_UNITS_INVERSE = inv_dict(BASE_UNITS)
    BASE_UNITS_LIST = ['NENG', 'mNENG', 'uNENG', 'swartz']
    TESTNET = False

    WIF_PREFIX = 0xb0
    ADDRTYPE_P2PKH = 53
    ADDRTYPE_P2SH = 5
    XPRV_HEADERS = {
        'standard': 0x0488ade4,
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard': 0x0488b21e,
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BIP44_COIN_TYPE = 681

    GENESIS = "14683bb988bcb69c74276df315c8de108d990fcff07483d5f2a044a3b4a592d8"

    DEFAULT_PORTS = {'t': '10001', 's': '10002'}
    DEFAULT_SERVERS = read_json('servers/Nengcoin-Mainnet.json', {})
    CHECKPOINTS = read_json('checkpoints/Nengcoin-Mainnet.json', [])

    LN_REALM_BYTE = 0
    LN_DNS_SEEDS = []

    COINBASE_MATURITY = 100
    COIN = 100000000
    TOTAL_COIN_SUPPLY_LIMIT = 84000000000
    SIGNED_MESSAGE_PREFIX = b"\x18Nengcoin Signed Message:\n"

    DECIMAL_POINT_DEFAULT = 8 # NENG
    
    TARGET_TIMESPAN = int(1 * 24 * 60 * 60)
    TARGET_SPACING = int(1 * 60)
    INTERVAL = int(TARGET_TIMESPAN / TARGET_SPACING)

    BLOCK_EXPLORERS = {
        'nengexplorer.mooo.com': ('http://nengexplorer.mooo.com:3001', {'tx': '/tx/', 'addr': '/address/'}),
    }


    @classmethod
    def get_target(cls, height: int, blockchain) -> int:
        index = height // 1440 - 1
        if index == -1:
            return cls.MAX_TARGET

        # NENG Blockchain is randomSpike on top of scrypt so that we dont have the info needed to
        # calculate the targets required
        return 0
