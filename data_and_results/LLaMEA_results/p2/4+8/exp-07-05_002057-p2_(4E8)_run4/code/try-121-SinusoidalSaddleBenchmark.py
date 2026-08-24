import numpy as np

class SinusoidalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute periodic coefficients for each dimension
        np.random.seed(42)
        self.freq_coeffs = np.random.uniform(1.0, 10.0, dim)
        self.ampl_coeffs = np.random.uniform(0.5, 2.0, dim)
        self.phase_coeffs = np.random.uniform(0, 2 * np.pi, dim)
        # Saddle point structure parameters
        self.saddle_centers = np.random.uniform(-5.0, 5.0, (5, dim))
        self.saddle_strengths = np.random.uniform(0.5, 2.5, 5)
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic sinusoidal component
        periodic_sum = 0.0
        for i in range(self.dim):
            freq = self.freq_coeffs[i]
            ampl = self.ampl_coeffs[i]
            phase = self.phase_coeffs[i]
            periodic_sum += ampl * np.sin(freq * x[i] + phase)
        
        # Saddle point structure with multiple centers
        saddle_sum = 0.0
        for i in range(5):
            center = self.saddle_centers[i]
            strength = self.saddle_strengths[i]
            distance = np.sum((x - center) ** 2)
            saddle_sum += strength * np.exp(-distance / (2 * 1.0 ** 2))
        
        # Adaptive conditioning based on dimension
        conditioning = 0.0
        for i in range(self.dim):
            xi = x[i]
            conditioning += (xi ** 2) * (1 + 0.1 * np.sin(3 * xi))
        
        # Cross-dimensional coupling with interaction matrix
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x[i] * x[j]) * np.sin(0.5 * (x[i] + x[j]))
        
        # Combine all components
        result = 0.4 * periodic_sum + 0.3 * saddle_sum + 0.2 * conditioning + 0.1 * interaction
        
        return result