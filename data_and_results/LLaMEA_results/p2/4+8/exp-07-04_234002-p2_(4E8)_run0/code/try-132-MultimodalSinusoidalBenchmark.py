import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with enhanced sinusoidal components
        result = 0.0
        
        # Main sinusoidal contribution with nested frequencies, cubic, quintic, and septic terms
        for i in range(self.dim):
            result += 1.5 * np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) + 0.4 * x[i]**3 + 0.08 * x[i]**5 + 0.01 * x[i]**7
            
        # Add complex interaction terms between dimensions with nested coupling and cross-dimensional chaos
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(3.0 * x[i]) * np.sin(2.5 * x[j]) + 0.05 * x[i] * x[j] + 0.03 * np.sin(4.0 * x[i] + 1.5 * x[j]) + 0.01 * np.sin(2.0 * x[i]**2 + 1.0 * x[j]**2)
                
        # Add a global scaling factor with adaptive polynomial terms and a dynamic logarithmic component
        adaptive_log = np.log(1.0 + 0.2 * np.sum(x**2) + 0.05 * np.sum(x**4))
        result = result * (1.0 + 0.4 * np.sum(x**2) + 0.15 * np.sum(x**4) + 0.08 * np.sum(x**6) + 0.03 * np.sum(x**8) + 0.01 * np.sum(x**10) + 0.03 * adaptive_log)
        
        # Add nested chaotic perturbations using a fractal-like structure with multiple frequencies and dynamic modulation
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor += 0.05 * np.sin(20.0 * x[i]) * np.cos(17.0 * x[i]) + 0.025 * np.sin(35.0 * x[i]) + 0.015 * np.sin(40.0 * x[i]**2) + 0.01 * np.sin(50.0 * x[i]**3)
            
        # Add adaptive scaling based on coordinate magnitude
        adaptive_scale = 1.0 + 0.02 * np.sum(np.abs(x)**1.5)
        result = result * chaotic_factor * adaptive_scale
        
        return result