import numpy as np

class FractalSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add fractal sine waves with multiple frequencies and amplitudes
        for i in range(1, min(self.dim + 1, 10)):
            freq = 2 ** i
            amp = 1.0 / (i + 1)
            
            # Create self-similar structure using sine waves with frequency modulation
            sine_term = amp * np.sin(freq * x[i-1] * (1 + 0.1 * np.sin(0.5 * freq * x[i-1])))
            
            # Add fractal scaling factor based on dimension
            scale_factor = 1.0 + 0.2 * np.sin(self.dim * 0.3 * i)
            
            result += sine_term * scale_factor
            
            # Add interaction terms between dimensions for increased complexity
            if i < self.dim:
                interaction = 0.5 * np.sin(freq * (x[i-1] + x[i]) * 0.5) * np.cos(freq * (x[i-1] - x[i]) * 0.3)
                result += interaction * scale_factor
        
        # Add multi-scale chaotic modulation
        chaotic_mod = 0.0
        for k in range(1, 6):
            chaotic_mod += np.sin(2 ** k * np.sum(x) * 0.1) * (1.0 / (k + 1))
        
        # Add polynomial perturbation with varying exponents
        poly_pert = 0.0
        for i in range(self.dim):
            poly_pert += 0.3 * x[i]**6 - 1.2 * x[i]**4 + 1.5 * x[i]**2
        
        return result + chaotic_mod + poly_pert