# ########### See more at: http://docs.mongoengine.org/guide/connecting.html
# from mongoengine import connect as conn

# conn = connect('twitter_post', host='localhost', port=9200)

# ### Replica Sets
# conn = connect('twitter_post', replicaset='rs-twitter_post')

# class Twitter():
#   meta = {
#     'db_alias': 'twitter_post'
#   }

# ### Switch DB
# with switch_db(Twitter, 'archive-twitter-post') as Twitter:
#   Twitter(name='Robin888').save() # Save the 'archive-twitter-post'

# ### Switch Collection
# with switch_collection(Group, 'group2000') as Group:
#   Group(name='hello Group 2000 collection!').save()
