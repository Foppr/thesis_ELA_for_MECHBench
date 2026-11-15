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
            fractal = 0.15 * np.sin(12.0 * x[i]) * np.cos(8.0 * x[i]) * np.sin(4.0 * x[i])
            # Add chaotic modulation
            chaotic = 0.05 * np.sin(15.0 * x[i]) * np.cos(10.0 * x[i])
            result += base + fractal + chaotic + 0.25 * x[i]**2 + 0.04 * x[i]**3
            
        # Add interaction terms between dimensions with chaotic coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Add chaotic interaction terms
                interaction = 0.05 * np.sin(1.8 * x[i]) * np.sin(1.1 * x[j]) 
                interaction += 0.03 * np.cos(2.3 * x[i]) * np.sin(1.6 * x[j])
                interaction += 0.02 * x[i] * x[j]
                # Add fractal-like coupling
                fractal_coupling = 0.01 * np.sin(6.0 * x[i] + 2.5 * x[j]) * np.cos(4.0 * x[i] - 1.5 * x[j])
                result += interaction + fractal_coupling
                
        # Add a global scaling factor with additional polynomial terms and chaotic modulation
        sum_x2 = np.sum(x**2)
        sum_x4 = np.sum(x**4)
        sum_x6 = np.sum(x**6)
        
        # Add chaotic scaling factor with hybrid mechanism
        chaotic_scale = 1.0 + 0.3 * sum_x2 + 0.1 * sum_x4 + 0.05 * sum_x6
        chaotic_scale += 0.1 * np.sin(10.0 * sum_x2) * np.cos(6.0 * sum_x4)
        # Add fractal scaling component
        fractal_scale = 1.0 + 0.08 * np.sin(18.0 * sum_x2) * np.cos(12.0 * sum_x4)
        chaotic_scale = chaotic_scale * fractal_scale
        
        result = result * chaotic_scale
        
        # Add a small noise term to increase landscape complexity
        noise = 0.002 * np.sum(np.sin(120.0 * x))
        result += noise
        
        # Add a novel hybrid fractal component
        fractal_component = 0.005 * np.sum(np.sin(20.0 * x) * np.cos(15.0 * x) * np.sin(10.0 * x))
        result += fractal_component
        
        return result