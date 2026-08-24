import numpy as np

class ExponentialBarrierBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute coefficients for sinusoidal perturbations
        self.coeffs = np.random.uniform(0.5, 2.0, dim)
        self.phases = np.random.uniform(0, 2*np.pi, dim)
    
    def f(self, x):
        # Scale input to [-1, 1]
        x_scaled = x / 5.0
        
        # Exponential barrier terms with varying steepness
        barrier = 0.0
        for i in range(self.dim):
            # Create exponential barriers at specific points
            barrier += np.exp(5 * (1 - np.abs(x_scaled[i])) * (x_scaled[i] > 0)) + \
                      np.exp(5 * (1 - np.abs(x_scaled[i])) * (x_scaled[i] < 0))
        
        # Polynomial conditioning with mixed degrees
        poly_cond = 0.0
        for i in range(self.dim):
            poly_cond += (x_scaled[i]**2 + 0.1 * x_scaled[i]**4 + 0.01 * x_scaled[i]**6)
        
        # Sinusoidal perturbations with varying frequencies and amplitudes
        sin_pert = 0.0
        for i in range(self.dim):
            freq = 2 * (i + 1)
            amp = 0.5 * (i + 1)
            sin_pert += amp * np.sin(freq * x_scaled[i] + self.phases[i])
        
        # Cross-term interactions with exponential decay
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2) * \
                             np.sin(3 * (x_scaled[i] + x_scaled[j]))
        
        # Global minimum at origin with additional noise
        return barrier + 0.5 * poly_cond + 0.3 * sin_pert + 0.2 * cross_term + 0.1 * np.random.random()