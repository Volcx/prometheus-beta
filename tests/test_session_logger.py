import os
import json
import pytest
from datetime import datetime
from src.session_logger import SessionLogger

def test_session_logger_initialization():
    """Test basic initialization of SessionLogger."""
    logger = SessionLogger()
    
    # Check session ID is generated
    assert logger.session_id is not None
    assert isinstance(logger.session_id, str)
    
    # Check log directory exists
    assert os.path.exists('session_logs')

def test_add_metadata():
    """Test adding metadata to the session."""
    logger = SessionLogger()
    logger.add_metadata('user', 'testuser')
    logger.add_metadata('environment', 'testing')
    
    session_data = logger.get_session_data()
    assert session_data['metadata']['user'] == 'testuser'
    assert session_data['metadata']['environment'] == 'testing'

def test_update_state():
    """Test updating session state."""
    logger = SessionLogger()
    logger.update_state('step', 'initialization')
    logger.update_state('progress', 50)
    
    session_data = logger.get_session_data()
    assert session_data['state']['step'] == 'initialization'
    assert session_data['state']['progress'] == 50

def test_log_session():
    """Test logging session to a file."""
    # Use a unique session ID to avoid conflicts
    session_id = datetime.now().strftime('%Y%m%d_%H%M%S_test')
    logger = SessionLogger(session_id=session_id)
    
    # Add some data
    logger.add_metadata('user', 'testuser')
    logger.update_state('step', 'processing')
    
    # Log the session
    log_file = logger.log_session()
    
    # Verify log file was created
    assert os.path.exists(log_file)
    
    # Verify log file contents
    with open(log_file, 'r') as f:
        logged_data = json.load(f)
    
    assert logged_data['session_id'] == session_id
    assert logged_data['metadata']['user'] == 'testuser'
    assert logged_data['state']['step'] == 'processing'
    assert 'start_time' in logged_data
    assert 'end_time' in logged_data

def test_get_session_data():
    """Test retrieving session data."""
    logger = SessionLogger()
    logger.add_metadata('test', 'data')
    logger.update_state('status', 'running')
    
    session_data = logger.get_session_data()
    
    # Verify metadata and state
    assert session_data['metadata']['test'] == 'data'
    assert session_data['state']['status'] == 'running'
    
    # Verify it's a copy (modifying won't affect original)
    session_data['metadata']['new_key'] = 'test'
    assert 'new_key' not in logger.get_session_data()['metadata']

def test_custom_log_directory():
    """Test creating a session logger with a custom log directory."""
    custom_dir = 'custom_logs'
    logger = SessionLogger(log_dir=custom_dir)
    
    # Verify custom directory exists
    assert os.path.exists(custom_dir)
    
    # Log session and verify file in custom directory
    log_file = logger.log_session()
    assert log_file.startswith(custom_dir)

# Clean up log directories after tests
def teardown_module(module):
    """Remove any created log directories after tests."""
    for log_dir in ['session_logs', 'custom_logs']:
        if os.path.exists(log_dir):
            for file in os.listdir(log_dir):
                os.remove(os.path.join(log_dir, file))
            os.rmdir(log_dir)