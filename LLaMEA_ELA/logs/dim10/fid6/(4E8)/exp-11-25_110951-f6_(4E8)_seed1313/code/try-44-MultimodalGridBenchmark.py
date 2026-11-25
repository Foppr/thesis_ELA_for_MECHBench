import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Fractal-like basin term with adaptive conditioning
        basin = 0.05 * np.sum(x**2) + 0.02 * np.sum(np.sin(1.5 * x)**2) + 0.01 * np.sum(np.cos(2.3 * x)**2)
        
        # Enhanced multimodal grid with chaotic interactions
        grid_terms = 0
        for i in range(self.dim):
            # Base periodic pattern with multiple local minima
            grid_terms += np.sin(0.8 * x[i]) * np.cos(0.5 * x[i])
            # Higher frequency components for increased complexity
            grid_terms += 0.4 * np.sin(4.0 * x[i]) * np.cos(3.0 * x[i])
            # Chaotic sine-cosine interaction with nonlinearity
            grid_terms += 0.25 * np.sin(6.2 * x[i]) * np.cos(1.9 * x[i]) * np.sin(0.7 * x[i]**2)
            # Adaptive scaling factors based on dimension
            scale_factor = 1.0 + 0.1 * np.sin(i * 0.5)
            grid_terms += 0.15 * scale_factor * np.sin(2.8 * x[i])**3 * np.cos(1.2 * x[i])
            
            # Cross-dimension coupling with fractal-like structure
            if i < self.dim - 1:
                grid_terms += 0.1 * np.sin(x[i] + 0.5 * x[i+1]) * np.cos(0.8 * x[i] - 0.3 * x[i+1])
            
            # Additional chaotic interactions with higher order terms
            if i < self.dim - 2:
                grid_terms += 0.08 * np.sin(x[i] + x[i+1] + 0.4 * x[i+2]) * np.cos(1.3 * x[i+2])
            
            # Fractal-like coupling with exponentially decaying influence
            if i < self.dim - 3:
                grid_terms += 0.05 * np.sin(x[i] * np.exp(-0.1 * i)) * np.cos(x[i+1] * np.exp(-0.05 * i))
        
        # Combine all terms with refined weights for enhanced difficulty
        return basin + grid_terms + 0.03 * np.sum(np.abs(x)) + 0.008 * np.sum(x**4) + 0.015 * np.sum(np.sin(x)**2)