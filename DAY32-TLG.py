# cook your dish here
N = int(input())

cumulative_score_player1 = 0
cumulative_score_player2 = 0

max_lead = 0
winner = 0

for _ in range(N):
    
    Si, Ti = map(int, input().split())
    
    cumulative_score_player1 += Si
    cumulative_score_player2 += Ti
    
    
    current_lead = cumulative_score_player1 - cumulative_score_player2
    
    
    if abs(current_lead) > max_lead:
        max_lead = abs(current_lead)
        winner = 1 if current_lead > 0 else 2
print(winner, max_lead)