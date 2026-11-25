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
            
            # Enhanced multi-scale quantum harmonic oscillator with fractal frequency modulation
            freq = 1.0 + 0.4 * np.sin(i * 0.8) * np.cos(i * 0.3) + 0.25 * np.sin(i * 1.2)
            oscillator = (np.sin(freq * xi)**2 + 
                         0.6 * np.cos(2 * freq * xi) + 
                         0.4 * np.sin(3 * freq * xi) + 
                         0.2 * np.cos(5 * freq * xi) + 
                         0.1 * np.sin(7 * freq * xi))
            
            # Enhanced probabilistic tunneling wells with hyper-chaotic parameters
            tunneling = 0.0
            for k in range(1, 12):
                # Hyper-chaotic modulation of tunneling parameters
                modulator = 1.0 + 0.3 * np.sin(k * i * 0.4 + self.dim * 0.15) * np.cos(k * i * 0.2)
                tunneling += (modulator / (k**2.2 + 0.3)) * np.exp(-k * np.abs(xi)) * np.sin(k * xi + modulator * 0.6)
            
            # Adaptive energy landscape with multi-phase transitions and fractal dynamics
            phase_shift = 0.15 * np.sin(i * 0.45 + self.dim * 0.25) * np.cos(i * 0.3)
            energy_factor = (1.0 + 
                           0.6 * np.sin(self.dim * 0.35 + i * 0.25 + phase_shift) + 
                           0.4 * np.cos(self.dim * 0.45 + i * 0.15 + phase_shift) +
                           0.3 * np.sin(self.dim * 0.65 + i * 0.35 + phase_shift) +
                           0.2 * np.cos(self.dim * 0.75 + i * 0.25 + phase_shift))
            
            # Enhanced cross-dimensional entanglement with fractal coupling and dynamic strength
            entanglement = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    # Fractal dimensionality in coupling strength with hyperbolic modulation
                    coupling_strength = 1.0 / (1.0 + (xi - x_norm[j])**2 + 0.15 * np.sin(i * j * 0.25) * np.cos(i * j * 0.1))
                    entanglement += coupling_strength * np.sin(xi + x_norm[j] + 0.4 * np.cos(i + j) * np.sin(i * j * 0.15))
            
            # Enhanced quantum interference terms with dynamic phase and multi-fractal structure
            interference = 0.0
            for k in range(1, 10):
                phase = k * 0.6 + 0.3 * np.sin(i * 0.35 + k * 0.45) * np.cos(k * 0.2)
                interference += (1.0 / k**1.7) * np.sin(k * xi + phase) * np.cos(k * x_norm[i % self.dim] + phase) * np.sin(k * 0.5 + i * 0.3)
            
            # Combine all components with enhanced chaotic weighting
            weight = 1.0 + 0.4 * np.sin(i * 0.75 + self.dim * 0.25) * np.cos(self.dim * 0.35 + i * 0.45)
            result += weight * (energy_factor * oscillator + tunneling + 0.6 * entanglement + 0.4 * interference)**2
            
        # Add hyper-chaotic global scaling factor with fractal modulation
        chaotic_correction = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 3.5 + self.dim * 0.15) * np.cos(np.log(self.dim + 1) * 2.5) + 0.15 * np.sin(self.dim * 0.3)
        return chaotic_correction * result / self.dim