# Make sure to invoke with `-s`
# `cat biz.json review.json | jq -s -f join_biz_and_review.jq`

# Pulls together by business_id
group_by(.business_id)
# This part is tricky. We want to accumulate a dict but we have to do it carefully depending on whether we're looking at a biz or a review.
| map(reduce .[] as $i 
	# Our merged dicts start with an empty reviews list
	({"reviews": []};
		(
			# If our incoming dict has categories, it's a biz so just accumulate name and cats.
			. as $accumulator | $i | if has("categories") then $accumulator + {business_id:$i.business_id, name:$i.name, categories:$i.categories}
			# Else, it's a review, so accumulate the review text into our array.
			else $accumulator + {reviews:($accumulator.reviews+[$i.text])}
			end
		)
	)
)
| map(select(has("categories")))
| .[]
