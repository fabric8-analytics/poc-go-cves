# -*- coding: utf-8 -*-
"""
This file contains the constants for interaction with AWS/Minio.
Note: Please don't add keys directly here, refer to environment variables
"""

import os

# Please make sure you have your AWS envt variables setup
AWS_S3_REGION = os.environ.get('AWS_S3_REGION', 'us-east-1')
AWS_S3_ACCESS_KEY_ID = os.environ.get('AWS_S3_ACCESS_KEY_ID', '')
AWS_S3_SECRET_ACCESS_KEY = os.environ.get('AWS_S3_SECRET_ACCESS_KEY', '')

# you don't need to change this
S3_BUCKET_NAME = 'dsarkar-dev-gokube-triage'

# Please set the following to point to your BQ auth credentials JSON
BIGQUERY_CREDENTIALS_FILEPATH = '../../auth/bq_key.json'

# you probably don't need to change this
GOKUBE_REPO_LIST = './utils/data_assets/golang-repo-list.txt'

# you probably don't need to change this
SEC_MODEL_TOKENIZER_PATH = './models/model_assets/gokube-phase1-jun19/embeddings/security_tokenizer_word2idx_fulldata.pkl'
SEC_MODEL_WEIGHTS_PATH = './models/model_assets/gokube-phase1-jun19/saved_models/security_model_train99-jun19_weights.h5'

# you probable don't need to change this
CVE_MODEL_TOKENIZER_PATH = './models/model_assets/gokube-phase1-jun19/embeddings/cve_tokenizer_word2idx_fulldata.pkl'
CVE_MODEL_WEIGHTS_PATH = './models/model_assets/gokube-phase1-jun19/saved_models/cve_model_train99-jun19_weights.h5'
