import numpy as np

class QuantumHarmonicResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        x = np.array(x)
        
        # Quantum-inspired harmonic oscillators with time-varying frequencies and amplitudes
        quantum_term = 0.0
        for i in range(self.dim):
            freq = 1.5 + 1.2 * np.sin(i * 0.6 + self.dim * 0.3)
            amp = 1.0 + 0.8 * np.cos(i * 0.5 + self.dim * 0.4)
            phase = 0.5 * np.sin(i * 0.8 + self.dim * 0.2)
            quantum_term += amp * np.sin(freq * x[i] + phase) * np.cos(freq * x[i] * 0.7 + phase)
        
        # Hyperbolic tangent gradient modulation with adaptive steepness
        tanh_term = 0.0
        for i in range(self.dim):
            steepness = 2.0 + 1.5 * np.sin(i * 0.4 + self.dim * 0.3)
            tanh_term += np.tanh(steepestness * x[i]) * np.exp(-0.5 * x[i] ** 2)
        
        # Stochastic resonance mechanism with multiplicative noise and coupling
        noise_term = 0.0
        for i in range(self.dim):
            coupling_strength = 0.3 + 0.4 * np.sin(i * 0.7 + self.dim * 0.25)
            noise = np.random.normal(0, 0.1)
            noise_term += coupling_strength * x[i] * np.exp(-0.3 * x[i] ** 2) * noise
        
        # Multi-scale fractal-like structure with recursive cosine components
        fractal_term = 0.0
        for i in range(self.dim):
            scale = 1.0 + 0.7 * np.sin(i * 1.1 + self.dim * 0.4)
            fractal_term += np.cos(x[i] * scale) * np.sin(x[i] * scale * 0.8) * np.exp(-0.2 * x[i] ** 2)
        
        # Coupled nonlinear oscillators with phase interactions
        coupled_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(x[i] - x[j]) * np.cos(x[i] + x[j])
                coupled_term += coupling ** 2
        
        # Adaptive peak landscape with varying heights and positions
        peak_term = 0.0
        for i in range(self.dim):
            h1 = 2.5 + 1.5 * np.sin(i * 0.9)
            w1 = 0.3 + 0.7 * np.cos(i * 0.6)
            p1 = -2.0 + 4.0 * np.sin(i * 0.8)
            h2 = 1.8 + 1.2 * np.cos(i * 0.7)
            w2 = 0.5 + 0.8 * np.sin(i * 0.5)
            p2 = -3.0 + 3.0 * np.cos(i * 0.6)
            peak1 = h1 * np.exp(-0.5 * ((x[i] - p1) / w1) ** 2)
            peak2 = h2 * np.exp(-0.5 * ((x[i] - p2) / w2) ** 2)
            peak_term += 0.7 * peak1 + 0.3 * peak2
        
        # Quantum tunneling effect with complex phase interference
        tunnel_term = 0.0
        for i in range(self.dim):
            phase_shift = np.pi * np.sin(i * 0.5 + self.dim * 0.3)
            tunnel_term += np.exp(-0.4 * x[i] ** 2) * np.cos(x[i] * 1.5 + phase_shift)
        
        # Final combination with weighted components
        total = 0.25 * quantum_term + 0.20 * tanh_term + 0.15 * noise_term + 0.18 * fractal_term + 0.12 * coupled_term + 0.08 * peak_term + 0.02 * tunnel_term
        
        # Global conditioning with adaptive scaling factor
        global_scale = 1.0 + 0.3 * np.sin(self.dim * 0.6) * np.cos(self.dim * 0.4)
        
        return total * global_scale