from abc import ABCMeta, abstractmethod

import firebase_admin
from firebase_admin import firestore


class BaseModel(metaclass=ABCMeta):
    """CRUD for Firestore."""

    def __init__(self, doc_id, attrs):
        self.doc_id = doc_id
        self.attrs = attrs

    @property
    @abstractmethod
    def collection(self):
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

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def destroy(self):
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
