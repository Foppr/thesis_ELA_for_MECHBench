import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Separable quadratic terms with varying condition numbers
        for i in range(self.dim):
            # Adaptive scaling based on dimension
            scale = 1.0 + 0.5 * np.sin(i * 0.7)
            result += 0.5 * scale * x[i]**2
        
        # Non-separable high-order interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling range
                # Chaotic interaction with sine modulation
                coupling = np.sin(3.0 * (x[i] + x[j]) + 0.5 * np.sin(7.0 * x[i]))
                result += 0.3 * (x[i]**3 + x[j]**3) * coupling
        
        # Asymmetric saddle-point terms with adaptive exponents
        for i in range(self.dim):
            # Asymmetric cubic term
            asymmetry = 1.0 + 0.3 * np.cos(i * 0.9)
            result += 0.2 * asymmetry * x[i]**3
        
        # Sine-wave modulated chaotic components
        for i in range(self.dim):
            # Multi-frequency sine modulation with chaotic phase
            phase = np.sin(2.0 * x[i]) + 0.5 * np.sin(5.0 * x[i]) + 0.2 * np.sin(13.0 * x[i])
            result += 0.4 * np.sin(3.0 * phase + 0.7 * np.cos(x[i])) * np.exp(-0.1 * x[i]**2)
        
        # Adaptive dimensionality scaling with fractal-like perturbations
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        result *= dim_factor
        
        # Add irregular perturbations with varying frequencies
        irregular = 0.0
        for i in range(self.dim):
            irregular += np.sin(15.0 * x[i]) * np.cos(8.0 * x[i]) * np.exp(-0.2 * x[i]**2)
        result += 0.15 * irregular
        
        # Add a global shift to increase difficulty
        shift = 0.5 * np.sum(np.sin(0.5 * x))
        result += shift
        
        return result