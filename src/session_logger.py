import json
import os
import copy
from datetime import datetime
from typing import Dict, Any, Optional

class SessionLogger:
    """
    A class to log the state of an interactive session.
    
    This logger provides methods to track and persist session information,
    including timestamps, metadata, and custom state data.
    """
    
    def __init__(self, 
                 log_dir: str = 'session_logs', 
                 session_id: Optional[str] = None):
        """
        Initialize the SessionLogger.
        
        Args:
            log_dir (str, optional): Directory to store session logs. 
                                     Defaults to 'session_logs'.
            session_id (str, optional): Custom session identifier. 
                                        If not provided, a timestamp-based ID is generated.
        """
        # Ensure log directory exists
        os.makedirs(log_dir, exist_ok=True)
        
        # Generate or use provided session ID
        self.session_id = session_id or datetime.now().strftime('%Y%m%d_%H%M%S')
        self.log_dir = log_dir
        
        # Initialize session metadata
        self.session_data: Dict[str, Any] = {
            'session_id': self.session_id,
            'start_time': datetime.now().isoformat(),
            'metadata': {},
            'state': {}
        }
    
    def add_metadata(self, key: str, value: Any) -> None:
        """
        Add metadata to the session.
        
        Args:
            key (str): Metadata key
            value (Any): Metadata value
        """
        self.session_data['metadata'][key] = value
    
    def update_state(self, key: str, value: Any) -> None:
        """
        Update the session state.
        
        Args:
            key (str): State key
            value (Any): State value
        """
        self.session_data['state'][key] = value
    
    def log_session(self) -> str:
        """
        Log the current session state to a JSON file.
        
        Returns:
            str: Path to the logged session file
        """
        # Add end time to session data
        self.session_data['end_time'] = datetime.now().isoformat()
        
        # Create log file path
        log_file = os.path.join(
            self.log_dir, 
            f'session_{self.session_id}.json'
        )
        
        # Write session data to JSON file
        with open(log_file, 'w') as f:
            json.dump(self.session_data, f, indent=2)
        
        return log_file
    
    def get_session_data(self) -> Dict[str, Any]:
        """
        Retrieve the current session data.
        
        Returns:
            Dict[str, Any]: Deep copy of current session data
        """
        return copy.deepcopy(self.session_data)