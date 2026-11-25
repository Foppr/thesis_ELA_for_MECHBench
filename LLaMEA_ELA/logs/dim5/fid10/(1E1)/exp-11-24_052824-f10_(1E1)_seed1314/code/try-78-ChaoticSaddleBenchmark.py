import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced nested polynomial terms with higher degree interactions
        poly_nested = 0
        for i in range(self.dim):
            poly_nested += (x[i]**8 + 4*x[i]**6 + 7*x[i]**4 + 5*x[i]**2) * np.sin(0.3 * x[i])
            
        # Sinusoidal component with chaotic phase modulation and additional harmonics
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.15 * x[i]**2)
            
        # Chaotic interaction between dimensions using enhanced coupling
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Saddle-point component with enhanced exponential decay and nonlinearity
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1)**3 * np.exp(-0.3 * x[i]**2)
            
        # High-order polynomial coupling with stronger sinusoidal modulation
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.3 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Component that introduces multiple local minima with varying depths and better separation
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(6 * x[i]) * np.cos(3 * x[i]) + 0.7 * np.sin(12 * x[i]) + 0.3 * np.sin(18 * x[i])
            
        # Additional chaotic component with exponential scaling
        chaotic_scaling = 0
        for i in range(self.dim):
            chaotic_scaling += np.exp(-0.5 * x[i]**2) * np.sin(2 * x[i]) * np.cos(0.5 * x[i])
            
        # Combine all components with adjusted weights to create a more challenging landscape
        return (0.25 * quadratic + 
                0.45 * poly_nested + 
                0.15 * sinusoidal + 
                0.2 * chaotic_interaction + 
                0.3 * saddle + 
                0.35 * high_order + 
                0.15 * local_minima + 
                0.2 * chaotic_scaling + 
                6 * np.sum(np.sin(x)**4))