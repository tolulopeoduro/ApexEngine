"""Polymorphic scene models supporting multiple genres."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class VideoGenre(str, Enum):
    """Supported video genres."""
    EXPLAINER = "explainer"
    NARRATIVE = "narrative"
    DOCUMENTARY = "documentary"
    GAMING = "gaming"
    SOCIAL_SHORT = "social_short"
    CUSTOM = "custom"


@dataclass
class Scene(ABC):
    """Base polymorphic scene model."""
    id: str
    duration_seconds: float
    genre: VideoGenre
    metadata: Dict[str, Any] = field(default_factory=dict)

    @abstractmethod
    def validate_scene(self) -> bool:
        """Validate genre-specific scene requirements."""
        raise NotImplementedError


@dataclass
class ExplainerScene(Scene):
    """Explainer scene with voiceover narration and focal visual concepts."""
    narration_script: str = ""
    visual_prompt: str = ""
    genre: VideoGenre = VideoGenre.EXPLAINER

    def validate_scene(self) -> bool:
        return bool(self.narration_script and self.duration_seconds > 0)


@dataclass
class NarrativeScene(Scene):
    """Narrative cinematic scene with dialogues, character actions, and atmosphere."""
    dialogue: List[Dict[str, str]] = field(default_factory=list)
    camera_movement: Optional[str] = None
    mood: Optional[str] = None
    genre: VideoGenre = VideoGenre.NARRATIVE

    def validate_scene(self) -> bool:
        return self.duration_seconds > 0


@dataclass
class SocialShortScene(Scene):
    """Fast-paced social media short scene with hook, captions, and overlays."""
    hook_text: str = ""
    captions: List[str] = field(default_factory=list)
    call_to_action: Optional[str] = None
    genre: VideoGenre = VideoGenre.SOCIAL_SHORT

    def validate_scene(self) -> bool:
        return self.duration_seconds > 0
