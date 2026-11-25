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
            
            # Multi-scale quantum harmonic oscillator with dynamic frequency
            freq = 1.0 + 0.3 * np.sin(i * 0.7) + 0.2 * np.cos(i * 0.5)
            oscillator = (np.sin(freq * xi)**2 + 
                         0.5 * np.cos(2 * freq * xi) + 
                         0.3 * np.sin(3 * freq * xi) + 
                         0.1 * np.sin(5 * freq * xi))
            
            # Enhanced probabilistic tunneling wells with chaotic parameters
            tunneling = 0.0
            for k in range(1, 10):
                # Chaotic modulation of tunneling parameters
                modulator = 1.0 + 0.2 * np.sin(k * i * 0.3 + self.dim * 0.1)
                tunneling += (modulator / (k**2 + 0.5)) * np.exp(-k * np.abs(xi)) * np.cos(k * xi + modulator * 0.5)
            
            # Adaptive energy landscape with multi-phase transitions
            phase_shift = 0.1 * np.sin(i * 0.4 + self.dim * 0.2)
            energy_factor = (1.0 + 
                           0.5 * np.sin(self.dim * 0.3 + i * 0.2 + phase_shift) + 
                           0.3 * np.cos(self.dim * 0.4 + i * 0.1 + phase_shift) +
                           0.2 * np.sin(self.dim * 0.6 + i * 0.3 + phase_shift))
            
            # Enhanced cross-dimensional entanglement with fractal coupling
            entanglement = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    # Fractal dimensionality in coupling strength
                    coupling_strength = 1.0 / (1.0 + (xi - x_norm[j])**2 + 0.1 * np.sin(i * j * 0.2))
                    entanglement += coupling_strength * np.sin(xi + x_norm[j] + 0.3 * np.cos(i + j))
            
            # Quantum interference terms with dynamic phase
            interference = 0.0
            for k in range(1, 8):
                phase = k * 0.5 + 0.2 * np.sin(i * 0.3 + k * 0.4)
                interference += (1.0 / k**1.5) * np.sin(k * xi + phase) * np.cos(k * x_norm[i % self.dim] + phase)
            
            # Combine all components with chaotic weighting
            weight = 1.0 + 0.3 * np.sin(i * 0.7 + self.dim * 0.2) * np.cos(self.dim * 0.3 + i * 0.4)
            result += weight * (energy_factor * oscillator + tunneling + 0.5 * entanglement + 0.3 * interference)**2
            
        # Add chaotic global scaling factor
        chaotic_correction = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 3.0 + self.dim * 0.1) + 0.1 * np.cos(np.log(self.dim + 1) * 2.0)
        return chaotic_correction * result / self.dim