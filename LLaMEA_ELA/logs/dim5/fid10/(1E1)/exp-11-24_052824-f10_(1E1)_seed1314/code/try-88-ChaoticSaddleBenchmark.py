import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Nested polynomial terms with varying degrees and chaotic modulation
        poly_nested = 0
        for i in range(self.dim):
            poly_nested += (x[i]**7 + 4*x[i]**5 + 6*x[i]**3 + 2*x[i]) * np.sin(0.7 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Sinusoidal component with chaotic phase modulation and exponential decay
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.2 * x[i]**2)
            
        # Chaotic interaction between dimensions using logistic map-like behavior with higher coupling
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(max(0, i-3), min(i+5, self.dim)):  # Extended coupling
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i]**2 + x[j]**2)) * np.exp(-0.1 * abs(x[i] - x[j]))
                
        # Saddle-point component with exponential decay and higher-order terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 2*x[i]**2) * np.exp(-0.3 * x[i]**2)
            
        # High-order polynomial coupling with sinusoidal modulation and additional chaotic perturbation
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.3 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Add a component that introduces multiple local minima with varying depths and chaotic positioning
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(7 * x[i]) * np.cos(3 * x[i]) + 0.7 * np.sin(14 * x[i]) + 0.3 * np.sin(21 * x[i])
            
        # Exponential barrier component to increase conditioning difficulty
        barriers = 0
        for i in range(self.dim):
            barriers += np.exp(2 * np.abs(x[i])) * np.sin(0.5 * x[i])**2
            
        # Cross-dimensional chaotic coupling with non-linear interaction
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += np.sin(0.5 * (x[i]**2 + x[j]**2)) * np.cos(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Combine all components with carefully tuned weights to create a challenging landscape
        return (0.25 * quadratic + 
                0.35 * poly_nested + 
                0.15 * sinusoidal + 
                0.2 * chaotic_interaction + 
                0.2 * saddle + 
                0.25 * high_order + 
                0.1 * local_minima + 
                0.15 * barriers + 
                0.1 * cross_coupling + 
                3 * np.sum(np.sin(x)**4))