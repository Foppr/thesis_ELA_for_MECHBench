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
            
            # Enhanced quantum harmonic oscillator potential with entanglement
            oscillator = np.sin(xi)**2 + 0.5 * np.cos(2 * xi) + 0.3 * np.sin(3 * xi) + 0.1 * np.sin(4 * xi)
            
            # Modified probabilistic tunneling wells with enhanced quantum-like behavior
            tunneling = 0.0
            for k in range(1, 15):
                tunneling += (1.0 / k**2.8) * np.exp(-k * np.abs(xi)) * np.cos(k * xi + 0.5 * i + 0.1 * np.sin(k * xi))
            
            # Enhanced adaptive energy landscape with phase transitions
            energy_factor = 1.0 + 0.7 * np.sin(self.dim * 0.35 + i * 0.25) + 0.4 * np.cos(self.dim * 0.45 + i * 0.15) + 0.2 * np.sin(self.dim * 0.6 + i * 0.3) + 0.15 * np.sin(xi * 7.0)
            
            # Improved cross-dimensional entanglement term with fractal interference
            entanglement = 0.0
            for j in range(max(0, i-4), min(self.dim, i+5)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    entanglement += (1.0 / (1.0 + distance**3.0)) * np.sin(xi + x_norm[j] + 0.3 * np.sin(i * j) + 0.1 * np.cos(xi * x_norm[j]) + 0.05 * np.sin(xi * x_norm[j] * 10.0))
            
            # Enhanced quantum-inspired weighting with additional dimension-dependent factor
            weight = 1.0 + 0.3 * np.sin(i * 0.6) * np.cos(self.dim * 0.12) + 0.15 * np.cos(i * 0.4) + 0.1 * np.sin(xi * 5.0)
            
            # Add hyperchaotic resonance term with improved complexity
            resonance = 0.2 * np.sin(13.0 * xi + 0.5 * i) * np.cos(7.0 * xi - 0.3 * i) + 0.1 * np.sin(23.0 * xi) + 0.05 * np.sin(31.0 * xi + 0.2 * i**1.5)
            
            # Add improved cross-dimensional coupling with more complex interaction
            cross_coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    cross_coupling += (1.0 / (1.0 + np.abs(xi - x_norm[j])**2.5)) * np.cos(xi * x_norm[j] * 3.0 + 0.1 * np.sin(i + j))
            
            result += weight * (energy_factor * oscillator + tunneling + 0.7 * entanglement + resonance + 0.3 * cross_coupling)**2
            
        # Improved global scaling factor with dimension-dependent quantum correction
        quantum_correction = 1.0 + 0.15 * np.sin(np.log(self.dim + 1) * 2.2) + 0.05 * np.cos(np.log(self.dim + 1) * 3.1) + 0.08 * np.sin(self.dim * 0.8)
        
        # Add multi-scale fractal interference pattern with enhanced complexity
        fractal_pattern = 0.0
        for scale in [2, 4, 8, 16]:
            fractal_pattern += 0.1 * np.sin(self.dim * 0.5 + scale * np.sum(np.sin(x_norm * scale))) / scale
            
        # Add improved dimensionality scaling and normalization
        normalized_result = result / self.dim
        
        return (quantum_correction * normalized_result) * (1.0 + fractal_pattern)