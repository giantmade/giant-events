from unittest import mock

from django.test import TestCase

from events.models import Event, EventQuerySet
from events.search_indexes import EventIndex
from haystack.indexes import SearchIndex


class EventIndexTest(TestCase):
    """
    Test case for the EventIndex search index
    """

    def test_get_model(self):
        """
        Test the get_model method returns the EventIndex class
        """

        assert EventIndex().get_model() == Event

    def test_prepare_tags(self):
        """
        Test the prepare_tags method on the EventIndex class
        """

        event = mock.Mock()
        event.tags.values_list.return_value = ["tag1", "tag2"]
        assert EventIndex().prepare_tags(event) == ["tag1", "tag2"]
        # Test the prepare tags method is called correctly
        event.tags.values_list.assert_called_once_with("pk", flat=True)

    @mock.patch.object(EventQuerySet, "published", mock.Mock(return_value="published"))
    def test_index_queryset(self):
        """
        Test that the queryset returns only published events
        """

        assert EventIndex().index_queryset() == "published"

    @mock.patch.object(SearchIndex, "remove_object")
    @mock.patch.object(SearchIndex, "update_object", mock.Mock(return_value="updated"))
    def test_update_object_published(self, method):
        """
        Test an object is updated when marked as published
        """

        obj = mock.Mock()
        obj.is_published = True
        EventIndex().remove_object = mock.Mock()
        assert EventIndex().update_object(obj) == "updated"
        EventIndex().remove_object.assert_not_called()

    @mock.patch.object(SearchIndex, "remove_object")
    @mock.patch.object(SearchIndex, "update_object")
    def test_update_object_not_published(self, update_method, remove_method):
        """
        Test an object is removed from the index when the object is unpublished
        """

        index = EventIndex()
        obj = mock.Mock()
        obj.is_published = False
        index.remove_object = mock.Mock(return_value="removed")
        assert index.update_object(obj) == "removed"
        update_method.assert_not_called()
