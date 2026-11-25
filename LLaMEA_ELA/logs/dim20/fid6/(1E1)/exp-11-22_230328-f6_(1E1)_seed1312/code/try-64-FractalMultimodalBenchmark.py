import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters for different scales
        self.scales = np.logspace(0, 2, 5)  # 5 scales from 1 to 100
        self.amplitudes = np.logspace(0, 3, 5)  # Amplitudes for each scale
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Initialize function value
        result = 0.0
        
        # Add fractal components at multiple scales
        for i, (scale, amp) in enumerate(zip(self.scales, self.amplitudes)):
            # Create fractal pattern with sine and cosine terms
            pattern = np.sin(scale * x_norm) * np.cos(scale * x_norm)
            
            # Add hierarchical structure with different exponents
            fractal_term = amp * (np.abs(pattern)**(1.5 + i*0.2)) * np.exp(-0.5 * np.sum(x_norm**2))
            
            # Add interaction between dimensions
            interaction = 0.0
            for j in range(self.dim - 1):
                interaction += np.sin(2 * scale * (x_norm[j] + x_norm[j+1])) * \
                              np.cos(3 * scale * (x_norm[j] - x_norm[j+1]))
            
            result += fractal_term + 0.1 * interaction
        
        # Add global multimodal structure
        global_structure = np.sum(np.sin(20 * x_norm) * np.cos(15 * x_norm))
        
        # Add basin-like regions with varying depths
        basin_terms = 0.0
        for i in range(self.dim):
            basin_terms += (x_norm[i]**4 - 2 * x_norm[i]**2 + 0.5)**2
        
        return result + global_structure + 0.3 * basin_terms