import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial valley component with chaotic exponent modulation and dynamic scaling
        poly_valley = 0.0
        for i in range(self.dim):
            exponent = 2 + (i % 5) + 0.5 * np.sin(i * 1.3)
            scale = 1.0 + 0.3 * np.cos(i * 0.7)
            poly_valley += (x[i] ** exponent) * scale * np.cos(0.2 * x[i])
        
        # Gaussian peak component with time-varying positions, amplitudes, and widths
        gaussian_peak = 0.0
        for i in range(self.dim):
            height = 1.0 + 0.5 * np.sin(i * 0.8 + self.dim)
            width = 0.2 + 0.3 * np.cos(i * 0.6 + self.dim)
            position = -3.0 + 6.0 * (i / self.dim) + 0.2 * np.sin(i * 0.5)
            gaussian_peak += height * np.exp(-0.5 * ((x[i] - position) ** 2) / (width ** 2))
        
        # Logarithmic barrier with entropy-based asymmetry and multi-scale modulation
        log_barrier = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                entropy_term = np.log(-x[i] + 5.0) * (1.0 + 0.2 * np.sin(i * 0.4))
                log_barrier += entropy_term * np.exp(-0.2 * x[i]) * (1.0 + 0.1 * np.cos(i))
            else:
                entropy_term = np.log(x[i] + 5.0) * (1.0 + 0.2 * np.cos(i * 0.4))
                log_barrier += entropy_term * np.exp(0.2 * x[i]) * (1.0 + 0.1 * np.sin(i))
        
        # Cross-dimensional coupling with chaotic phase shifts and multi-frequency interactions
        cross_coupling = 0.0
        for i in range(self.dim-1):
            phase_shift = 0.3 * np.sin(i * 0.5 + self.dim * 0.1)
            freq1 = 0.4 + 0.2 * np.cos(i * 0.3)
            freq2 = 0.6 + 0.3 * np.sin(i * 0.4)
            cross_coupling += np.sin(x[i] * x[i+1] + phase_shift) * np.cos(freq1 * (x[i] + x[i+1]) + phase_shift) * np.exp(-0.1 * abs(x[i] - x[i+1]))
        
        # High-frequency oscillation with adaptive frequency modulation
        high_freq = 0.0
        for i in range(self.dim):
            freq_mod = 15.0 + 5.0 * np.sin(i * 0.3)
            high_freq += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.5)
        
        # Entropy-based scaling factor with dimension-dependent modulation
        entropy_scale = 1.5 + 0.4 * np.log(self.dim + 2) + 0.1 * np.sin(self.dim * 0.3)
        
        # Add a noise term that depends on the landscape's complexity
        noise_term = 0.02 * np.random.rand() * (1.0 + 0.1 * np.sum(np.abs(x)))
        
        return (poly_valley + gaussian_peak + log_barrier + cross_coupling + high_freq) * entropy_scale + noise_term