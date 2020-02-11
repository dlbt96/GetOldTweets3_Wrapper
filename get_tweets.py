def get_tweets(query,start_date,end_date,parent_path):
    
    start = start_date # initial start

    # Create folder if not existed
    folder_name = query.replace(' ','_')
    folder_name = parent_path+'/'+folder_name
    subprocess.call('mkdir -p {}'.format(folder_name),shell=True)

    # Find the latest date downloaded
    files = os.listdir(folder_name)
    if files != []:
        files.sort()
        start = files[-1].split('_')[-1].split('.')[0].split(' ')[0] # keep splitting the string to get the date

    start = datetime.datetime.strptime(start,'%Y-%m-%d')
    end = start
    end_date = datetime.datetime.strptime(end_date,'%Y-%m-%d')
    file_name = folder_name+'/'+'twitter_' + query.replace(' ','_')

    if start == end_date:
        return
    while (end <= end_date):
        end = start + datetime.timedelta(days=1)
        since_date = datetime.datetime.strftime(start,'%Y-%m-%d')
        until_date = datetime.datetime.strftime(end,'%Y-%m-%d')
        output = file_name + '_' + since_date + '.csv'
        cmd = 'GetOldTweets3 --querysearch "{query}" --since {since_date} --until {until_date} --lang en --emoji ignore --output {output}'.format(query=query,since_date=since_date,until_date=until_date,output=output)
        subprocess.call(cmd,shell=True)
        start = end
        print('Done for query {} on {}'.format(query,since_date))
        time.sleep(10)
