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
            phase = np.sin(x[i]) + 0.4 * np.sin(4 * x[i]) + 0.15 * np.sin(8 * x[i])
            sinusoidal += np.cos(phase * x[i]) * np.exp(-0.12 * x[i]**2)
            
        # Chaotic interaction between dimensions using logistic map-like behavior with stronger coupling
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(max(0, i-2), min(i+3, self.dim)):  # Broader coupling range
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * abs(x[i] - x[j]))
                
        # Saddle-point component with modified exponential decay and additional sinusoidal modulation
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.4 * x[i]**2) * np.sin(0.8 * x[i])
            
        # High-order polynomial coupling with enhanced sinusoidal modulation and additional interaction terms
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.4 * x[i] * x[j]) * (1 + 0.2 * np.cos(x[i] + x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Component that introduces multiple local minima with varying depths and sharper gradients
        local_minima = 0
        for i in range(self.dim):
            local_minima += np.sin(7 * x[i]) * np.cos(3 * x[i]) + 0.7 * np.sin(14 * x[i]) + 0.3 * np.sin(21 * x[i])
            
        # Additional chaotic component with multiple sine waves for increased landscape complexity
        chaotic_component = 0
        for i in range(self.dim):
            chaotic_component += np.sin(5 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.2 * x[i]**2)
            
        # Combine all components with modified weights to create a more challenging landscape
        return (0.25 * quadratic + 
                0.35 * poly_nested + 
                0.18 * sinusoidal + 
                0.12 * chaotic_interaction + 
                0.22 * saddle + 
                0.28 * high_order + 
                0.08 * local_minima + 
                0.05 * chaotic_component +
                4.5 * np.sum(np.sin(x)**5))  # Changed to sin^5 for even sharper minima