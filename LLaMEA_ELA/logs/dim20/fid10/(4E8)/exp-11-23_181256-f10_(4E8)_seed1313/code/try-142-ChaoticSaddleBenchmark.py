import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Logarithmic repulsion terms with adaptive strength
        log_repulsion = np.sum(np.log(1.0 + 0.3 * np.abs(x_scaled) + 0.05 * x_scaled**2))
        
        # Multi-scale harmonic interference with varying frequencies and amplitudes
        harmonic_sum = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.4 * np.sin(0.3 * i)
            amp = 1.0 + 0.2 * np.cos(0.25 * i)
            harmonic_sum += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i]**2)
        
        # Adaptive curvature terms with variable exponents and multi-scale influence
        curvature = 0.0
        for i in range(self.dim):
            exp_base = 1.5 + 0.3 * np.sin(0.4 * i)
            curvature += (x_scaled[i]**2 + 0.1)**exp_base
        
        # Chaotic saddle-point attraction with multi-dimensional coupling
        saddle = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                saddle += np.sin(x_scaled[i] * x_scaled[j]) * np.exp(-0.5 * (x_scaled[i] - x_scaled[j])**2)
        
        # Exponential decay with oscillatory modulation
        exp_decay = np.sum(np.exp(-0.5 * x_scaled**2) * (1.0 + 0.3 * np.sin(3.0 * x_scaled)))
        
        # Multi-modal exponential interactions with phase shifts
        modal_exp = 0.0
        for i in range(self.dim):
            phase = 0.5 * np.sin(0.2 * i)
            modal_exp += np.exp(-0.3 * (x_scaled[i] - phase)**2) * np.cos(2.0 * x_scaled[i])
        
        # Cross-dimensional coupling with varying strength
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                strength = 0.5 + 0.3 * np.sin(0.1 * (i + j))
                cross_coupling += strength * np.tanh(x_scaled[i] * x_scaled[j])
        
        # Combine all components with carefully tuned weights
        return 2.5 * log_repulsion + 1.8 * harmonic_sum + 0.7 * curvature + 0.6 * saddle + 0.4 * exp_decay + 0.3 * modal_exp + 0.2 * cross_coupling