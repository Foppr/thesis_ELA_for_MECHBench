import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Quadratic basin term - encourages convergence to center
        basin_term = np.sum(x**2) * 0.05
        
        # Exponentially decaying sinusoidal waves
        wave_term = 0.0
        for i in range(self.dim):
            # Create exponentially decaying waves in each dimension
            decay_factor = np.exp(-0.1 * (i + 1))
            wave_term += decay_factor * np.sin(2 * np.pi * x[i]) * np.cos(4 * np.pi * x[i])
        
        # Add multiple local minima using Gaussian peaks
        gaussian_term = 0.0
        num_peaks = 3
        for i in range(num_peaks):
            for j in range(num_peaks):
                peak_x = -3.0 + 3.0 * i / (num_peaks - 1) if num_peaks > 1 else 0.0
                peak_y = -3.0 + 3.0 * j / (num_peaks - 1) if num_peaks > 1 else 0.0
                
                # Only use first two dimensions for peaks, rest are zero
                distance = 0.0
                if self.dim >= 1:
                    distance += (x[0] - peak_x)**2
                if self.dim >= 2:
                    distance += (x[1] - peak_y)**2
                    
                gaussian_term += np.exp(-distance / 2.0)
        
        # Add noise to make it non-trivial
        noise = np.sum(np.random.normal(0, 0.01, len(x)))
        
        return basin_term - wave_term + gaussian_term + noise