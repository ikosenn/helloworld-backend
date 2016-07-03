import os

login_user = os.environ.get('SIL_EMR_STAGING_PG_USER',
                            'emr_staging_user')
login_password = os.environ.get('SIL_EMR_STAGING_PG_PASSWORD',
                                'ready+player-one')
db_user = os.environ.get('SIL_EMR_STAGING_DB_USER',
                         'emr_mockups_user')
db_pass = os.environ.get('SIL_EMR_STAGING_DB_PASSWORD',
                         'emr_mockups')
db_name = os.environ.get('SIL_EMR_STAGING_DB_NAME',
                         'emr_backend')
secret_key = os.environ.get('secret_key', '')
front_end_url = os.environ.get('SIL_EMR_FRONTEND_URL', '')
libcloud_user = os.environ.get('SIL_EMR_LIBCLOUD_USER', '')
libcloud_key = os.environ.get('SIL_EMR_LIBCLOUD_KEY', '')
aws_key_id = os.environ.get('SIL_EMR_AWS_KEY_ID', '')
aws_secret = os.environ.get('SIL_EMR_AWS_SECRET', '')
libcloud_storage = os.environ.get('SIL_EMR_LIBCLOUD_PROVIDER', 'google')
libcloud_provider = os.environ.get(
    'SIL_EMR_LIBCLOUD_STORAGE', 'djlibcloud.storage.LibCloudStorage')
libcloud_type = os.environ.get(
    'SIL_EMR_LIBCLOUD_TYPE', 'libcloud.storage.types.Provider.GOOGLE_STORAGE')
libcloud_bucket = os.environ.get('SIL_EMR_LIBCLOUD_BUCKET', 'emr-images')
