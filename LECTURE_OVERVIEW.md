# <span style="color:orange">Lecture overview</span>

Welcome to the "Integrating Action Secrets in GitHub Workflows" course section! In this module, we will guide you through the process of adding action secrets to your GitHub repositories to enhance the security and efficiency of your automated workflows.

Our GitHub workflow is expecting a bunch of secrets in order for it function correctly. Please ensure you add the following secrets to your repository:

Secret name | Detail | Example 
--- | --- | ---
CELERY_BACKEND| Backend used by Celery - please add your REDIS_PASSWORD. In the example I have used password 123456.| redis://:123456@redis:6379
CELERY_BROKER| Broker used by Celery - please add your REDIS_PASSWORD. In the example I have used password 123456. | redis://:123456@redis:6379
NAMESPACE| GitHub username | bobby-didcoding
PERSONAL_ACCESS_TOKEN| [Create a new github personal access token](https://github.com/settings/tokens/new) | lashfhfolsahfjrshd
PROD_AWS_ACCESS_KEY_ID| Your Digital Ocean spaces api key : https://cloud.digitalocean.com/account/api/spaces | argertehbtghsrhbshbtrg
PROD_AWS_LOCATION| Then name of the static directory in Digital Ocean | static
PROD_AWS_MEDIA_LOCATION| Then name of the media directory in Digital Ocean | media
PROD_AWS_S3_ENDPOINT_URL| You Digital Ocean spaces url | nyc3.digitaloceanspaces.com
PROD_AWS_SECRET_ACCESS_KEY| Your Digital Ocean spaces secret api key : https://cloud.digitalocean.com/account/api/spaces | lkvfrngfvorfihg;raesghfvohg
PROD_AWS_STORAGE_BUCKET_NAME| You Digital Ocean spaces bucket name | course
PROD_CERT_KEY| Your Cloudflare origin service ssl cert key : https://dash.cloudflare.com/**your-id**>/**site-name**>/ssl-tls/origin | XXX
PROD_CERT_PEM| Your Cloudflare origin service ssl cert pem : https://dash.cloudflare.com/**your-id**>/**site-name**>/ssl-tls/origin | XXX
PROD_COOKIE_BOT| Your cookiebot domain group id https://manage.cookiebot.com/en/manage | 13213213-45465456-4564564-4564
PROD_DB_ENGINE| PostgreSQL engine | django.db.backends.postgresql
PROD_DB_HOST| Digital Ocean database host name | abc.ondigitalocean.com
PROD_DB_NAME| Database name | stage
PROD_DB_PASSWORD| Database user password | 1234567
PROD_DB_PORT| Database port | 25060
PROD_DB_USER| Database user | prod
PROD_DJANGO_ALLOWED_HOSTS| You domain | stage.bobbystearman.co.uk
PROD_DOCKER_CONTAINER_EMAIL| Your email address to access containers in UI | bobby@didcoding.com
PROD_DOCKER_CONTAINER_PASSWORD| Your password to access containers in UI | my-password
PROD_EMAIL_ADDRESS| Your email address used to send emails | bobby@didcoding.com
PROD_EMAIL_DISPLAY_NAME| The name displayed on emails | Did Coding
PROD_EMAIL_HOST| The email provider | smtp.gmail.com
PROD_EMAIL_PASSWORD| Your email password (Google app password) | lhfljrehfklerhx
PROD_EMAIL_PORT| Email provider port | 587
PROD_EMAIL_USE_TLS| TLS option | 1
PROD_IP_ADDRESS| Your Digital Ocean Droplet IP address | 123.12.3.456
PROD_PRIVATE_KEY| Your private SSH key | XXX
PROD_RECAPTCHA_PRIVATE_KEY| Your reCaptcha private key | 5464513125464154614356
PROD_RECAPTCHA_PUBLIC_KEY| Your reCaptcha public key | 5364173196846831468
PROD_REDIS_PASSWORD| Your Redis password - you need to add this to CELERY_BACKEND and CELERY_BROKER | 123456
PROD_SECRET_KEY| Your Django secret key | jhfabrgfojlrhnvflnrvfklenrvgfkldnevgklx
PROD_SENTRY_DNS| Your Sentry DNS | https://12345.ingest.sentry.io/12345
PROD_STRIPE_PUBLISHABLE| Your LIVE Stripe publishable key | pk_live_klsghflhrgfljshrgfx
PROD_STRIPE_SECRET| Your LIVE Stripe API key | sk_live_klhfklsrhfklrhgfklx
PROD_SUPPORT_EMAIL| Email address that is added to emails | bobby@didcoding.com
STAGE_AWS_ACCESS_KEY_ID| Your Digital Ocean spaces api key : https://cloud.digitalocean.com/account/api/spaces | argtfgbvsthstgfr
STAGE_AWS_LOCATION| Then name of the static directory in Digital Ocean | static
STAGE_AWS_MEDIA_LOCATION| Then name of the media directory in Digital Ocean | media
STAGE_AWS_S3_ENDPOINT_URL| You Digital Ocean spaces url | nyc3.digitaloceanspaces.com
STAGE_AWS_SECRET_ACCESS_KEY| Your Digital Ocean spaces secret api key : https://cloud.digitalocean.com/account/api/spaces | lkvfrngfvorfihg;raesghfvohg
STAGE_AWS_STORAGE_BUCKET_NAME| You Digital Ocean spaces bucket name | course
STAGE_CERT_KEY| Your Cloudflare origin service ssl cert key : https://dash.cloudflare.com/**your-id**>/**site-name**>/ssl-tls/origin | XXX
STAGE_CERT_PEM| Your Cloudflare origin service ssl cert pem : https://dash.cloudflare.com/**your-id**>/**site-name**>/ssl-tls/origin | XXX
STAGE_COOKIE_BOT| Your cookiebot domain group id https://manage.cookiebot.com/en/manage | 13213213-45465456-4564564-4564
STAGE_DB_ENGINE| PostgreSQL engine | django.db.backends.postgresql
STAGE_DB_HOST| Digital Ocean database host name | abc.ondigitalocean.com
STAGE_DB_NAME| Database name | stage
STAGE_DB_PASSWORD| Database user password | 1234567
STAGE_DB_PORT| Database port | 25060
STAGE_DB_USER| Database user | prod
STAGE_DJANGO_ALLOWED_HOSTS| You domain | stage.bobbystearman.co.uk
STAGE_DOCKER_CONTAINER_EMAIL| Your email address to access containers in UI | bobby@didcoding.com
STAGE_DOCKER_CONTAINER_PASSWORD| Your password to access containers in UI | my-password
STAGE_EMAIL_ADDRESS| Your email address used to send emails | bobby@didcoding.com
STAGE_EMAIL_DISPLAY_NAME| The name displayed on emails | Did Coding
STAGE_EMAIL_HOST| The email provider | smtp.gmail.com
STAGE_EMAIL_PASSWORD| Your email password (Google app password) | lhfljrehfklerhx
STAGE_EMAIL_PORT| Email provider port | 587
STAGE_EMAIL_USE_TLS| TLS option | 1
STAGE_IP_ADDRESS| Your Digital Ocean Droplet IP address | 123.12.3.456
STAGE_PRIVATE_KEY| Your private SSH key | XXX
STAGE_RECAPTCHA_PRIVATE_KEY| Your reCaptcha private key | 5464513125464154614356
STAGE_RECAPTCHA_PUBLIC_KEY| Your reCaptcha public key | 5364173196846831468
STAGE_REDIS_PASSWORD| Your Redis password - you need to add this to CELERY_BACKEND and CELERY_BROKER | 123456
STAGE_SECRET_KEY| Your Django secret key | jhfabrgfojlrhnvflnrvfklenrvgfkldnevgklx
STAGE_SENTRY_DNS| Your Sentry DNS | https://12345.ingest.sentry.io/12345
STAGE_STRIPE_PUBLISHABLE| Your LIVE Stripe publishable key | pk_test_klsghflhrgfljshrgfx
STAGE_STRIPE_SECRET| Your LIVE Stripe API key | sk_test_klhfklsrhfklrhgfklx
STAGE_SUPPORT_EMAIL| Email address that is added to emails | bobby@didcoding.com

# <span style="color:orange">Code changes</span>

You can find all code changes [here](https://github.com/bobby-didcoding/build-and-deploy-dockerised-django-app-handbook/pull/28/files).


***
***