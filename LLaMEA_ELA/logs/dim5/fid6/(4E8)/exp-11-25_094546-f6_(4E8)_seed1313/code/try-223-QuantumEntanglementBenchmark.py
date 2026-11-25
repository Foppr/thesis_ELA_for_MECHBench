import numpy as np

class QuantumEntanglementBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Quantum harmonic oscillator potential with entanglement
            oscillator = xi**2 + 0.6 * np.sin(3.0 * xi) + 0.15 * np.cos(5.0 * xi)
            
            # Probabilistic tunneling well with dimension-dependent depth
            tunnel_depth = 0.4 * (1.0 + np.sin(self.dim * 0.6 + i * 0.35))
            tunnel = tunnel_depth * np.exp(-xi**2 / 1.5) * np.sin(xi * 2.5)
            
            # Adaptive energy landscape with phase transitions
            energy_scale = 1.0 + 0.5 * np.sin(i * 0.75 + self.dim * 0.35)
            phase_transition = 0.6 * (1.0 + np.tanh(2.5 * xi + i * 0.25))
            
            # Cross-dimensional entanglement with interaction weights
            entanglement = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    coupling_strength = 0.25 * np.exp(-abs(i - j) * 0.6)
                    entanglement += coupling_strength * np.sin(xi + x_norm[j] + 0.35 * np.cos(i + j))
            
            # Quantum interference pattern with fractal modulation
            interference = np.sin(xi * 4.5 + np.sum(x_norm[:i]) * 0.55) * np.cos(xi * 3.5 + self.dim * 0.25)
            
            # Add to result with quantum mechanical weighting
            weight = 1.0 + 0.35 * np.sin(i * 0.65) * np.cos(self.dim * 0.25 + i * 0.45)
            
            # Apply quantum amplitude modulation
            amplitude = 1.0 + 0.25 * np.sin(np.sum(x_norm**2) * 0.55 + i * 0.35)
            
            result += weight * amplitude * (energy_scale * (oscillator + tunnel)**2 + 
                                          phase_transition * entanglement**2 + 
                                          interference**2)
            
        # Global quantum scaling with dimension-dependent correction
        global_scale = 1.0 + 0.35 * np.sin(np.log(self.dim + 1) * 3.5)
        
        # Add quantum superposition modulation
        superposition = 1.0 + 0.2 * np.sin(np.sum(np.abs(x_norm)) * 2.5 + self.dim * 0.45)
        
        return global_scale * superposition * result / self.dim