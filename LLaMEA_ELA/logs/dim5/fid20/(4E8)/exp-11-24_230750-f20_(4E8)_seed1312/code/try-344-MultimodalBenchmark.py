import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential-logarithmic potential with chaotic modulation
        exp_log_potential = 0.0
        for i in range(self.dim):
            base = np.exp(0.3 * x[i]) + np.log(np.abs(x[i]) + 1.0)
            chaos_mod = 1.0 + 0.5 * np.sin(2.0 * x[i] + np.cos(x[i]))
            exp_log_potential += base * chaos_mod
        
        # Cross-dimensional saddle-point interactions with time-variant weights
        saddle_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                weight = np.sin(0.5 * (x[i] + x[j]) + 0.3 * np.cos(0.7 * x[i])) * \
                         np.cos(0.4 * (x[i] - x[j]) + 0.2 * np.sin(0.6 * x[j]))
                saddle_interaction += weight * (x[i]**2 - x[j]**2)
        
        # Asymmetric sinusoidal modulation with dynamic frequency and amplitude
        sin_modulation = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(0.8 * x[i] + 0.4)
            amp = 1.0 + 0.7 * np.cos(0.6 * x[i]**2 + 0.3)
            phase = 0.2 * np.sin(1.5 * x[i] + 0.1)
            sin_modulation += amp * np.sin(freq * x[i] + phase) * np.exp(-0.2 * x[i]**2)
        
        # Logarithmic barrier with adaptive scaling
        barrier = 0.0
        for i in range(self.dim):
            barrier += np.log(1.0 + 0.5 * (x[i]**2 + 1.0)) * \
                       (1.0 + 0.3 * np.sin(0.9 * x[i] + 0.5))
        
        # Time-variant harmonic coupling with chaotic phase shifts
        time_coupling = 0.0
        t = 0.5 * self.dim + 1.0
        for i in range(self.dim):
            phase_shift = np.sin(t + 0.4 * x[i]) * np.cos(0.3 * x[i]**2)
            time_coupling += np.sin(x[i] + phase_shift) * np.cos(0.7 * x[i])
        
        # Dimensionally varying normalization with hyperbolic scaling
        norm_factor = 1.0 + 0.2 * np.tanh(self.dim / 5.0) + 0.1 * np.log(self.dim + 1)
        
        return (0.3 * exp_log_potential + 0.25 * saddle_interaction + 
                0.2 * sin_modulation + 0.15 * barrier + 0.1 * time_coupling) * norm_factor