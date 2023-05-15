import pytest
from unittest.mock import Mock
from snoosnooper.script import kw_in_submission


def test_kw_in_submission_title_true():
   # creating mock submission
   mock_submission = Mock()
   mock_submission.title = "synology title"
   mock_submission.selftext = "bleh"

   assert kw_in_submission(mock_submission, "synology")


def test_kw_in_submission_title_false():
   # creating mock submission
   mock_submission = Mock()
   mock_submission.title = "synology title"
   mock_submission.selftext = "bleh"

   assert not kw_in_submission(mock_submission, "gtx")


def test_kw_in_submission_selftext_true():
   # creating mock submission
   mock_submission = Mock()
   mock_submission.title = "title"
   mock_submission.selftext = "bleh synology"

   assert kw_in_submission(mock_submission, "synology") 


def test_kw_in_submission_selftext_false():
   # creating mock submission
   mock_submission = Mock()
   mock_submission.title = "title"
   mock_submission.selftext = "bleh"

   assert not kw_in_submission(mock_submission, "synology")        
