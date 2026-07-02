import logging

logger = logging.getLogger('flask_ask')
logger.addHandler(logging.StreamHandler())
if logger.level == logging.NOTSET:
    logger.setLevel(logging.WARN)


from .core import (  # noqa: E402
    Ask as Ask,
    request as request,
    session as session,
    version as version,
    context as context,
    current_stream as current_stream,
    convert_errors as convert_errors,
)

from .models import (  # noqa: E402
    question as question,
    statement as statement,
    audio as audio,
    delegate as delegate,
    elicit_slot as elicit_slot,
    confirm_slot as confirm_slot,
    confirm_intent as confirm_intent,
    buy as buy,
    upsell as upsell,
    refund as refund,
)
