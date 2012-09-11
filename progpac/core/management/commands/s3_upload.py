from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from boto.s3.connection import S3Connection
from boto.s3.key import Key

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        import os

        conn = S3Connection(
            settings.AWS_ACCESS_KEY_ID,
            settings.AWS_SECRET_ACCESS_KEY
        )
        bucket = conn.create_bucket(settings.AWS_STORAGE_BUCKET_NAME)
        bucket.delete_keys(bucket.get_all_keys())
        # bucket = conn.create_bucket(settings.AWS_STORAGE_BUCKET_NAME)
        # CACHE_DIR = '%s/CACHE' % settings.STATIC_ROOT

        for root, dirs, files in os.walk('%s/CACHE' % settings.STATIC_ROOT):

            for f in files:

                k = Key(bucket)
                k.key = "%s/%s" % (root.lstrip(settings.STATIC_ROOT), f)

                k.set_contents_from_filename('%s/%s' % (root,f))
                k.set_acl('public-read')
