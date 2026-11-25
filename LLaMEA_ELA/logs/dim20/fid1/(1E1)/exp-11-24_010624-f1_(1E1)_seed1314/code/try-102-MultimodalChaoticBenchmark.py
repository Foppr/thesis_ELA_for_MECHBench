import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive conditioning parameters
        self.conditioning = np.array([1.0 + 0.5 * np.sin(i * 0.5) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Exponential decay component with adaptive conditioning
        for i in range(self.dim):
            result += self.conditioning[i] * np.exp(-0.1 * x[i]**2) * np.cos(2 * np.pi * x[i])
            
        # Trigonometric coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                coupling = np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i] + x[j]))
                result += 0.2 * coupling * np.exp(-0.05 * (i - j)**2)
                
        # Adaptive polynomial terms with frequency modulation
        for i in range(self.dim):
            poly_term = 0.1 * x[i]**4 * np.sin(3 * x[i]) * np.exp(-0.02 * np.abs(x[i]))
            result += poly_term
            
        # Saddle point structure using hyperbolic functions
        for i in range(self.dim):
            saddle_term = 0.05 * (np.cosh(x[i]) - 1) * np.sin(0.3 * x[i])
            result += saddle_term
            
        # Global distortion with radial symmetry
        dist_from_origin = np.sqrt(np.sum(x**2))
        distortion = 0.1 * np.sin(0.4 * dist_from_origin) * np.cos(0.6 * dist_from_origin)
        result *= (1 + distortion)
        
        # Add noise for increased irregularity
        noise = 0.005 * np.sum(np.sin(x * 20))
        result += noise
        
        return result