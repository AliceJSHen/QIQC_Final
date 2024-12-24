# File: target_function.py

import numpy as np
import matplotlib.pyplot as plt

class TARGET_FUNCTION:
    @staticmethod
    def bimodal(num_qubits, mean1=0.28, std1=0.08, mean2=0.72, std2=0.08):
        # Calculate the size of the dataset
        num_states = 2**num_qubits

        mean1 = mean1 * num_states
        mean2 = mean2 * num_states
        std1 = std1 * num_states
        std2 = std2 * num_states

        # Generate data for the first mode
        probabilities = []
        for x in range(num_states):
            prob1 = (np.pi*std1) * np.exp(-0.5*((x-mean1)/std1)**2)
            prob2 = (np.pi*std2) * np.exp(-0.5*((x-mean2)/std2)**2)
            probabilities.append(prob1+prob2)

        
        # Normalize probabilities
        probabilities = np.array(probabilities)
        probabilities /= np.sum(probabilities)

        # Create target distribution as a dictionary
        target_distribution = {format(i, f'0{num_qubits}b'): prob for i, prob in enumerate(probabilities)}

        return target_distribution
    
    def gaussian(num_qubits):
        num_states = 2**num_qubits  # Total basis states
        mid_point = (num_states - 1) / 2  # Center the distribution
        
        # Map basis states to integers and calculate probabilities
        probabilities = []
        for i in range(num_states):
            x = i - mid_point  # Centered integer value
            prob = np.exp(-(x/4)**2 / 2)  # Gaussian probability
            probabilities.append(prob)
        
        # Normalize probabilities
        probabilities = np.array(probabilities)
        probabilities /= np.sum(probabilities)
        
        # Create target distribution as a dictionary
        target_distribution = {format(i, f'0{num_qubits}b'): prob for i, prob in enumerate(probabilities)}
        return target_distribution
    
    def triangular(num_qubits, critical_point=0.4):
        num_states = 2**num_qubits  # Total basis states
        critical_point = critical_point * num_states

        # Map basis states to integers and calculate probabilities
        probabilities = []
        for i in range(num_states):
            if i < critical_point:
                prob = i / critical_point
            else:
                prob = 1 - (i - critical_point) / (num_states - critical_point)
            if prob <= 0:
                prob = 0.0001
            probabilities.append(prob)
        
        # Normalize probabilities
        probabilities = np.array(probabilities)
        probabilities /= np.sum(probabilities)

        # Create target distribution as a dictionary
        target_distribution = {format(i, f'0{num_qubits}b'): prob for i, prob in enumerate(probabilities)}
        return target_distribution
    
    def sinusoidal(num_qubits):
        num_states = 2**num_qubits

        probabilities = []
        for i in range(num_states):
            prob = np.sin(2 * np.pi * i / num_states)**2
            if prob <= 0:
                prob = 0.00001
            probabilities.append(prob)
        
        # Normalize probabilities
        probabilities = np.array(probabilities)
        probabilities /= np.sum(probabilities)

        # Create target distribution as a dictionary
        target_distribution = {format(i, f'0{num_qubits}b'): prob for i, prob in enumerate(probabilities)}
        return target_distribution

    

        

