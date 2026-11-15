import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different scales
        self.scales = np.array([1.0, 0.5, 0.25, 0.125])
        self.amplitudes = np.array([1.0, 0.5, 0.25, 0.125])
    
    def f(self, x):
        # Normalize to [-1, 1]
        x_norm = x / 5.0
        
        # Initialize result
        result = 0.0
        
        # Fractal structure with multiple scales
        for scale, amp in zip(self.scales, self.amplitudes):
            # Create fractal pattern using sine waves at different frequencies
            fractal_term = np.sum(
                amp * np.sin(scale * 20 * np.pi * x_norm) * 
                np.cos(scale * 15 * np.pi * x_norm) *
                np.sin(scale * 10 * np.pi * x_norm) *
                np.cos(scale * 5 * np.pi * x_norm)
            )
            
            # Add radial component for hierarchical structure
            radial_component = amp * np.sum(
                np.sin(scale * 30 * np.pi * np.linalg.norm(x_norm)) * 
                np.cos(scale * 25 * np.pi * np.linalg.norm(x_norm))
            )
            
            result += fractal_term + radial_component
        
        # Add a global minimum at the center with increasing complexity
        center_penalty = np.sum(x_norm**2) * 0.1
        
        # Add a chaotic component for additional difficulty
        chaotic_component = np.sum(
            np.sin(50 * np.pi * x_norm**3) * 
            np.cos(30 * np.pi * x_norm**3) *
            np.exp(-np.sum(x_norm**2) / 2)
        )
        
        return result + center_penalty + 0.5 * chaotic_component