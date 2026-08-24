import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodic coefficients for cross-dimensional interactions
        self.periodic_coeffs = np.array([np.sin(i * 0.5) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Sinusoidal ruggedness with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(i * 0.3)
            amp = 1.0 + 0.5 * np.cos(i * 0.4)
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Cross-dimensional coupling with periodic coefficients
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = self.periodic_coeffs[i] * self.periodic_coeffs[j]
                result += 0.3 * coupling * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Saddle-point attractor with enhanced basin complexity
        saddle_term = 0.0
        for i in range(self.dim):
            saddle_term += np.sin(2 * x[i]) * np.cos(3 * x[i])
        result += 0.2 * saddle_term**2
        
        # Global minimum enforcing with logarithmic barrier
        result += 0.1 * np.sum(np.log(1.0 + np.abs(x)))
        
        # Multi-scale oscillatory components with dynamic scaling
        for i in range(self.dim):
            scale = 1.0 + 0.3 * np.sin(i * 0.7)
            result += 0.25 * np.sin(scale * x[i]) * np.cos(scale * x[i] * 0.3) * np.exp(-0.02 * x[i]**2)
            
        # Enhanced noise with periodic modulation
        noise = 0.0
        for i in range(self.dim):
            noise += 0.1 * np.sin(15 * x[i]) * np.cos(7.5 * x[i]) * np.sin(i * 0.2)
        result += noise
        
        # Fractal-like self-similarity through recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            fractal += 0.1 * np.sin(4 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.01 * i)
        result += fractal
        
        # Memory-dependent component with influence from previous evaluation
        if hasattr(self, 'prev_x'):
            memory_influence = 0.0
            for i in range(self.dim):
                memory_influence += 0.05 * (x[i] - self.prev_x[i]) * np.sin(x[i])
            result += memory_influence
        self.prev_x = x.copy()
        
        return result