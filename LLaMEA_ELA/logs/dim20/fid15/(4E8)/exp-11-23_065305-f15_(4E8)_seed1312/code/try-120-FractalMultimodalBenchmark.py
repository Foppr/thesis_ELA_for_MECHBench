import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        # Precompute logistic map coefficients for chaos
        self.logistic_r = 3.97
        self.fractal_scale = 1.0
        
    def f(self, x):
        x = np.array(x)
        # Clip to domain [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize fractal component
        fractal_val = 0.0
        
        # Scale-invariant hierarchical structure using multiple resolutions
        for level in range(1, min(5, self.dim + 1)):
            scale = 2 ** (-level)
            # Apply logistic map at each level for chaotic behavior
            logistic_vals = np.zeros_like(x)
            current_x = x.copy()
            for _ in range(3):  # Apply logistic map dynamics
                logistic_vals = self.logistic_r * current_x * (1 - current_x)
                current_x = logistic_vals
            
            # Scale and accumulate fractal contribution
            fractal_val += scale * np.sum(logistic_vals**2)
        
        # Multi-scale sinusoidal coupling with varying frequencies
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 2 ** (i % 4)  # Varying frequencies
            sinusoidal += np.sin(freq * x[i]) * np.cos(freq * x[i] / 2)
        
        # Add chaotic radial component with fractal scaling
        radius = np.sqrt(np.sum(x**2))
        radial_oscillation = np.sin(10 * radius) * np.exp(-radius / 5)
        
        # Add self-similar valley structure using inverse polynomial scaling
        valley_depth = 0.0
        for i in range(self.dim):
            valley_depth += 1.0 / (1 + 0.1 * (x[i] - 2)**2 + 0.05 * (x[i] + 2)**2)
        
        # Combine all components with varying weights
        result = fractal_val + 0.5 * sinusoidal + 0.3 * radial_oscillation + 0.2 * valley_depth
        
        # Add noise component for robustness testing
        noise = 0.01 * np.sum(np.random.randn(self.dim) * x)
        
        return float(result + noise)