import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Nested polynomial terms with varying degrees and chaotic modulations
        poly_nested = 0
        for i in range(self.dim):
            poly_nested += (x[i]**7 + 4*x[i]**5 + 6*x[i]**3 + 2*x[i]) * np.sin(0.7 * x[i]) * np.cos(0.3 * x[i]**2)
            
        # Enhanced sinusoidal component with multiple phase modulations
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.15 * x[i]**2) * (1 + 0.3 * np.sin(5 * x[i]))
            
        # Stronger chaotic interaction between dimensions using modified logistic map behavior
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.6 * (x[i]**2 + x[j]**2)) * np.exp(-0.2 * abs(x[i] - x[j]))
                
        # Enhanced saddle-point component with higher-order terms
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**4 - 2*x[i]**2 + 1) * np.exp(-0.3 * x[i]**2)
            
        # High-order polynomial coupling with complex sinusoidal modulation
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.5 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Novel local minima component with fractal-like structure
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(8 * x[i]) * np.cos(3 * x[i]) + 0.7 * np.sin(15 * x[i]) + 0.3 * np.sin(25 * x[i])
            
        # Additional chaotic cross-term with exponential decay
        cross_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(0.8 * x[i]) * np.cos(0.6 * x[j]) * np.exp(-0.25 * (x[i]**2 + x[j]**2)) * (1 + 0.2 * np.sin(x[i] + x[j]))
                
        # Combine all components with carefully tuned weights to create a challenging landscape
        return (0.25 * quadratic + 
                0.35 * poly_nested + 
                0.2 * sinusoidal + 
                0.18 * chaotic_interaction + 
                0.28 * saddle + 
                0.35 * high_order + 
                0.15 * local_minima + 
                0.12 * cross_term + 
                6 * np.sum(np.sin(x)**5))  # Changed to sin^5 for even sharper minima