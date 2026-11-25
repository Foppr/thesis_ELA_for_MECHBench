import numpy as np

class QuantumSaddleFractalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Quantum-inspired oscillatory component with phase modulation
        quantum_term = 0.0
        for i in range(self.dim):
            phase = np.pi * (i + 1) / (self.dim + 1)
            freq = 3.0 + 2.0 * np.sin(phase)
            amp = 1.5 + 0.8 * np.cos(phase)
            quantum_term += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.7 + phase)
        
        # Saddle-point gradient field with hyperbolic tangent components
        saddle_term = 0.0
        for i in range(self.dim):
            # Create saddle points with varying strength
            strength = 1.0 + 0.5 * np.sin(i * 0.8)
            saddle_term += strength * np.tanh(x[i]) * (x[i] ** 2 - 1.0)
        
        # Log-periodic fractal structure with multi-scale self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            # Log-periodic scaling with varying exponents
            log_scale = 1.0 + 0.7 * np.sin(i * 0.6)
            fractal_term += np.exp(-log_scale * np.abs(x[i])) * np.cos(log_scale * np.log(np.abs(x[i]) + 1e-8))
        
        # Coupled harmonic oscillators with time-varying coupling strength
        coupled_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling_strength = 0.5 + 0.5 * np.sin((i + j) * 0.3)
                coupled_term += coupling_strength * np.sin(x[i] - x[j]) * np.cos(x[i] + x[j])
        
        # Multi-scale Gaussian peaks with varying amplitudes and positions
        peak_term = 0.0
        for i in range(self.dim):
            # Multiple peaks per dimension
            for k in range(3):
                peak_height = 1.0 + 0.5 * np.sin(i * 0.7 + k * 0.9)
                peak_width = 0.3 + 0.4 * np.cos(i * 0.6 + k * 0.8)
                peak_position = -4.0 + 8.0 * np.sin(i * 0.5 + k * 0.7)
                peak_term += peak_height * np.exp(-0.5 * ((x[i] - peak_position) / peak_width) ** 2)
        
        # Exponential decay with periodic modulation
        decay_term = 0.0
        for i in range(self.dim):
            mod_freq = 2.0 + 1.5 * np.cos(i * 0.4)
            decay_term += np.exp(-0.3 * x[i] ** 2) * np.sin(mod_freq * x[i])
        
        # Final weighted combination
        total = 0.25 * quantum_term + 0.20 * saddle_term + 0.18 * fractal_term + 0.15 * coupled_term + 0.12 * peak_term + 0.08 * decay_term
        
        # Global conditioning with dimension-dependent scaling
        global_factor = 1.0 + 0.3 * np.sin(self.dim * 0.5) * np.cos(self.dim * 0.2)
        
        return total * global_factor