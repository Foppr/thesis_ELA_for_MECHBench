import numpy as np

class AdaptiveRidgeHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Self-adaptive elliptic parameter sections
        self.elliptic_params = np.random.uniform(0.5, 2.5, (min(10, dim), 3))
        # Dynamic ridge structures with varying heights and widths
        self.ridge_heights = np.random.uniform(1.0, 4.0, min(8, dim))
        self.ridge_widths = np.random.uniform(0.5, 2.0, min(8, dim))
        # Stochastic harmonic interference patterns
        self.harmonic_amplitudes = np.random.uniform(0.8, 3.0, min(12, dim))
        self.harmonic_frequencies = np.random.uniform(1.0, 6.0, min(12, dim))
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = np.clip(x / 5.0, -1.0, 1.0)
        
        # Elliptic section terms with self-adaptive parameters
        elliptic_term = 0.0
        for i in range(min(len(self.elliptic_params), self.dim)):
            a, b, c = self.elliptic_params[i]
            # Adaptive elliptic curvature with polynomial modulation
            elliptic_val = a * (x_norm[i] ** 2) + b * (x_norm[i] ** 3) + c * np.exp(-0.5 * x_norm[i] ** 2)
            elliptic_term += elliptic_val
            
        # Dynamic ridge structures with harmonic modulation
        ridge_term = 0.0
        for i in range(min(len(self.ridge_heights), self.dim)):
            height = self.ridge_heights[i]
            width = self.ridge_widths[i]
            # Ridge with Gaussian-like shape and dynamic scaling
            ridge_val = height * np.exp(-0.5 * ((x_norm[i] / width) ** 2))
            ridge_term += ridge_val
            
        # Stochastic harmonic interference with varying phase shifts
        harmonic_term = 0.0
        for i in range(min(len(self.harmonic_amplitudes), self.dim)):
            amp = self.harmonic_amplitudes[i]
            freq = self.harmonic_frequencies[i]
            # Harmonic interference with dynamic phase and exponential decay
            phase_shift = np.pi * (i + 1) / (self.dim + 1)
            harmonic_val = amp * np.sin(freq * x_norm[i] + phase_shift) * \
                          np.exp(-0.2 * x_norm[i] ** 2)
            harmonic_term += harmonic_val
            
        # Cross-dimensional coupling with adaptive interaction weights
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i + 1, self.dim):
                # Adaptive coupling with dynamic weight adjustment based on dimension
                weight = 0.5 * (i + j) / self.dim
                coupling_val = weight * x_norm[i] * x_norm[j] * \
                              np.cos(2.0 * x_norm[i] + 1.5 * x_norm[j])
                coupling_term += coupling_val
                
        # Combined landscape with dynamic scaling and noise sensitivity
        result = 1.2 * elliptic_term + 0.9 * ridge_term + 0.8 * harmonic_term + 0.7 * coupling_term
        
        # Enhanced stochastic noise with dimensionality-dependent variance
        noise_variance = 0.03 * (1.0 + 0.08 * self.dim)
        noise = np.random.normal(0, noise_variance)
        
        return result + noise