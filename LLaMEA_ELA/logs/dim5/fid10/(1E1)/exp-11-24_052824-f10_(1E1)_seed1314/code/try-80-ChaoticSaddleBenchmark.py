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
            poly_nested += (x[i]**7 + 2*x[i]**5 + 4*x[i]**3) * np.sin(0.7 * x[i])
            
        # Sinusoidal component with chaotic phase modulation
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(4 * x[i]) + 0.15 * np.sin(6 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.12 * x[i]**2)
            
        # Chaotic interaction between dimensions using logistic map-like behavior
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced coupling
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i]**2 + x[j]**2))
                
        # Saddle-point component with exponential decay
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.6 * x[i]**2)
            
        # High-order polynomial coupling with sinusoidal modulation
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.3 * x[i] * x[j]) * (1 + 0.15 * np.cos(x[i] + x[j]))
                
        # Add a component that introduces multiple local minima with varying depths
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(6 * x[i]) * np.cos(2.5 * x[i]) + 0.6 * np.sin(11 * x[i])
            
        # Combine all components with carefully tuned weights to create a challenging landscape
        return (0.25 * quadratic + 
                0.45 * poly_nested + 
                0.18 * sinusoidal + 
                0.18 * chaotic_interaction + 
                0.22 * saddle + 
                0.35 * high_order + 
                0.12 * local_minima + 
                4.5 * np.sum(np.sin(x)**4))