import basc_py4chan
import re
def clean_data(post)->str:
    new_post = re.sub('[^A-Za-z0-9]+', ' ',post)
    new_post = re.sub('\d{9}', '',new_post)
    return new_post

def main():
    b = basc_py4chan.get_boards(['a','b','c','w','m','cgl','cm','f','n','jp','vt'])
    with open ('4_chan_data_clean.txt', 'w') as f:
        for tag in b:
            threads = tag.get_all_threads()
            for thread in threads:
                for post in thread.all_posts:
                    f.write( clean_data(post.text_comment))
                    # f.write(clean_data(post))
    f.close()
                
if __name__ == '__main__':
    main()