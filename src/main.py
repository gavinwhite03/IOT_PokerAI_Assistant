import random
from src.poker_ai.cfr_poker_agent import cfr_poker_agent
from poker_ai.poker_env import PokerEnv

def main():
    # Set up the poker environment and agents
    env = PokerEnv()  # This would initialize the poker game environment.
    agent1 = cfr_poker_agent()
    agent2 = cfr_poker_agent()

    num_episodes = 10000  # Set the number of poker games to simulate.
    wins = {1: 0, 2: 0}  # Track wins for each agent
    
    for episode in range(num_episodes):
        env.reset()  # Reset environment at the start of each game
        
        done = False
        current_player = 1  # Start with player 1; will switch each episode

        while not done:
            # Get the agent corresponding to the current player
            current_agent = agent1 if current_player == 1 else agent2
            
            # Retrieve the game state from the environment
            state = env.get_state(current_player)
            
            # Use CFR agent to select an action
            action = current_agent.select_action(state)

            # Take the action in the environment
            next_state, reward, done, info = env.step(action)

            # Update agent with outcome and store regrets
            if done:
                if reward > 0:
                    wins[current_player] += 1
                current_agent.update_regret(state, action, reward)

            # Switch players
            current_player = 1 if current_player == 2 else 2

        # Print a simple progress update every 1000 games
        if (episode + 1) % 1000 == 0:
            print(f"Episode {episode + 1}/{num_episodes}")

    print(f"Simulation complete. Wins: {wins}")

if __name__ == "__main__":
    main()
