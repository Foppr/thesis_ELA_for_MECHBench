import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Nested polynomial terms with varying degrees and enhanced nonlinearity
        poly_nested = 0
        for i in range(self.dim):
            poly_nested += (x[i]**8 + 4*x[i]**6 + 7*x[i]**4 + 3*x[i]**2) * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i])
            
        # Sinusoidal component with chaotic phase modulation and additional harmonic
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.15 * x[i]**2) * (1 + 0.2 * np.sin(5 * x[i]))
            
        # Chaotic interaction between dimensions using enhanced logistic map-like behavior
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * abs(x[i] - x[j]))
                
        # Saddle-point component with enhanced exponential decay and additional sinusoidal modulation
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.6 * x[i]**2) * np.sin(2 * x[i])
            
        # High-order polynomial coupling with enhanced sinusoidal modulation and additional interaction terms
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.4 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Component that introduces multiple local minima with varying depths and complex structure
        local_minima = 0
        for i in range(self.dim):
            local_minima += (np.sin(7 * x[i]) * np.cos(3 * x[i]) + 0.7 * np.sin(14 * x[i]) + 0.3 * np.sin(21 * x[i])) * np.exp(-0.2 * x[i]**2)
            
        # Novel gradient modulation component with multiple frequency harmonics
        gradient_mod = 0
        for i in range(self.dim):
            gradient_mod += (np.sin(8 * x[i]) + 0.5 * np.sin(16 * x[i]) + 0.3 * np.sin(24 * x[i])) * np.cos(2 * x[i])**3
            
        # Combine all components with carefully tuned weights to create a challenging landscape
        return (0.25 * quadratic + 
                0.35 * poly_nested + 
                0.15 * sinusoidal + 
                0.2 * chaotic_interaction + 
                0.2 * saddle + 
                0.35 * high_order + 
                0.15 * local_minima + 
                0.1 * gradient_mod + 
                6 * np.sum(np.sin(x)**5))  # Changed to sin^5 for even sharper minima