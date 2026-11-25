import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial valley component with varying exponents and noise
        poly_valley = 0.0
        for i in range(self.dim):
            exponent = 2 + (i % 4)
            noise = 0.1 * np.sin(i * x[i])
            poly_valley += (x[i] ** exponent) * np.cos(0.3 * x[i]) + noise
        
        # Gaussian peak component with dynamic positions and amplitudes
        gaussian_peak = 0.0
        for i in range(self.dim):
            height = 1.5 + 0.8 * np.sin(i * 0.5)
            width = 0.3 + 0.4 * np.cos(i * 0.7)
            position = -2.0 + 4.0 * (i / self.dim)  # Dynamic peak positions
            gaussian_peak += height * np.exp(-0.5 * ((x[i] - position) ** 2) / (width ** 2))
        
        # Logarithmic barrier component with multi-exponential scaling and asymmetry
        log_barrier = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                log_barrier += np.log(-x[i] + 5.0) * np.exp(-0.15 * x[i]) * (1.0 + 0.2 * np.sin(i))
            else:
                log_barrier += np.log(x[i] + 5.0) * np.exp(0.15 * x[i]) * (1.0 + 0.2 * np.cos(i))
        
        # Novel cross-dimensional coupling with sine-cosine interactions and phase shifts
        cross_coupling = 0.0
        for i in range(self.dim-1):
            phase_shift = 0.5 * np.sin(i * 0.3)
            cross_coupling += np.sin(x[i] * x[i+1] + phase_shift) * np.cos(0.4 * (x[i] + x[i+1]) + phase_shift)
        
        # Additional high-frequency oscillation component
        high_freq = 0.0
        for i in range(self.dim):
            high_freq += np.sin(10.0 * x[i]) * np.cos(5.0 * x[i])
        
        # Global scaling factor with dimension-dependent modulation and random perturbation
        scale_factor = 1.2 + 0.2 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim)
        
        # Add a small random noise term to increase robustness testing
        noise_term = 0.01 * np.random.rand()
        
        return (poly_valley + gaussian_peak + log_barrier + cross_coupling + high_freq) * scale_factor + noise_term