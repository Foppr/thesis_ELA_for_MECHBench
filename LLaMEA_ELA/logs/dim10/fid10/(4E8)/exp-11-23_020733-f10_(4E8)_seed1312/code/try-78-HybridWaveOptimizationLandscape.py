import numpy as np

class HybridWaveOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Separable quadratic base
        result = 0.5 * np.sum(x**2)
        
        # Add periodic wave components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 0.5 * np.sin(i * 0.7)
            amp = 1.0 + 0.3 * np.cos(i * 0.9)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Add multi-modal sine-cosine interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                result += 0.2 * np.sin(x[i]) * np.cos(x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Incorporate asymmetric saddle points with varying steepness
        for i in range(self.dim):
            result += 0.1 * x[i]**3 + 0.05 * x[i]**4 + 0.02 * np.sin(5 * x[i]) * np.cos(3 * x[i])
        
        # Add cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
                result += 0.15 * coupling
        
        # Introduce a fractal-like noise component using sine series
        noise = 0.03 * np.sum(np.sin(10 * x) + np.cos(7 * x) + np.tan(4 * x))
        result += noise
        
        # Apply global scaling factor to control difficulty
        result *= 1.15
        
        return result