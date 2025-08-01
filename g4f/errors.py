class ProviderNotFoundError(Exception):
    ...

class ProviderNotWorkingError(Exception):
    ...

class StreamNotSupportedError(Exception):
    ...

class ModelNotFoundError(Exception):
    ...

class ModelNotAllowedError(Exception):
    ...

class RetryProviderError(Exception):
    ...

class RetryNoProviderError(Exception):
    ...

class VersionNotFoundError(Exception):
    ...

class MissingRequirementsError(Exception):
    ...

class NestAsyncioError(MissingRequirementsError):
    ...

class MissingAuthError(Exception):
    ...

class PaymentRequiredError(Exception):
    ...

class NoMediaResponseError(Exception):
    ...

class ResponseError(Exception):
    ...

class ResponseStatusError(Exception):
    ...

class CloudflareError(ResponseStatusError):
    ...

class RateLimitError(ResponseStatusError):
    ...

class NoValidHarFileError(Exception):
    ...

class TimeoutError(Exception):
    """Raised for timeout errors during API requests."""

class ConversationLimitError(Exception):
    """Raised for conversation limit during API requests to AI endpoint."""