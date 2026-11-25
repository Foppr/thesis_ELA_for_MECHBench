import numpy as np

class MultimodalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute adaptive parameters for each dimension
        self.freq_params = np.array([2.0 + 0.5 * np.sin(i * 0.8) for i in range(dim)])
        self.amp_params = np.array([1.0 + 0.3 * np.cos(i * 0.6) for i in range(dim)])
        self.conditioning = np.array([0.5 + 0.5 * np.sin(i * 0.4) for i in range(dim)])
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Trigonometric oscillation component with adaptive frequencies and amplitudes
        for i in range(self.dim):
            freq = self.freq_params[i]
            amp = self.amp_params[i]
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i])
            
        # Radial basis function component with varying widths
        for i in range(self.dim):
            width = 0.5 + 0.5 * np.sin(i * 0.3)
            result += np.exp(-width * x[i]**2) * np.sin(x[i])
            
        # Cross-dimensional coupling with adaptive conditioning
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cond = self.conditioning[i] + self.conditioning[j]
                coupling = np.sin(x[i] * x[j]) * np.exp(-cond * (x[i]**2 + x[j]**2))
                result += coupling
                
        # Add multiple local minima using cosine peaks
        for i in range(self.dim):
            peak_positions = np.array([-3.0, -1.0, 1.0, 3.0])
            for pos in peak_positions:
                result += 0.5 * np.cos(2 * np.pi * (x[i] - pos)) * np.exp(-0.1 * (x[i] - pos)**2)
                
        # Adaptive conditioning component
        condition_factor = 1.0 + 0.3 * np.sum(self.conditioning)
        result *= condition_factor
        
        # Add noise for increased irregularity
        noise = 0.02 * np.sum(np.sin(x * 7) * np.cos(x * 3))
        result += noise
        
        return result