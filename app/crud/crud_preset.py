from psycopg2 import IntegrityError

from app.api.error import Exception404, Exception409
from app.crud.base import CRUDBase
from app.models.post import Post
from app.schemas.post import PostCreate, PostUpdate
from app.utils.logger import make_logger

logger = make_logger(__name__)


class CRUDPreset(CRUDBase[Post, PostCreate, PostUpdate]):
    def create_preset(self, preset: PostCreate) -> Post | None:
        try:
            created_preset = self.create(obj_in=preset)
        except IntegrityError as e:
            logger.error(e)
            raise Exception409(type="PresetAlreadyExists")
        return created_preset

    def update_preset(self, preset_update: PostUpdate) -> Post:
        preset = self.get_by_id(id=preset_update.id)

        if not preset:
            raise Exception404(type="PresetDoesNotExists")

        logger.info(f"preset info: {preset_update}")

        return self.update(db_obj=preset, obj_in=preset_update)
