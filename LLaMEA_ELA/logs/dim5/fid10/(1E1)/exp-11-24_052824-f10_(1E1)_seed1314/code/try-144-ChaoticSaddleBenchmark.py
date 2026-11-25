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
            
        # Sinusoidal component with chaotic phase modulation and multi-scale frequencies
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.05 * x[i]**2) * (1 + 0.3 * np.sin(2 * x[i]))
            
        # Chaotic interaction between dimensions using modified logistic map behavior with higher sensitivity
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Increased coupling range
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.6 * (x[i]**2 + x[j]**2)) * np.exp(-0.02 * abs(x[i] - x[j]))
                
        # Saddle-point component with multi-scale exponential decay and polynomial modification
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.3 * x[i]**2) * (1 + 0.2 * np.sin(3 * x[i]))
            
        # High-order polynomial coupling with sinusoidal modulation and additional chaos
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.4 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j])) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Component introducing multiple local minima with varying depths and chaotic positioning
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(8 * x[i]) * np.cos(3 * x[i]) + 0.8 * np.sin(16 * x[i]) + 0.4 * np.sin(24 * x[i])
            
        # Novel hybrid chaotic component with fractal-like behavior
        fractal_component = 0
        for i in range(self.dim):
            fractal_component += np.sin(5 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.2 * x[i]**2) + \
                                0.5 * np.sin(10 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add a component that introduces sharp ridges and valleys through hyperbolic tangent modulation
        ridge_valley = 0
        for i in range(self.dim):
            ridge_valley += np.tanh(3 * x[i]) * np.sin(2 * x[i]) + 0.3 * np.tanh(6 * x[i]) * np.cos(5 * x[i])
            
        # Combine all components with carefully tuned weights to create a challenging landscape
        return (0.25 * quadratic + 
                0.35 * poly_nested + 
                0.18 * sinusoidal + 
                0.12 * chaotic_interaction + 
                0.22 * saddle + 
                0.28 * high_order + 
                0.1 * local_minima + 
                0.08 * fractal_component + 
                0.15 * ridge_valley + 
                7 * np.sum(np.sin(x)**5))  # Changed to sin^5 for even sharper minima