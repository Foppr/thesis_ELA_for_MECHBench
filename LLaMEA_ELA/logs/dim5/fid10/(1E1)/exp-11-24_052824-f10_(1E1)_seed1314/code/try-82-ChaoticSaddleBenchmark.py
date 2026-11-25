import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        quadratic = np.sum(x**2)
        
        # Enhanced nested polynomial terms with higher-order interactions
        poly_nested = 0
        for i in range(self.dim):
            poly_nested += (x[i]**7 + 4*x[i]**5 + 6*x[i]**3 + 2*x[i]) * np.sin(0.6 * x[i])
            
        # Sinusoidal component with chaotic phase modulation and amplitude variation
        sinusoidal = 0
        for i in range(self.dim):
            phase = np.sin(x[i]) + 0.4 * np.sin(3 * x[i]) + 0.2 * np.sin(7 * x[i]) + 0.1 * np.sin(11 * x[i])
            amplitude = 1.0 + 0.3 * np.sin(0.5 * x[i])
            sinusoidal += amplitude * np.cos(phase * x[i]) * np.exp(-0.12 * x[i]**2)
            
        # Chaotic interaction between dimensions using coupled sine waves
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling
                chaotic_interaction += np.sin(x[i] * x[j]) * np.cos(0.4 * (x[i]**2 + x[j]**2)) * np.exp(-0.05 * (x[i] - x[j])**2)
                
        # Saddle-point component with multi-scale exponential decay
        saddle = 0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1) * np.exp(-0.4 * x[i]**2) + 0.5 * (x[i]**4 - 1) * np.exp(-0.2 * x[i]**2)
            
        # High-order polynomial coupling with dynamic sinusoidal modulation
        high_order = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_factor = 1 + 0.2 * np.sin(0.3 * x[i] * x[j])
                high_order += (x[i]**4 + x[j]**4) * np.sin(0.25 * x[i] * x[j]) * coupling_factor
                
        # Component that introduces multiple local minima with varying depths and locations
        local_minima = 0
        for i in range(self.dim):
            local_minima += (np.sin(6 * x[i]) * np.cos(3 * x[i]) + 0.7 * np.sin(12 * x[i])) * np.exp(-0.1 * x[i]**2)
            
        # Additional chaotic component with fractal-like behavior
        fractal = 0
        for i in range(self.dim):
            fractal += np.sin(2 * x[i]) * np.cos(4 * x[i]) * np.sin(8 * x[i]) * (1 + 0.3 * np.cos(x[i]))
            
        # Combine all components with carefully tuned weights to create a challenging landscape
        return (0.25 * quadratic + 
                0.35 * poly_nested + 
                0.2 * sinusoidal + 
                0.18 * chaotic_interaction + 
                0.22 * saddle + 
                0.28 * high_order + 
                0.12 * local_minima + 
                0.15 * fractal + 
                4.5 * np.sum(np.sin(x)**4))