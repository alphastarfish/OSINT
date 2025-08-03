#!/usr/bin/env python3
"""
🔗 NODELINK SECURE COMMUNICATIONS
TYLER Force Multiplier Framework - Encrypted Operator Network

Classification: SECURE COMMUNICATIONS
Version: 1.0
Node: SIGMA COMMAND
"""

import asyncio
import json
import time
import hashlib
import hmac
import secrets
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, asdict
from enum import Enum
import sqlite3
import threading
import logging
from concurrent.futures import ThreadPoolExecutor

try:
    import cryptography
    from cryptography.fernet import Fernet
    from cryptography.hazmat.primitives import hashes, serialization
    from cryptography.hazmat.primitives.asymmetric import rsa, padding
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    import websockets
    import ssl
    import base64
    import aiohttp
    from aiohttp import web
except ImportError as e:
    print(f"Missing dependencies. Install with: pip install {e.name}")
    exit(1)

# ===========================
# SECURITY ENUMS & CONSTANTS
# ===========================

class SecurityLevel(Enum):
    ALPHA = "alpha"      # Public-facing operations
    BRAVO = "bravo"      # Sensitive intelligence
    CHARLIE = "charlie"  # Classified red team ops
    DELTA = "delta"      # Supreme command

class MessageType(Enum):
    HEARTBEAT = "heartbeat"
    INTEL_REPORT = "intel_report"
    MISSION_DIRECTIVE = "mission_directive"
    STATUS_UPDATE = "status_update"
    EMERGENCY_BURN = "emergency_burn"
    NODE_REGISTRATION = "node_registration"
    THREAT_ALERT = "threat_alert"
    TACTICAL_UPDATE = "tactical_update"

class NodeRole(Enum):
    COMMAND = "command"
    OPERATOR = "operator"
    RELAY = "relay"
    OBSERVER = "observer"

# Security Constants
ENCRYPTION_KEY_SIZE = 32  # 256-bit keys
SIGNATURE_KEY_SIZE = 32
MESSAGE_MAX_AGE = 300     # 5 minutes
HEARTBEAT_INTERVAL = 30   # 30 seconds
KEY_ROTATION_INTERVAL = 3600  # 1 hour

# ===========================
# SECURE MESSAGE STRUCTURES
# ===========================

@dataclass
class SecureMessage:
    message_id: str
    sender_id: str
    recipient_id: str
    message_type: MessageType
    security_level: SecurityLevel
    timestamp: datetime
    payload: Dict[str, Any]
    signature: Optional[str] = None
    encryption_method: str = "AES-256-GCM"

@dataclass
class NodeCredentials:
    node_id: str
    public_key: bytes
    private_key: bytes
    symmetric_key: bytes
    signature_key: bytes
    key_version: int
    expiry: datetime
    security_clearance: SecurityLevel

@dataclass
class NetworkNode:
    node_id: str
    codename: str
    role: NodeRole
    endpoint: str
    public_key: bytes
    last_seen: datetime
    status: str
    security_level: SecurityLevel
    capabilities: List[str]
    trust_score: float

# ===========================
# CRYPTOGRAPHIC ENGINE
# ===========================

class CryptoEngine:
    """
    Advanced cryptographic engine for NodeLink
    Handles encryption, decryption, signatures, and key management
    """
    
    def __init__(self):
        self.active_keys = {}
        self.key_history = {}
        self.signature_keys = {}
        
    def generate_node_credentials(self, node_id: str, security_level: SecurityLevel) -> NodeCredentials:
        """Generate complete cryptographic credentials for a node"""
        
        # Generate RSA key pair for asymmetric operations
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        
        # Serialize keys
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        
        # Generate symmetric key for message encryption
        symmetric_key = secrets.token_bytes(ENCRYPTION_KEY_SIZE)
        
        # Generate signature key
        signature_key = secrets.token_bytes(SIGNATURE_KEY_SIZE)
        
        # Set expiry based on security level
        expiry_hours = {
            SecurityLevel.ALPHA: 24,
            SecurityLevel.BRAVO: 12,
            SecurityLevel.CHARLIE: 6,
            SecurityLevel.DELTA: 3
        }
        
        expiry = datetime.now() + timedelta(hours=expiry_hours[security_level])
        
        return NodeCredentials(
            node_id=node_id,
            public_key=public_pem,
            private_key=private_pem,
            symmetric_key=symmetric_key,
            signature_key=signature_key,
            key_version=1,
            expiry=expiry,
            security_clearance=security_level
        )
    
    def encrypt_message(self, message: str, key: bytes) -> tuple[bytes, bytes, bytes]:
        """Encrypt message using AES-256-GCM"""
        # Generate random IV
        iv = secrets.token_bytes(12)  # 96-bit IV for GCM
        
        # Create cipher
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv))
        encryptor = cipher.encryptor()
        
        # Encrypt message
        ciphertext = encryptor.update(message.encode()) + encryptor.finalize()
        
        return ciphertext, iv, encryptor.tag
    
    def decrypt_message(self, ciphertext: bytes, key: bytes, iv: bytes, tag: bytes) -> str:
        """Decrypt message using AES-256-GCM"""
        cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag))
        decryptor = cipher.decryptor()
        
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        return plaintext.decode()
    
    def sign_message(self, message: str, signature_key: bytes) -> str:
        """Create HMAC signature for message integrity"""
        signature = hmac.new(
            signature_key,
            message.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature
    
    def verify_signature(self, message: str, signature: str, signature_key: bytes) -> bool:
        """Verify HMAC signature"""
        expected_signature = hmac.new(
            signature_key,
            message.encode(),
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(signature, expected_signature)
    
    def derive_session_key(self, shared_secret: bytes, salt: bytes) -> bytes:
        """Derive session key using PBKDF2"""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
        )
        return kdf.derive(shared_secret)

# ===========================
# NODELINK PROTOCOL HANDLER
# ===========================

class NodeLinkProtocol:
    """
    Secure communication protocol for operator network
    Handles message formatting, encryption, and routing
    """
    
    def __init__(self, crypto_engine: CryptoEngine):
        self.crypto = crypto_engine
        self.message_cache = {}
        self.replay_prevention = set()
        
    def create_secure_message(self, 
                            sender_creds: NodeCredentials,
                            recipient_id: str,
                            message_type: MessageType,
                            payload: Dict[str, Any],
                            security_level: SecurityLevel) -> Dict[str, Any]:
        """Create a secure, encrypted message"""
        
        # Create base message
        message = SecureMessage(
            message_id=secrets.token_hex(16),
            sender_id=sender_creds.node_id,
            recipient_id=recipient_id,
            message_type=message_type,
            security_level=security_level,
            timestamp=datetime.now(),
            payload=payload
        )
        
        # Serialize message for encryption
        message_json = json.dumps({
            'message_id': message.message_id,
            'sender_id': message.sender_id,
            'recipient_id': message.recipient_id,
            'message_type': message.message_type.value,
            'security_level': message.security_level.value,
            'timestamp': message.timestamp.isoformat(),
            'payload': message.payload
        })
        
        # Encrypt the message
        ciphertext, iv, tag = self.crypto.encrypt_message(
            message_json, 
            sender_creds.symmetric_key
        )
        
        # Create signature
        signature = self.crypto.sign_message(message_json, sender_creds.signature_key)
        
        # Return encrypted package
        return {
            'message_id': message.message_id,
            'sender_id': message.sender_id,
            'recipient_id': message.recipient_id,
            'encrypted_payload': base64.b64encode(ciphertext).decode(),
            'iv': base64.b64encode(iv).decode(),
            'tag': base64.b64encode(tag).decode(),
            'signature': signature,
            'timestamp': message.timestamp.isoformat(),
            'security_level': message.security_level.value,
            'protocol_version': '1.0'
        }
    
    def decrypt_secure_message(self, 
                             encrypted_message: Dict[str, Any],
                             recipient_creds: NodeCredentials) -> Optional[SecureMessage]:
        """Decrypt and validate a secure message"""
        
        try:
            # Extract components
            message_id = encrypted_message['message_id']
            sender_id = encrypted_message['sender_id']
            encrypted_payload = base64.b64decode(encrypted_message['encrypted_payload'])
            iv = base64.b64decode(encrypted_message['iv'])
            tag = base64.b64decode(encrypted_message['tag'])
            signature = encrypted_message['signature']
            timestamp_str = encrypted_message['timestamp']
            
            # Check for replay attacks
            if message_id in self.replay_prevention:
                logging.warning(f"Replay attack detected for message {message_id}")
                return None
            
            # Check message age
            timestamp = datetime.fromisoformat(timestamp_str)
            if (datetime.now() - timestamp).total_seconds() > MESSAGE_MAX_AGE:
                logging.warning(f"Message {message_id} too old, rejecting")
                return None
            
            # Decrypt the message
            decrypted_json = self.crypto.decrypt_message(
                encrypted_payload,
                recipient_creds.symmetric_key,
                iv,
                tag
            )
            
            # Verify signature
            if not self.crypto.verify_signature(
                decrypted_json,
                signature,
                recipient_creds.signature_key
            ):
                logging.error(f"Signature verification failed for message {message_id}")
                return None
            
            # Parse decrypted message
            message_data = json.loads(decrypted_json)
            
            # Add to replay prevention
            self.replay_prevention.add(message_id)
            
            # Clean old entries from replay prevention
            if len(self.replay_prevention) > 1000:
                self.replay_prevention.clear()
            
            # Return parsed message
            return SecureMessage(
                message_id=message_data['message_id'],
                sender_id=message_data['sender_id'],
                recipient_id=message_data['recipient_id'],
                message_type=MessageType(message_data['message_type']),
                security_level=SecurityLevel(message_data['security_level']),
                timestamp=datetime.fromisoformat(message_data['timestamp']),
                payload=message_data['payload'],
                signature=signature
            )
            
        except Exception as e:
            logging.error(f"Failed to decrypt message: {e}")
            return None

# ===========================
# NODELINK COMMUNICATION HUB
# ===========================

class NodeLinkHub:
    """
    Central communication hub for the NodeLink network
    Manages nodes, routes messages, handles authentication
    """
    
    def __init__(self, host="0.0.0.0", port=8443):
        self.host = host
        self.port = port
        self.crypto = CryptoEngine()
        self.protocol = NodeLinkProtocol(self.crypto)
        self.active_nodes = {}
        self.message_handlers = {}
        self.app = web.Application()
        self.db_path = "nodelink.db"
        
        self._setup_database()
        self._setup_routes()
        self._setup_ssl_context()
        
    def _setup_database(self):
        """Initialize database for persistent storage"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS nodes (
                node_id TEXT PRIMARY KEY,
                codename TEXT,
                role TEXT,
                endpoint TEXT,
                public_key BLOB,
                last_seen TEXT,
                status TEXT,
                security_level TEXT,
                capabilities TEXT,
                trust_score REAL
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                message_id TEXT PRIMARY KEY,
                sender_id TEXT,
                recipient_id TEXT,
                message_type TEXT,
                timestamp TEXT,
                processed BOOLEAN
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS credentials (
                node_id TEXT PRIMARY KEY,
                public_key BLOB,
                private_key BLOB,
                symmetric_key BLOB,
                signature_key BLOB,
                key_version INTEGER,
                expiry TEXT,
                security_clearance TEXT
            )
        """)
        
        conn.commit()
        conn.close()
    
    def _setup_routes(self):
        """Setup HTTP/WebSocket routes"""
        self.app.router.add_post('/api/register', self.handle_node_registration)
        self.app.router.add_post('/api/message', self.handle_secure_message)
        self.app.router.add_get('/api/status', self.handle_status_request)
        self.app.router.add_get('/ws', self.handle_websocket)
    
    def _setup_ssl_context(self):
        """Setup SSL context for secure communications"""
        # In production, use proper certificates
        self.ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        # For development - in production use real certificates
        # self.ssl_context.load_cert_chain('cert.pem', 'key.pem')
    
    async def handle_node_registration(self, request):
        """Handle new node registration"""
        try:
            data = await request.json()
            
            node_id = data['node_id']
            codename = data['codename']
            role = NodeRole(data['role'])
            endpoint = data['endpoint']
            security_level = SecurityLevel(data['security_level'])
            capabilities = data.get('capabilities', [])
            
            # Generate credentials for the node
            credentials = self.crypto.generate_node_credentials(node_id, security_level)
            
            # Create network node record
            node = NetworkNode(
                node_id=node_id,
                codename=codename,
                role=role,
                endpoint=endpoint,
                public_key=credentials.public_key,
                last_seen=datetime.now(),
                status="active",
                security_level=security_level,
                capabilities=capabilities,
                trust_score=1.0
            )
            
            # Store in memory and database
            self.active_nodes[node_id] = node
            self._store_node(node)
            self._store_credentials(credentials)
            
            # Return public credentials to node
            return web.json_response({
                'status': 'registered',
                'node_id': node_id,
                'public_key': base64.b64encode(credentials.public_key).decode(),
                'symmetric_key': base64.b64encode(credentials.symmetric_key).decode(),
                'signature_key': base64.b64encode(credentials.signature_key).decode(),
                'key_version': credentials.key_version,
                'expiry': credentials.expiry.isoformat()
            })
            
        except Exception as e:
            logging.error(f"Node registration failed: {e}")
            return web.json_response({'error': 'Registration failed'}, status=400)
    
    async def handle_secure_message(self, request):
        """Handle incoming secure messages"""
        try:
            encrypted_message = await request.json()
            
            # Get recipient credentials
            recipient_id = encrypted_message['recipient_id']
            recipient_creds = self._load_credentials(recipient_id)
            
            if not recipient_creds:
                return web.json_response({'error': 'Invalid recipient'}, status=400)
            
            # Decrypt message
            message = self.protocol.decrypt_secure_message(encrypted_message, recipient_creds)
            
            if not message:
                return web.json_response({'error': 'Message decryption failed'}, status=400)
            
            # Process message based on type
            await self._process_message(message)
            
            # Log message
            self._log_message(message)
            
            return web.json_response({'status': 'message_processed'})
            
        except Exception as e:
            logging.error(f"Message handling failed: {e}")
            return web.json_response({'error': 'Message processing failed'}, status=400)
    
    async def handle_status_request(self, request):
        """Handle status requests"""
        return web.json_response({
            'status': 'operational',
            'active_nodes': len(self.active_nodes),
            'timestamp': datetime.now().isoformat(),
            'system_health': 'green'
        })
    
    async def handle_websocket(self, request):
        """Handle WebSocket connections for real-time communication"""
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        
        try:
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    data = json.loads(msg.data)
                    # Handle real-time message
                    await self._handle_realtime_message(ws, data)
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    logging.error(f'WebSocket error: {ws.exception()}')
                    
        except Exception as e:
            logging.error(f"WebSocket error: {e}")
        
        return ws
    
    async def _process_message(self, message: SecureMessage):
        """Process decrypted message based on type"""
        if message.message_type == MessageType.HEARTBEAT:
            await self._handle_heartbeat(message)
        elif message.message_type == MessageType.INTEL_REPORT:
            await self._handle_intel_report(message)
        elif message.message_type == MessageType.THREAT_ALERT:
            await self._handle_threat_alert(message)
        elif message.message_type == MessageType.EMERGENCY_BURN:
            await self._handle_emergency_burn(message)
        # Add more message type handlers
    
    async def _handle_heartbeat(self, message: SecureMessage):
        """Handle node heartbeat"""
        if message.sender_id in self.active_nodes:
            self.active_nodes[message.sender_id].last_seen = datetime.now()
            logging.debug(f"Heartbeat received from {message.sender_id}")
    
    async def _handle_intel_report(self, message: SecureMessage):
        """Handle intelligence reports"""
        logging.info(f"Intel report from {message.sender_id}: {message.payload}")
        # Forward to VIBE Core for processing
    
    async def _handle_threat_alert(self, message: SecureMessage):
        """Handle threat alerts"""
        logging.warning(f"Threat alert from {message.sender_id}: {message.payload}")
        # Broadcast to relevant nodes
        await self._broadcast_threat_alert(message)
    
    async def _handle_emergency_burn(self, message: SecureMessage):
        """Handle emergency burn protocols"""
        logging.critical(f"Emergency burn initiated by {message.sender_id}")
        # Execute burn procedures
    
    async def _broadcast_threat_alert(self, message: SecureMessage):
        """Broadcast threat alert to relevant nodes"""
        for node_id, node in self.active_nodes.items():
            if node.security_level.value in ['charlie', 'delta']:
                # Forward threat alert to high-security nodes
                pass
    
    def _store_node(self, node: NetworkNode):
        """Store node in database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO nodes 
            (node_id, codename, role, endpoint, public_key, last_seen, status, security_level, capabilities, trust_score)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            node.node_id,
            node.codename,
            node.role.value,
            node.endpoint,
            node.public_key,
            node.last_seen.isoformat(),
            node.status,
            node.security_level.value,
            json.dumps(node.capabilities),
            node.trust_score
        ))
        
        conn.commit()
        conn.close()
    
    def _store_credentials(self, creds: NodeCredentials):
        """Store node credentials"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT OR REPLACE INTO credentials 
            (node_id, public_key, private_key, symmetric_key, signature_key, key_version, expiry, security_clearance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            creds.node_id,
            creds.public_key,
            creds.private_key,
            creds.symmetric_key,
            creds.signature_key,
            creds.key_version,
            creds.expiry.isoformat(),
            creds.security_clearance.value
        ))
        
        conn.commit()
        conn.close()
    
    def _load_credentials(self, node_id: str) -> Optional[NodeCredentials]:
        """Load node credentials"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM credentials WHERE node_id = ?", (node_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return NodeCredentials(
                node_id=row[0],
                public_key=row[1],
                private_key=row[2],
                symmetric_key=row[3],
                signature_key=row[4],
                key_version=row[5],
                expiry=datetime.fromisoformat(row[6]),
                security_clearance=SecurityLevel(row[7])
            )
        return None
    
    def _log_message(self, message: SecureMessage):
        """Log message to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO messages 
            (message_id, sender_id, recipient_id, message_type, timestamp, processed)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            message.message_id,
            message.sender_id,
            message.recipient_id,
            message.message_type.value,
            message.timestamp.isoformat(),
            True
        ))
        
        conn.commit()
        conn.close()
    
    def run(self):
        """Start the NodeLink hub"""
        logging.info(f"🔗 NodeLink Hub starting on {self.host}:{self.port}")
        logging.info("🔒 Secure communications active")
        
        # For development - use HTTP. In production, use HTTPS with SSL context
        web.run_app(self.app, host=self.host, port=self.port)
        # For production:
        # web.run_app(self.app, host=self.host, port=self.port, ssl_context=self.ssl_context)

# ===========================
# NODELINK CLIENT
# ===========================

class NodeLinkClient:
    """
    Client for connecting to NodeLink network
    Handles authentication, message sending/receiving
    """
    
    def __init__(self, node_id: str, codename: str, hub_endpoint: str):
        self.node_id = node_id
        self.codename = codename
        self.hub_endpoint = hub_endpoint
        self.credentials = None
        self.crypto = CryptoEngine()
        self.protocol = NodeLinkProtocol(self.crypto)
        self.session = None
        
    async def register(self, role: NodeRole, security_level: SecurityLevel, capabilities: List[str]):
        """Register with NodeLink hub"""
        try:
            registration_data = {
                'node_id': self.node_id,
                'codename': self.codename,
                'role': role.value,
                'endpoint': f"node_{self.node_id}",
                'security_level': security_level.value,
                'capabilities': capabilities
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.hub_endpoint}/api/register",
                    json=registration_data
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        # Store credentials
                        self.credentials = NodeCredentials(
                            node_id=data['node_id'],
                            public_key=base64.b64decode(data['public_key']),
                            private_key=b'',  # We don't get private key back
                            symmetric_key=base64.b64decode(data['symmetric_key']),
                            signature_key=base64.b64decode(data['signature_key']),
                            key_version=data['key_version'],
                            expiry=datetime.fromisoformat(data['expiry']),
                            security_clearance=security_level
                        )
                        
                        logging.info(f"✅ Node {self.node_id} registered successfully")
                        return True
                    else:
                        logging.error(f"Registration failed: {response.status}")
                        return False
                        
        except Exception as e:
            logging.error(f"Registration error: {e}")
            return False
    
    async def send_message(self, 
                          recipient_id: str, 
                          message_type: MessageType,
                          payload: Dict[str, Any],
                          security_level: SecurityLevel):
        """Send encrypted message"""
        if not self.credentials:
            logging.error("Node not registered")
            return False
        
        try:
            # Create secure message
            encrypted_message = self.protocol.create_secure_message(
                self.credentials,
                recipient_id,
                message_type,
                payload,
                security_level
            )
            
            # Send via HTTP
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.hub_endpoint}/api/message",
                    json=encrypted_message
                ) as response:
                    return response.status == 200
                    
        except Exception as e:
            logging.error(f"Message send error: {e}")
            return False
    
    async def send_heartbeat(self):
        """Send heartbeat to maintain connection"""
        await self.send_message(
            "hub",
            MessageType.HEARTBEAT,
            {"status": "operational", "timestamp": datetime.now().isoformat()},
            SecurityLevel.ALPHA
        )

# ===========================
# MAIN EXECUTION
# ===========================

def main():
    """Main execution function"""
    logging.basicConfig(level=logging.INFO)
    
    # Start NodeLink Hub
    hub = NodeLinkHub()
    
    print("🔗 NodeLink Secure Communications")
    print("🧠 TYLER Force Multiplier Framework")
    print("🔒 Encrypted operator network active")
    print(f"📡 Hub listening on port {hub.port}")
    
    hub.run()

if __name__ == "__main__":
    main()