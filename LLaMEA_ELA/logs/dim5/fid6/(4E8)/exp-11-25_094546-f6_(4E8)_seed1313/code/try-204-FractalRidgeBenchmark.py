import numpy as np

class FractalRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        result = 0.0
        
        for i in range(self.dim):
            xi = x_norm[i]
            
            # Enhanced fractal ridge structure with quantum interference patterns
            ridge = 0.0
            for k in range(1, 8):
                scale = 2.0 ** (-k)
                freq = 2 ** k
                # Quantum-like interference term
                interference = np.sin(freq * xi + k * 0.5) * np.cos(freq * xi - k * 0.3)
                ridge += scale * interference
            
            # Adaptive curvature field with quantum entanglement scaling
            entanglement_factor = 1.0 + 0.6 * np.sin(self.dim * 0.3 + i * 0.4) * np.cos(i * 0.5)
            curvature = entanglement_factor * (1.0 + 0.4 * np.sin(xi * 3.0))
            
            # Cross-dimensional coupling with quantum tunneling effects
            coupling = 0.0
            for j in range(max(0, i-3), min(self.dim, i+4)):
                if i != j:
                    distance = np.abs(xi - x_norm[j])
                    # Quantum tunneling interaction
                    tunneling = np.exp(-distance**2 * 0.5) * np.sin(xi + x_norm[j] + 0.7 * np.cos(i + j))
                    coupling += tunneling
            
            # Multi-scale harmonic modulation with quantum phase shifts
            modulation = 1.0
            for k in range(1, 6):
                phase_shift = k * 0.3 + np.sin(i * 0.2)
                modulation *= (1.0 + 0.4 * np.sin(k * xi + phase_shift))
            
            # Add to result with quantum-adaptive weighting
            weight = 1.0 + 0.5 * np.sin(i * 0.6) * np.cos(self.dim * 0.2 + i * 0.3)
            
            # Apply quantum chaos amplification
            chaos_amp = 1.0 + 0.4 * np.sin(np.sum(x_norm**3) + i * 0.3) * np.cos(np.sum(x_norm**2) * 0.5)
            
            result += weight * chaos_amp * (curvature * ridge**3 + 0.3 * coupling)**2
            
        # Global quantum scaling with entanglement correction
        global_scale = 1.0 + 0.3 * np.sin(np.log(self.dim + 1) * 5.0)
        
        # Add quantum hyper-fractal modulation based on all dimensions
        hyper_fractal = 1.0 + 0.3 * np.sin(np.sum(np.abs(x_norm)) * 4.0 + self.dim * 0.4)
        
        # Add quantum phase transition factor
        phase_transition = 1.0 + 0.2 * np.sin(np.sum(x_norm**4) * 2.0)
        
        return global_scale * hyper_fractal * phase_transition * result / self.dim