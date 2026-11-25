import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with chaotic sine modulations and Gaussian decay
        multimodal = 0
        for i in range(self.dim):
            freq1 = 6 * (i + 1) / self.dim
            freq2 = 3.0 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 8 + 0.7 * np.exp(-0.5 * (x[i] / 1.5)**2) * np.cos(freq2 * np.pi * x[i]) ** 6
        
        # Enhanced polynomial interaction terms with higher-order cross-terms and chaotic coupling
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.12 * (x[i] ** 4) * (x[j] ** 6) * np.sin(0.5 * np.pi * x[i] * x[j])
        
        # Adaptive scaling based on dimensionality with chaotic factor
        scale_factor = 1.0 + 0.3 * np.log(self.dim + 1) + 0.05 * np.sin(0.2 * self.dim)
        
        # Global shift with dynamic component to increase landscape complexity
        shift = 0.8 * np.sum(np.abs(x)) + 0.1 * np.sum(np.sin(0.3 * x))
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.2 * multimodal + 0.05 * polynomial) + shift