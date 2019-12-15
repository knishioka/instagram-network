from abc import ABCMeta, abstractmethod

import firebase_admin
from firebase_admin import firestore


class BaseModel(metaclass=ABCMeta):
    """CRUD for Firestore."""

    def __init__(self, doc_id, attrs):
        """Initialize firebase model.

        Args:
            doc_id (str): firestore document id.
            attrs (dict): custome attributes which key will be variable name.

        Returns:
            BaseModel

        """
        self.doc_id = doc_id
        for k in self.valid_keys:
            setattr(self, k, attrs.get(k))

    @property
    @abstractmethod
    def collection(self):
        """Firebase collection name."""
        raise NotImplementedError

    @property
    @abstractmethod
    def valid_keys(self):
        """Valid custom attribution list."""
        raise NotImplementedError

    def connection():
        """Create connection to firebase."""
        if (not len(firebase_admin._apps)):
            firebase_admin.initialize_app()
        return firestore.client()

    @classmethod
    def document(cls, doc_id):
        """Create document reference.

        Args:
            cls (BaseModel): class itself.
            doc_id: firebase document_id.

        Returns:
            google.cloud.firestore_v1.document.DocumentReference

        """
        db = BaseModel.connection()
        return db.collection(cls.collection).document(doc_id)

    @classmethod
    def create(cls, doc_id, attrs={}):
        """Create firebase document.

        Args:
            cls (BaseModel): class itself.
            doc_id: firebase document_id.
            attrs: document attributes.

        Returns:
            BaseModel

        """
        doc = cls.document(doc_id)
        doc.set(attrs)
        return cls(doc_id=doc_id, attrs=doc.get().to_dict())

    def update(self):
        """Update data to firebase."""
        pass

    def destroy(self):
        """Destroy data from firebase."""
        pass

    @classmethod
    def find(cls, doc_id):
        """Find firebase document.

        Args:
            cls (BaseModel): class itself.
            doc_id: firebase document_id.

        Returns:
            BaseModel

        """
        doc = cls.document(doc_id)
        return cls(doc_id=doc_id, attrs=doc.get().to_dict())
