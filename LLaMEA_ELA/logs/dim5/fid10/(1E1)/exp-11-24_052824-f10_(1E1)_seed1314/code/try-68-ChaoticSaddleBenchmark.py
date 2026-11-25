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
            poly_nested += (x[i]**7 + 4*x[i]**5 + 6*x[i]**3 + 2*x[i]) * np.sin(0.7 * x[i] + 0.3 * np.sin(5 * x[i]))
            
        # Sinusoidal component with chaotic phase modulation and multi-scale frequency
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.15 * x[i]**2) * (1 + 0.2 * np.sin(2 * x[i]))
            
        # Chaotic interaction between dimensions using logistic map-like behavior with time-delay
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * abs(x[i] - x[j]))
                
        # Saddle-point component with exponential decay and periodic modulation
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.6 * x[i]**2) * np.sin(0.5 * x[i])
            
        # High-order polynomial coupling with sinusoidal modulation and chaotic phase
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.3 * x[i] * x[j]) * (1 + 0.15 * np.cos(x[i] + x[j] + 0.2 * np.sin(x[i] * x[j])))
                
        # Component that introduces multiple local minima with varying depths and chaotic positioning
        local_minima = 0
        for i in range(self.dim):
            local_minima += (np.sin(6 * x[i]) * np.cos(3 * x[i]) + 0.6 * np.sin(12 * x[i])) * np.exp(-0.2 * x[i]**2)
            
        # Additional chaotic modulation with fractal-like behavior
        fractal_modulation = 0
        for i in range(self.dim):
            fractal_modulation += np.sin(8 * x[i]) * np.cos(4 * x[i]) * np.exp(-0.1 * x[i]**2) + 0.3 * np.sin(16 * x[i])
            
        # Combine all components with carefully tuned weights to create a challenging landscape
        return (0.25 * quadratic + 
                0.35 * poly_nested + 
                0.2 * sinusoidal + 
                0.18 * chaotic_interaction + 
                0.22 * saddle + 
                0.28 * high_order + 
                0.12 * local_minima + 
                0.15 * fractal_modulation + 
                7 * np.sum(np.sin(x)**4))