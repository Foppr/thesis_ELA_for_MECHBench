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
            
            # Enhanced quantum harmonic oscillator with multi-frequency harmonics
            oscillator = (np.sin(xi)**2 + 
                         0.5 * np.cos(2 * xi) + 
                         0.3 * np.sin(3 * xi) + 
                         0.1 * np.sin(5 * xi) + 
                         0.05 * np.cos(7 * xi))
            
            # Multi-scale probabilistic tunneling wells with varying decay rates
            tunneling = 0.0
            for k in range(1, 10):
                decay_rate = 0.5 + 0.3 * np.sin(i * 0.7 + k * 0.3)
                tunneling += (1.0 / k**2.5) * np.exp(-k * decay_rate * np.abs(xi)) * np.cos(k * xi + k * 0.2)
            
            # Dynamic phase transitions with time-varying energy factors
            energy_factor = (1.0 + 
                           0.5 * np.sin(self.dim * 0.3 + i * 0.2) + 
                           0.3 * np.cos(self.dim * 0.4 + i * 0.1) +
                           0.2 * np.sin(self.dim * 0.6 + i * 0.4 + np.sum(x_norm[:i+1]) if i > 0 else 0))
            
            # Fractal cross-dimensional entanglement with self-similar patterns
            entanglement = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    # Fractal scaling factor
                    fractal_scale = 1.0 + 0.3 * np.sin(np.log(distance + 1) * 3.0)
                    entanglement += (fractal_scale / (1.0 + distance**2)) * np.sin(xi + x_norm[j] + 0.5 * np.cos(i + j))
            
            # Add quantum interference terms with dynamic phase shifts
            interference = 0.0
            for k in range(1, 8):
                phase_shift = 0.3 * np.sin(i * 0.4 + k * 0.2 + self.dim * 0.1)
                interference += (1.0 / k**1.8) * np.sin(k * xi + phase_shift) * np.cos(k * x_norm[min(self.dim-1, i+k)] if i+k < self.dim else 0)
            
            # Combine all components with enhanced quantum-inspired weighting
            weight = 1.0 + 0.3 * np.sin(i * 0.5) * np.cos(self.dim * 0.1 + np.sum(x_norm[:i+1]) if i > 0 else 0)
            
            # Add chaotic amplification factor
            chaos_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm)**2 + i * 0.3)
            
            result += weight * chaos_factor * (energy_factor * oscillator + tunneling + 0.5 * entanglement + 0.3 * interference)**2
            
        # Add global scaling factor with enhanced dimension-dependent quantum correction
        quantum_correction = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 3.0) + 0.1 * np.cos(np.log(self.dim + 1) * 5.0)
        
        # Add hyperchaotic modulation based on all dimensions
        hyperchaos = 1.0 + 0.15 * np.sin(np.sum(x_norm**2) * 2.0 + self.dim * 0.5)
        
        return quantum_correction * hyperchaos * result / self.dim