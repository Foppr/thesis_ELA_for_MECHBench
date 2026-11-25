import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with conditioning
        result = 0.5 * np.sum(x**2)
        
        # Chaotic multi-scale sine-wave interactions with dynamic modulation
        for i in range(self.dim):
            # Dynamic amplitude and frequency based on position and dimension
            amp = 1.5 + 0.5 * np.sin(x[i] * 0.7) + 0.3 * (i % 7)
            freq = 2.0 + 0.8 * np.cos(x[i] * 0.5) + 0.4 * (i % 5)
            
            # Chaotic oscillation with multiple interacting sine waves
            oscillation = 0.0
            for k in range(1, 6):
                phase = k * np.pi / 4 + x[i] * 0.1 * k
                oscillation += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] / (k + 2))
            
            result += 0.8 * oscillation
            
        # Asymmetric saddle points with chaotic decay
        for i in range(self.dim):
            asym_term = 0.3 * x[i]**4 * np.exp(-0.15 * np.abs(x[i]))
            result += asym_term
            
        # Adaptive cross-dimension coupling with fractal-like structure
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Adaptive coupling strength based on dimension and position
                coupling_strength = 0.2 * (1 + 0.1 * (i + j)) * np.sin(x[i] * x[j])
                coupling = coupling_strength * np.exp(-0.3 * (x[i]**2 + x[j]**2))
                result += coupling
                
        # Add chaotic scaling factor dependent on dimension and position
        chaos_factor = 1.0 + 0.1 * np.sum(np.sin(x) * np.cos(x)) + 0.02 * self.dim
        result *= chaos_factor
        
        # Add high-frequency noise component for increased complexity
        noise = 0.05 * np.sum(np.sin(10 * x) * np.cos(8 * x))
        result += noise
        
        return result