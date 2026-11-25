import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Quadratic basin term - global minimum at origin
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal grid terms with chaotic interaction
        grid_terms = 0
        for i in range(self.dim):
            # Chaotic sine-wave pattern with varying amplitudes and frequencies
            grid_terms += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.sin(0.7 * x[i])
            
        # Radial component - increases complexity away from origin
        radial = 0.05 * np.sum(x**4)
        
        # Asymmetric cross-terms that create skewed landscape
        asymmetric = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Asymmetric interaction based on dimension index
                asym_factor = (i + 1) / (j + 1)
                asymmetric += asym_factor * x[i]**2 * x[j] * np.sin(0.3 * x[i] + 0.2 * x[j])
                
        # Add noise-like perturbation for additional challenge
        noise = 0.02 * np.sum(np.sin(3.0 * x) * np.cos(2.0 * x))
        
        return basin + grid_terms + radial + asymmetric + noise