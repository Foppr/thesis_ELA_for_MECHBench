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
            
            # Enhanced quantum harmonic oscillator with multi-frequency harmonics and chaotic modulation
            oscillator = (np.sin(xi)**2 + 
                         0.5 * np.cos(2 * xi) + 
                         0.3 * np.sin(3 * xi) + 
                         0.1 * np.sin(5 * xi) + 
                         0.05 * np.cos(7 * xi) +
                         0.02 * np.sin(11 * xi + np.sum(x_norm[:i+1]) if i > 0 else 0))
            
            # Multi-scale probabilistic tunneling wells with varying decay rates and quantum interference
            tunneling = 0.0
            for k in range(1, 15):
                decay_rate = 0.5 + 0.3 * np.sin(i * 0.7 + k * 0.3 + np.cos(xi))
                tunneling += (1.0 / k**2.8) * np.exp(-k * decay_rate * np.abs(xi)) * np.cos(k * xi + k * 0.2 + np.sin(k * xi))
            
            # Dynamic phase transitions with time-varying energy factors and fractal scaling
            energy_factor = (1.0 + 
                           0.5 * np.sin(self.dim * 0.3 + i * 0.2) + 
                           0.3 * np.cos(self.dim * 0.4 + i * 0.1) +
                           0.2 * np.sin(self.dim * 0.6 + i * 0.4 + np.sum(x_norm[:i+1]) if i > 0 else 0) +
                           0.1 * np.cos(np.sum(x_norm**2) * 0.5))
            
            # Fractal cross-dimensional entanglement with self-similar patterns and chaotic coupling
            entanglement = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    # Fractal scaling factor with chaotic modulation
                    fractal_scale = 1.0 + 0.3 * np.sin(np.log(distance + 1) * 3.0 + np.cos(xi + x_norm[j]))
                    entanglement += (fractal_scale / (1.0 + distance**2.5)) * np.sin(xi + x_norm[j] + 0.5 * np.cos(i + j + np.sin(xi * x_norm[j])))
            
            # Add quantum interference terms with dynamic phase shifts and chaotic phase modulation
            interference = 0.0
            for k in range(1, 12):
                phase_shift = 0.3 * np.sin(i * 0.4 + k * 0.2 + self.dim * 0.1 + np.cos(k * xi))
                interference += (1.0 / k**2.1) * np.sin(k * xi + phase_shift) * np.cos(k * x_norm[min(self.dim-1, i+k)] if i+k < self.dim else 0)
            
            # Combine all components with enhanced quantum-inspired weighting
            weight = 1.0 + 0.3 * np.sin(i * 0.5 + np.cos(xi)) * np.cos(self.dim * 0.1 + np.sum(x_norm[:i+1]) if i > 0 else 0)
            
            # Add chaotic amplification factor with dynamic modulation
            chaos_factor = 1.0 + 0.2 * np.sin(np.sum(x_norm)**2 + i * 0.3 + np.cos(xi))
            
            result += weight * chaos_factor * (energy_factor * oscillator + tunneling + 0.5 * entanglement + 0.3 * interference)**2
            
        # Add global scaling factor with enhanced dimension-dependent quantum correction
        quantum_correction = 1.0 + 0.2 * np.sin(np.log(self.dim + 1) * 3.0) + 0.1 * np.cos(np.log(self.dim + 1) * 5.0) + 0.05 * np.sin(np.sum(x_norm**3))
        
        # Add hyperchaotic modulation based on all dimensions with fractal enhancement
        hyperchaos = 1.0 + 0.15 * np.sin(np.sum(x_norm**2) * 2.0 + self.dim * 0.5 + np.cos(np.sum(x_norm)))
        
        return quantum_correction * hyperchaos * result / self.dim