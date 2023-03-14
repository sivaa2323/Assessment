from datetime import datetime
with open('C:/Users/Siva Sankar RAJU/Downloads/net_square_assesment/samplelog.txt', 'r') as f:
    lines = f.readlines()

    user_sessions = {}
    for line in lines:
        parts = line.strip().split()
        if len(parts) < 3: #timestamp, username, and action 
            continue
            
        try:
            time = datetime.strptime(parts[0], '%H:%M:%S')
        except ValueError:
           continue 
        
        user = parts[1]
        action = parts[2]

        if action == 'Start':
            if user not in user_sessions:
                user_sessions[user] = []
            user_sessions[user].append((time, None))
        elif action == 'End':
            if user not in user_sessions:
                continue
            if user_sessions[user][-1][1] is None:
                user_sessions[user][-1] = (user_sessions[user][-1][0], time)
            else:
                continue
        else:
            continue

    for user, sessions in user_sessions.items():
        session_count = len(sessions)
        total_duration = 0
        for start_time, end_time in sessions:
            if end_time is None:
                end_time = time
            duration = (end_time - start_time).total_seconds()
            total_duration += duration
       
        print(f"{user} {session_count} {total_duration}")







