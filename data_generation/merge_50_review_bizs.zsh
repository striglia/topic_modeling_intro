#! /bin/zsh
# To run, simply unpack the Yelp dataset into this folder and run this script.
# You can alter the values of the variables to change what businesses are
# selected.

MIN_REVIEWS=40
MAX_REVIEWS=50
OUTPUT='biz_and_review_sample.json.gz'
TMP_BIZ_FILE='small_businesses.json'

# Selects out the businesses we care about and a subset of their data.
cat yelp_academic_dataset_business.json \
	| jq -c "select(.review_count >= $MIN_REVIEWS) | select(.review_count <= $MAX_REVIEWS) | {business_id:.business_id, name:.name, categories:.categories }" \
	> $TMP_BIZ_FILE

# Join each business against its reviews.
cat $TMP_BIZ_FILE yelp_academic_dataset_review.json \
	| jq -s -f join_biz_and_review.jq -c \
	| gzip > $OUTPUT

rm $TMP_BIZ_FILE
