# --------------------------------------------------------------
# App imports
# --------------------------------------------------------------

from core.admin.policy import PolicyAdmin
from core.admin.contact import ContactAdmin
from core.admin.blog import BlogAdmin
from core.admin.newsletter import NewsLetterAdmin
from core.admin.certificate import CertificateAdmin
from core.admin.portfolio import PortfolioAdmin
from core.admin.skill import SkillAdmin
from core.admin.testimonial import TestimonialAdmin

__all__ = [
    PolicyAdmin,
    ContactAdmin,
    BlogAdmin,
    NewsLetterAdmin,
    CertificateAdmin,
    PortfolioAdmin,
    SkillAdmin,
    TestimonialAdmin,
]
