import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Nested polynomial terms with varying degrees (slightly modified weights)
        poly_nested = 0
        for i in range(self.dim):
            poly_nested += (x[i]**6 + 2.5*x[i]**4 + 4*x[i]**2) * np.sin(0.6 * x[i])
            
        # Sinusoidal component with chaotic phase modulation (modified frequencies)
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3.5 * x[i]) + 0.15 * np.sin(6.5 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.12 * x[i]**2)
            
        # Chaotic interaction between dimensions using logistic map-like behavior (modified coupling)
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i]**2 + x[j]**2))
                
        # Saddle-point component with exponential decay (modified coefficients)
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1.2) * np.exp(-0.4 * x[i]**2)
            
        # High-order polynomial coupling with sinusoidal modulation (changed interaction)
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**3 + x[j]**3) * np.sin(0.25 * x[i] * x[j]) * (1 + 0.15 * np.cos(x[i] + x[j]))
                
        # Add a component that introduces multiple local minima with varying depths
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(4.5 * x[i]) * np.cos(2.2 * x[i]) + 0.4 * np.sin(9.5 * x[i])
            
        # Combine all components with carefully tuned weights to create a challenging landscape
        return (0.25 * quadratic + 
                0.45 * poly_nested + 
                0.18 * sinusoidal + 
                0.18 * chaotic_interaction + 
                0.22 * saddle + 
                0.32 * high_order + 
                0.08 * local_minima + 
                5.5 * np.sum(np.sin(x)**3))