import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Separable quadratic terms with varying condition numbers
        for i in range(self.dim):
            result += 0.5 * (x[i]**2) * (1.0 + 0.5 * np.sin(i * 0.5))
        
        # Non-separable high-order interactions with chaotic coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling range
                coupling = np.sin(3.0 * (x[i] + x[j])) * np.cos(2.0 * (x[i] - x[j]))
                result += 0.3 * coupling * (1.0 + 0.2 * np.sin(i * 0.7 + j * 0.3))
        
        # Chaotic sine-wave modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.4)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            result += amp * np.sin(freq * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Saddle-point inducing higher-order polynomial terms
        for i in range(self.dim):
            result += 0.1 * x[i]**5 * np.cos(0.5 * x[i]) + 0.05 * x[i]**6
        
        # Multi-modal sinusoidal perturbations with varying periods and amplitudes
        for i in range(self.dim):
            period = 2.0 + 1.5 * np.sin(i * 0.6)
            amp = 0.8 + 0.4 * np.cos(i * 0.5)
            result += amp * np.sin(period * x[i] + 0.5 * np.sin(2.0 * x[i]))
        
        # Dimensionality-dependent scaling factor
        result *= (1.0 + 0.1 * np.log(self.dim + 1))
        
        # Add small noise to increase robustness
        noise = 0.001 * np.sum(np.random.rand(self.dim) * x**2)
        result += noise
        
        return result