import numpy as np

class MultiModalTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodic coefficients for cross-dimensional interactions
        self.coeffs = np.array([np.sin(i * 0.5) + np.cos(i * 0.3) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quadratic base term
        result = np.sum(x**2)
        
        # Sinusoidal ruggedness with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.4)
            amp = 1.0 + 0.5 * np.cos(i * 0.3)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Cross-dimensional interaction with periodic coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coeff = self.coeffs[i] * self.coeffs[j]
                result += coeff * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Multi-scale periodic components with increasing complexity
        for i in range(self.dim):
            result += 0.3 * np.sin(4 * x[i]) * np.cos(2 * x[i]) * np.sin(0.5 * x[i])
            
        # Global minimum attractor with complex trigonometric function
        attractor = 0.0
        for i in range(self.dim):
            attractor += np.sin(x[i] * 0.5) * np.cos(x[i] * 0.3) * np.sin(x[i] * 0.1)
        result += 0.2 * attractor**2
        
        # Sharp peaks and valleys using high-frequency oscillations
        for i in range(self.dim):
            result += 0.1 * np.sin(10 * x[i]) * np.cos(5 * x[i]) * np.exp(-0.05 * x[i]**2)
            
        # Fractal-like self-similarity through recursive trigonometric terms
        for i in range(self.dim):
            result += 0.05 * np.sin(3 * x[i]) * np.cos(1.5 * x[i]) * np.sin(0.75 * x[i])
            
        # Memory-dependent component using previous x values if available
        if hasattr(self, 'prev_x'):
            memory_term = 0.0
            for i in range(self.dim):
                memory_term += 0.03 * (x[i] - self.prev_x[i]) * np.sin(x[i])
            result += memory_term
        self.prev_x = x.copy()
        
        # Add noise-like perturbations with controlled amplitude
        noise = 0.0
        for i in range(self.dim):
            noise += 0.02 * np.sin(15 * x[i]) * np.cos(7 * x[i])
        result += noise
        
        return result