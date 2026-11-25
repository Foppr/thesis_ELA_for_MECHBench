import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Nested polynomial terms with varying degrees and increased complexity
        poly_nested = 0
        for i in range(self.dim):
            poly_nested += (x[i]**7 + 4*x[i]**5 + 6*x[i]**3 + 2*x[i]) * np.sin(0.6 * x[i])
            
        # Sinusoidal component with chaotic phase modulation and increased frequency
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Chaotic interaction between dimensions using logistic map-like behavior (mutated with stronger coupling)
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * abs(x[i] - x[j]))
                
        # Saddle-point component with modified exponential decay and increased nonlinearity
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1)**3 * np.exp(-0.4 * x[i]**2)
            
        # High-order polynomial coupling with sinusoidal modulation (mutated with stronger interaction)
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.4 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j])) * np.exp(-0.1 * abs(x[i] - x[j]))
                
        # Add a component that introduces multiple local minima with varying depths and increased density
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(7 * x[i]) * np.cos(3 * x[i]) + 0.7 * np.sin(14 * x[i]) + 0.3 * np.sin(21 * x[i])
            
        # Add a new component with fractional powers to increase gradient complexity
        fractional = 0
        for i in range(self.dim):
            fractional += (np.abs(x[i])**1.7 + 0.5 * np.abs(x[i])**2.3) * np.cos(0.8 * x[i])
            
        # Combine all components with carefully tuned weights to create a challenging landscape
        return (0.25 * quadratic + 
                0.45 * poly_nested + 
                0.15 * sinusoidal + 
                0.2 * chaotic_interaction + 
                0.3 * saddle + 
                0.25 * high_order + 
                0.15 * local_minima + 
                0.1 * fractional + 
                6 * np.sum(np.sin(x)**5))  # Changed to sin^5 for sharper minima and increased complexity