import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Enhanced polynomial terms with varying degrees and conditioning
        for i in range(self.dim):
            result += 0.8 * x[i]**4 - 3.0 * x[i]**3 + 2.0 * x[i]**2 - 0.5 * x[i]
            
        # Stronger sinusoidal coupling between dimensions with varying frequencies
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # More localized coupling
                freq_i = 2.0 + 0.5 * i
                freq_j = 1.5 + 0.3 * j
                result += 0.5 * np.sin(freq_i * np.pi * x[i]) * np.cos(freq_j * np.pi * x[j])
                
        # Enhanced radial basis function component with multiple centers
        centers = np.linspace(-3.0, 3.0, self.dim)
        for i in range(self.dim):
            result += 0.3 * np.exp(-0.2 * (x[i] - centers[i])**2)
            
        # Additional high-frequency oscillation with variable amplitude
        for i in range(self.dim):
            amp = 0.2 + 0.1 * np.sin(i)
            result += amp * np.sin(15 * x[i]) * np.cos(7 * x[i])
            
        # Global minimum modification with stronger penalty
        result += 0.1 * np.sum(x**2)
        
        # Add a small noise term to increase robustness
        result += 0.01 * np.random.rand()
        
        return result