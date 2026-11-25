import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spatiotemporal chaotic lattice with dynamic phase transitions
        lattice_energy = 0
        for i in range(self.dim):
            # Dynamic phase coupling with time-varying modulation
            phase_coupling = np.sin(2.0 * x[i] + 0.5 * np.sin(1.5 * x[i]) * self.dim)
            # Chaotic temporal modulation with fractal scaling
            temporal_mod = 1.0 + 0.3 * np.sin(0.8 * x[i] + 0.4 * np.cos(x[i]))
            lattice_energy += temporal_mod * (x[i]**2) * np.exp(-0.1 * x[i]**2) * phase_coupling
        
        # Multi-scale fractal interference patterns
        interference = 0
        for i in range(self.dim):
            scale1 = 2.0 + 1.5 * np.sin(0.7 * x[i] + self.dim * 0.3)
            scale2 = 1.5 + 0.8 * np.cos(0.9 * x[i] + self.dim * 0.4)
            interference += np.sin(scale1 * x[i]) * np.cos(scale2 * x[i]**2) * np.exp(-0.2 * x[i]**2)
        
        # Adaptive gradient coupling with dynamic scaling
        coupling = 0
        for i in range(self.dim):
            for j in range(max(0, i-2), min(i+2, self.dim)):  # Reduced coupling range
                # Adaptive coupling strength based on distance and dimensionality
                coupling_strength = 0.8 + 0.4 * np.sin(0.6 * (x[i] - x[j]) + self.dim * 0.2)
                coupling += coupling_strength * np.exp(-0.3 * (x[i] - x[j])**2) * (x[i]**2 + x[j]**2)
        
        # Multi-scale harmonic components with dynamic frequency modulation
        harmonic = 0
        for i in range(self.dim):
            freq1 = 2.5 + 1.2 * np.sin(0.6 * x[i] + self.dim * 0.35)
            freq2 = 1.8 + 0.9 * np.cos(0.7 * x[i] + self.dim * 0.4)
            harmonic += (freq1 * np.sin(freq1 * x[i]) + freq2 * np.cos(freq2 * x[i])) * np.exp(-0.15 * x[i]**2)
        
        # Fractal-based dimensionality scaling with added complexity
        fractal_dim = 1.2 + 0.3 * np.sin(self.dim * 0.8 + 0.2 * np.cos(x[0] if self.dim > 0 else 0)) + 0.1 * np.sin(3.0 * x[0] if self.dim > 0 else 0)
        
        # Combined landscape with optimized multi-scale weights
        return (0.4 * lattice_energy + 0.3 * interference + 
                0.2 * coupling + 0.1 * harmonic) * fractal_dim