import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms (central valley)
        f1 = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with exponentially decaying amplitudes and increasing frequencies
        f2 = np.sum(np.exp(-1.5 * np.abs(x_norm)) * (np.sin(7.0 * np.pi * x_norm))**3)
        
        # Product of cosine terms with varying frequencies and amplitudes
        f3 = np.prod(np.cos(3.0 * np.pi * x_norm) * np.exp(-0.3 * x_norm**2))
        
        # Additional high-frequency multimodal component with varying amplitude
        f4 = np.sum(np.sin(12.0 * np.pi * x_norm) * np.cos(10.0 * np.pi * x_norm) * np.exp(-0.5 * np.abs(x_norm)))
        
        # Combined with a shifted quadratic term to create a more complex global minimum
        shift = 0.03 * np.sum((x_norm - 0.2)**2)
        
        # Add a conditioning factor to increase the condition number
        condition_factor = 1.0 + 0.5 * np.sum(np.abs(x_norm)**3)
        
        # Combine all terms with optimized weights
        result = 0.25 * f1 + 0.35 * f2 + 0.25 * f3 + 0.15 * f4 + shift
        
        # Apply conditioning factor
        result = result * condition_factor
        
        return result