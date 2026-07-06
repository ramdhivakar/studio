from enum import Enum


class DeploymentType(str, Enum):
    ON_PREM = "on_prem"
    CLOUD = "cloud"
    HYBRID = "hybrid"


class ProductStatus(str, Enum):
    ACTIVE = "active"
    DEPRECATED = "deprecated"
    END_OF_LIFE = "end_of_life"


class KnowledgeType(str, Enum):
    INSTALLATION = "installation"
    TROUBLESHOOTING = "troubleshooting"
    CONFIGURATION = "configuration"
    KB_ARTICLE = "kb_article"
    RELEASE_NOTE = "release_note"
    INTERNAL_NOTE = "internal_note"