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
            
            # Enhanced quantum harmonic oscillator with adaptive frequency
            freq = 1.0 + 0.4 * np.sin(i * 0.6) + 0.3 * np.cos(i * 0.4)
            oscillator = (np.sin(freq * xi)**2 + 
                         0.6 * np.cos(2 * freq * xi) + 
                         0.4 * np.sin(3 * freq * xi) + 
                         0.2 * np.sin(5 * freq * xi))
            
            # Enhanced probabilistic tunneling wells with chaotic parameters
            tunneling = 0.0
            for k in range(1, 12):
                # Chaotic modulation of tunneling parameters
                modulator = 1.0 + 0.3 * np.sin(k * i * 0.25 + self.dim * 0.15)
                tunneling += (modulator / (k**2.2 + 0.3)) * np.exp(-k * np.abs(xi)) * np.cos(k * xi + modulator * 0.4)
            
            # Adaptive energy landscape with multi-phase transitions
            phase_shift = 0.15 * np.sin(i * 0.35 + self.dim * 0.25)
            energy_factor = (1.0 + 
                           0.6 * np.sin(self.dim * 0.35 + i * 0.25 + phase_shift) + 
                           0.4 * np.cos(self.dim * 0.45 + i * 0.15 + phase_shift) +
                           0.3 * np.sin(self.dim * 0.65 + i * 0.35 + phase_shift))
            
            # Enhanced cross-dimensional entanglement with fractal coupling
            entanglement = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    # Fractal dimensionality in coupling strength
                    coupling_strength = 1.0 / (1.0 + (xi - x_norm[j])**2 + 0.15 * np.sin(i * j * 0.25))
                    entanglement += coupling_strength * np.sin(xi + x_norm[j] + 0.4 * np.cos(i + j))
            
            # Quantum interference terms with dynamic phase
            interference = 0.0
            for k in range(1, 10):
                phase = k * 0.45 + 0.25 * np.sin(i * 0.35 + k * 0.45)
                interference += (1.0 / k**1.7) * np.sin(k * xi + phase) * np.cos(k * x_norm[i % self.dim] + phase)
            
            # Combine all components with chaotic weighting
            weight = 1.0 + 0.4 * np.sin(i * 0.75 + self.dim * 0.25) * np.cos(self.dim * 0.35 + i * 0.45)
            result += weight * (energy_factor * oscillator + tunneling + 0.6 * entanglement + 0.4 * interference)**2
            
        # Add chaotic global scaling factor
        chaotic_correction = 1.0 + 0.25 * np.sin(np.log(self.dim + 1) * 3.2 + self.dim * 0.15) + 0.15 * np.cos(np.log(self.dim + 1) * 2.2)
        return chaotic_correction * result / self.dim