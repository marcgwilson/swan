from django.conf import settings
from swan.codec.codec import IDCodec


base62 = IDCodec(settings.CIPHER_KEY,
	settings.ALPHABET,
	settings.HASH_KEY_SIZE,
	settings.HASH_ID_SIZE)
