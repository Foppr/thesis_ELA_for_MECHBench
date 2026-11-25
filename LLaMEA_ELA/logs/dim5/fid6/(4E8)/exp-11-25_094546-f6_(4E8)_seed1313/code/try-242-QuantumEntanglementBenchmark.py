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
            
            # Enhanced quantum harmonic oscillator with chaotic modulation
            oscillator = xi**2 + 0.8 * np.sin(3.0 * xi) + 0.2 * np.cos(5.0 * xi) + 0.1 * np.sin(7.0 * xi)
            
            # Modified tunneling well with chaotic depth and position
            tunnel_depth = 0.6 * (1.0 + np.sin(self.dim * 0.8 + i * 0.4 + np.cos(i * 0.3)))
            tunnel_position = 0.3 * np.sin(xi * 3.0 + np.cos(i * 0.5))
            tunnel = tunnel_depth * np.exp(-xi**2 / 1.2) * np.sin(xi * 3.0 + tunnel_position)
            
            # Enhanced phase transitions with chaotic frequency modulation
            phase_freq = 0.8 * (1.0 + np.cos(i * 0.5 + self.dim * 0.4))
            phase_transition = phase_freq * (1.0 + np.tanh(3.0 * xi + i * 0.3 + np.sin(self.dim * 0.2)))
            
            # Improved entanglement with fractal coupling weights
            entanglement = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    coupling_strength = 0.3 * np.exp(-abs(i - j) * 0.7) * (1.0 + 0.2 * np.sin(i * j * 0.3))
                    entanglement += coupling_strength * np.sin(xi + x_norm[j] + 0.4 * np.cos(i + j + np.sin(i * 0.5)))
            
            # Hyperdimensional interference with chaotic modulation
            interference = np.sin(xi * 5.0 + np.sum(x_norm[:i]) * 0.6) * np.cos(xi * 4.0 + self.dim * 0.3 + np.sin(xi * 0.7))
            
            # Quantum amplitude modulation with fractal scaling
            amplitude = 1.0 + 0.3 * np.sin(np.sum(x_norm**2) * 0.6 + i * 0.4 + np.cos(self.dim * 0.5))
            
            # Apply quantum mechanical weighting with chaotic component
            weight = 1.0 + 0.4 * np.sin(i * 0.7 + np.cos(self.dim * 0.3)) * np.cos(self.dim * 0.3 + i * 0.5)
            
            # Add to result with enhanced quantum mechanical components
            result += weight * amplitude * (oscillator + tunnel)**2 + \
                     phase_transition * entanglement**2 + \
                     interference**2
            
        # Global scaling with chaotic dimension correction
        global_scale = 1.0 + 0.4 * np.sin(np.log(self.dim + 1) * 4.0 + np.cos(self.dim * 0.3))
        
        # Enhanced superposition modulation with hyperdimensional fractal component
        superposition = 1.0 + 0.25 * np.sin(np.sum(np.abs(x_norm)) * 3.0 + self.dim * 0.5 + np.cos(self.dim * 0.4))
        
        # Add chaotic noise to final result
        chaotic_noise = 0.05 * np.sin(np.sum(x_norm) * 10.0 + self.dim * 0.6)
        
        return global_scale * superposition * result / self.dim + chaotic_noise