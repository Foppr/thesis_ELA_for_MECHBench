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
            # Varying quadratic weights to create condition number variation
            weight = 1.0 + 0.5 * np.sin(i * 0.7)
            result += 0.5 * weight * x[i]**2
        
        # Non-separable chaotic correlation terms with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Exponentially decaying correlation with chaotic phase
                distance = np.abs(x[i] - x[j])
                phase = np.sin(3.0 * (x[i] + x[j]) + 0.5 * np.cos(2.0 * x[i]) * np.sin(1.5 * x[j]))
                coupling = np.exp(-0.1 * distance**2) * phase
                result += 0.3 * coupling
        
        # Sine-based multimodal components with varying frequencies
        for i in range(self.dim):
            result += 0.8 * np.sin(2.0 * np.pi * x[i]) + 0.4 * np.sin(4.0 * np.pi * x[i]) + 0.2 * np.sin(8.0 * np.pi * x[i])
        
        # Fractal-like perturbations using fractional exponents and trigonometric combinations
        for i in range(self.dim):
            result += 0.15 * np.sin(10.0 * x[i]) * np.cos(5.0 * x[i]) * np.abs(x[i])**0.7
        
        # Add saddle-point inducing higher-order terms
        for i in range(self.dim):
            result += 0.1 * x[i]**5 - 0.3 * x[i]**3
        
        # Dimensionality-dependent scaling with logarithmic growth
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        result *= dim_factor
        
        return result