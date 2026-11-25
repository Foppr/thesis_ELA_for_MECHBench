import numpy as np

class ExponentialSphericalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency parameters for sinusoidal components
        self.frequencies = np.array([1.0 + 0.2 * np.sin(i * 0.5) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Spherical component with exponential weighting
        sphere_term = np.sum(x**2)
        result += np.exp(0.01 * sphere_term) * sphere_term
        
        # Exponential decay terms with sinusoidal modulation
        for i in range(self.dim):
            exp_decay = np.exp(-0.1 * x[i]**2) * np.cos(self.frequencies[i] * x[i])
            result += 0.5 * exp_decay
            
        # Cross-dimensional coupling with Gaussian kernels
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = (x[i] - x[j])**2
                coupling = np.exp(-0.05 * dist) * np.sin(x[i] + x[j])
                result += 0.3 * coupling
                
        # Add periodic modulation with varying amplitudes
        periodic_term = 0.0
        for i in range(self.dim):
            periodic_term += np.sin(2 * self.frequencies[i] * x[i]) * np.cos(3 * self.frequencies[i] * x[i])
        result += 0.2 * periodic_term
        
        # Add a multi-modal component with multiple peaks
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (x[i] - 2)**4 + (x[i] + 2)**4
        result += 0.1 * multimodal
        
        # Add noise to increase irregularity
        noise = 0.005 * np.sum(np.sin(10 * x))
        result += noise
        
        return result