import dotenv
dotenv.load_dotenv()

import os
n = 0
graph = []
q = []
R = []

def init():
    global graph, n
    graph = [
        [0, 1, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0]
    ]

    with open("input.in", "r") as f:
        n = int(f.readline())
        graph = []
        for i in range(n):
            graph.append(list(map(int, f.readline().split())))

    global q, R
    q = [[0 for i in range(len(graph))] for j in range(len(graph))]
    R = [-1 for i in range(len(graph))]
    R[n - 1] = 100

import random
def train(epochs=1000, alpha=0.8, gamma=0.8):
    global q, R


    for i in range(epochs):
        current_state = random.randint(0, n - 1)
        possible_actions = []
        for j in range(len(graph)):
            if graph[current_state][j] == 1:
                possible_actions.append(j)
        next_state = random.choice(possible_actions) #  randomly select a next state/action
        possible_next_actions = []
        for j in range(len(graph)):
            if graph[next_state][j] == 1:
                possible_next_actions.append(j)
        next_next_state = random.choice(possible_next_actions)  # randomly select a next next state/action
        q[current_state][next_state] = (1 - alpha) * q[current_state][next_state] + alpha * (R[next_state] + gamma * max(q[next_state]))
        next_state = next_next_state

def argmax(arr):
    max_val = max(arr)
    for i in range(len(arr)):
        if arr[i] == max_val:
            return i
    return -1
def test():
    global q
    print("node  : ", end="")
    for i in  range(len(q)):
        print(i + 1, end=" ")
    print()
    print("action: ", end="")
    for i in range(len(q)):
        print(argmax(q[i]) + 1, end=" ")
    print()
    print("Q matrix: i = 4")
    print(q[3])

m  = 0
s = 0

def main():
    init()
    train() # start q-learning
    test()  # test the effectiveness of the model

if __name__ == "__main__":
    main()