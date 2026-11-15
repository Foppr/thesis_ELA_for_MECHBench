import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with sinusoidal components
        result = 0.0
        
        # Main sinusoidal contribution with modified frequencies and chaotic perturbations
        for i in range(self.dim):
            # Base sinusoidal term with chaotic modulation
            base = 0.8 * np.sin(1.5 * x[i]) * np.cos(0.7 * x[i])
            # Add fractal-like perturbation
            fractal = 0.12 * np.sin(9.0 * x[i]) * np.cos(6.0 * x[i]) * np.sin(2.5 * x[i])
            result += base + fractal + 0.25 * x[i]**2 + 0.04 * x[i]**3
            
        # Add interaction terms between dimensions with chaotic coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add chaotic interaction terms
                interaction = 0.05 * np.sin(1.7 * x[i]) * np.sin(1.0 * x[j]) 
                interaction += 0.025 * np.cos(2.2 * x[i]) * np.sin(1.5 * x[j])
                interaction += 0.02 * x[i] * x[j]
                # Add fractal-like coupling
                fractal_coupling = 0.006 * np.sin(4.5 * x[i] + 1.8 * x[j]) * np.cos(2.8 * x[i] - 0.9 * x[j])
                result += interaction + fractal_coupling
                
        # Add a global scaling factor with additional polynomial terms and chaotic modulation
        sum_x2 = np.sum(x**2)
        sum_x4 = np.sum(x**4)
        sum_x6 = np.sum(x**6)
        
        # Add chaotic scaling factor
        chaotic_scale = 1.0 + 0.22 * sum_x2 + 0.08 * sum_x4 + 0.025 * sum_x6
        chaotic_scale += 0.06 * np.sin(7.5 * sum_x2) * np.cos(4.5 * sum_x4)
        
        result = result * chaotic_scale
        
        # Add a small noise term to increase landscape complexity
        noise = 0.0015 * np.sum(np.sin(95.0 * x))
        result += noise
        
        return result