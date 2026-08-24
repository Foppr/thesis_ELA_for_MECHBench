import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Base quadratic term with chaotic modulation
        for i in range(self.dim):
            # Add chaotic modulation to the quadratic term
            chaotic_mod = 0.1 * np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
            result += 0.5 * x[i]**2 + chaotic_mod
            
        # Add fractal-like high-order polynomial terms
        for i in range(self.dim):
            result += 0.05 * x[i]**4 + 0.02 * x[i]**6 + 0.01 * x[i]**8
            
        # Cross-dimensional coupling with chaotic interaction coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling with fractal-like structure
                coupling = 0.03 * np.sin(3.0 * x[i] + 2.0 * x[j]) * np.cos(2.0 * x[i] - x[j])
                coupling += 0.01 * np.sin(5.0 * x[i] * x[j]) * np.cos(4.0 * x[i] + x[j])
                result += coupling
                
        # Add chaotic scaling factor based on sum of powers
        sum_x2 = np.sum(x**2)
        sum_x4 = np.sum(x**4)
        sum_x6 = np.sum(x**6)
        
        # Fractal-like scaling with chaotic perturbations
        scale_factor = 1.0 + 0.1 * np.sin(5.0 * sum_x2) + 0.05 * np.cos(3.0 * sum_x4) + 0.02 * np.sin(7.0 * sum_x6)
        result = result * scale_factor
        
        # Add saddle-point dominance through sinusoidal perturbations
        for i in range(self.dim):
            result += 0.02 * np.sin(15.0 * x[i]) * np.cos(12.0 * x[i])
            
        # Add small noise to increase complexity
        noise = 0.005 * np.sum(np.sin(50.0 * x))
        result += noise
        
        return result