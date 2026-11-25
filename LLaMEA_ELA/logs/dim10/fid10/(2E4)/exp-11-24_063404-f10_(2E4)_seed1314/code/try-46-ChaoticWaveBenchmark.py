import numpy as np

class ChaoticWaveBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Exponential decay modulated radial component with multiple scales
        r = np.sqrt(np.sum(x_scaled**2))
        radial = np.exp(-r**2) * (np.sin(10 * r) + 0.5 * np.sin(30 * r) + 0.3 * np.sin(60 * r))
        
        # Trigonometric wave interference pattern in angular dimensions
        angular = 0.0
        if self.dim > 1:
            angles = np.arctan2(x_scaled[1], x_scaled[0])
            # Wave interference with varying frequencies and amplitudes
            for i in range(1, min(8, self.dim)):
                freq = i * 7 + np.sin(i * 0.5)
                amp = 1.0 / (1.0 + 0.1 * i)
                angular += amp * np.sin(freq * angles) * np.cos(freq * angles)
        
        # Multi-scale polynomial with adaptive exponents
        poly_term = 0.0
        for i in range(self.dim):
            poly_term += (x_scaled[i]**(3 + i % 4)) * np.exp(-0.5 * abs(x_scaled[i]))
        
        # Cross-dimensional coupling with exponential decay and sinusoidal modulation
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_scaled[i] - x_scaled[j])
                cross_coupling += np.exp(-dist**2) * np.sin(15 * (x_scaled[i] + x_scaled[j]))
        
        # Adaptive chaotic perturbation with dynamic frequency modulation
        chaos = 0.0
        for i in range(self.dim):
            freq_mod = 10 + 5 * np.sin(x_scaled[i] * 2)
            chaos += np.sin(freq_mod * x_scaled[i]) * np.cos(freq_mod * x_scaled[i])
        
        # Sparse gradient landscape with discontinuous regions
        sparse_term = 0.0
        for i in range(self.dim):
            sparse_term += np.sin(25 * x_scaled[i]) * np.exp(-0.1 * abs(x_scaled[i]))
        
        # Combine all components with carefully tuned weights
        return (0.8 * radial + 0.6 * angular + 0.4 * poly_term + 
                0.3 * cross_coupling + 0.2 * chaos + 0.05 * sparse_term)