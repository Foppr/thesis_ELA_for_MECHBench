import numpy as np

class NestedEllipticSpectralBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Nested elliptic valley structure with varying eccentricity
        f1 = 0.0
        for i in range(self.dim):
            # Elliptic valley with adaptive eccentricity
            eccentricity = 1.0 + 0.5 * np.sin(0.3 * i + 0.2 * np.sum(x**2))
            f1 += (x[i]**2 / (1.0 + 0.3 * eccentricity)) + 0.5 * np.cos(eccentricity * x[i])
            
        # Adaptive gradient steering with spectral coupling
        f2 = 0.0
        for i in range(self.dim):
            # Spectral harmonic components with adaptive weights
            weight = 1.0 + 0.4 * np.sin(0.5 * i + 0.3 * np.sum(x**2))
            f2 += weight * np.sin(2.0 * x[i] + 0.5 * np.cos(i))**2
            
        # Multi-scale harmonic coupling with phase modulation
        f3 = 0.0
        for i in range(self.dim):
            coupling_sum = 0.0
            for j in range(self.dim):
                if i != j:
                    # Phase-modulated coupling strength
                    phase = 0.4 * np.sin(0.6 * (i - j) + 0.3 * np.sum(x**2))
                    coupling = 1.0 + 0.3 * np.cos(phase)
                    coupling_sum += coupling * np.cos(x[i] - x[j])**2
            f3 += coupling_sum
            
        # Nested harmonic resonance with frequency modulation
        f4 = 0.0
        for i in range(self.dim):
            # Frequency modulation based on radial distance and dimension
            freq_mod = 1.5 + 0.8 * np.sin(0.7 * i + 0.4 * np.sqrt(np.sum(x**2)))
            f4 += np.sin(freq_mod * x[i] + 0.3 * np.cos(i))**3
            
        # Adaptive elliptic conditioning with chaotic modulation
        f5 = 0.0
        r = np.sqrt(np.sum(x**2))
        for i in range(self.dim):
            # Chaotic parameter modulation based on radial distance
            param_mod = 1.0 + 0.6 * np.sin(0.4 * i + 0.3 * r)
            f5 += (x[i]**2 / (1.0 + 0.2 * r**2)) * param_mod
            
        # Boundary interaction with spectral decay
        f6 = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.0:
                boundary_decay = 1.0 + 0.3 * np.sin(0.5 * i + 0.2 * r)
                f6 += boundary_decay * (np.exp(-0.3 * (np.abs(x[i]) - 4.0)) + 0.5 * np.exp(-0.6 * (np.abs(x[i]) - 4.0)))
                
        # Multi-dimensional harmonic interactions with adaptive coupling
        f7 = 0.0
        for i in range(self.dim):
            harmonic_sum = 0.0
            for j in range(i+1, self.dim):
                # Adaptive coupling coefficient based on position and dimension
                coeff = 1.0 + 0.4 * np.sin(0.5 * (i + j) + 0.3 * r)
                harmonic_interaction = coeff * np.sin(x[i] + x[j])**2 * np.cos(x[i] - x[j])**2
                harmonic_sum += harmonic_interaction
            f7 += harmonic_sum
            
        # Fractal-like spectral structure with nested harmonics
        f8 = 0.0
        for i in range(self.dim):
            # Nested harmonic components with varying scales
            scale = 1.0 + 0.5 * np.sin(0.6 * i + 0.4 * r)
            f8 += scale * np.cos(3.0 * x[i] / (1.0 + 0.2 * r))**2
            
        # Chaotic gradient steering with multi-scale harmonic components
        f9 = 0.0
        for i in range(self.dim):
            # Multi-scale frequency components with chaotic phase relationships
            freq_component = 2.0 + 0.7 * np.sin(0.8 * i + 0.5 * r)
            phase_component = 0.5 * np.cos(0.6 * i + 0.3 * r) + 0.3 * np.sin(r)
            f9 += np.sin(freq_component * x[i] + phase_component)**4
            
        # Adaptive spectral conditioning with elliptic parameters
        f10 = 0.0
        for i in range(self.dim):
            # Elliptic parameter with adaptive frequency
            ell_param = 1.0 + 0.8 * np.sin(0.7 * i + 0.4 * r)
            f10 += ell_param * np.exp(-0.15 * x[i]**2) * np.cos(2.0 * x[i])**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + f10