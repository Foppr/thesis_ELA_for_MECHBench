import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Nested polynomial terms with varying degrees
        poly_nested = 0
        for i in range(self.dim):
            poly_nested += (x[i]**6 + 3*x[i]**4 + 5*x[i]**2) * np.sin(0.5 * x[i])
            
        # Sinusoidal component with chaotic phase modulation
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.3 * np.sin(3 * x[i]) + 0.1 * np.sin(7 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Chaotic interaction between dimensions using logistic map-like behavior (mutated)
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Slightly increased coupling range
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))  # Slight frequency increase
                
        # Saddle-point component with exponential decay
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.5 * x[i]**2)
            
        # High-order polynomial coupling with sinusoidal modulation (mutated)
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**3 + x[j]**3) * np.sin(0.35 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j]))  # Increased modulation
                
        # Add a component that introduces multiple local minima with varying depths (mutated)
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(6 * x[i]) * np.cos(2.5 * x[i]) + 0.7 * np.sin(12 * x[i])  # Increased amplitude
            
        # Add a new term with higher frequency oscillations to increase gradient complexity
        high_freq = 0
        for i in range(self.dim):
            high_freq += np.sin(15 * x[i]) * np.cos(8 * x[i]) + 0.5 * np.sin(25 * x[i])
            
        # Combine all components with carefully tuned weights to create a challenging landscape
        return (0.3 * quadratic + 
                0.4 * poly_nested + 
                0.2 * sinusoidal + 
                0.15 * chaotic_interaction + 
                0.25 * saddle + 
                0.3 * high_order + 
                0.12 * local_minima + 
                0.1 * high_freq + 
                5 * np.sum(np.sin(x)**4))