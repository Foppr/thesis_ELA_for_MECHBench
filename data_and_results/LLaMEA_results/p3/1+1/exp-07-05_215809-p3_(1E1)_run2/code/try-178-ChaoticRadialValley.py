import numpy as np

class ChaoticRadialValley:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        # Normalize input to [-pi, pi] range
        x_norm = (x - self.bounds.lb) * (2 * np.pi) / (self.bounds.ub - self.bounds.lb) - np.pi
        
        # Radial component with chaotic modulation
        r = np.sqrt(np.sum(x**2))
        radial = 0.5 * r * np.sin(3 * r) * np.cos(2 * r) + 0.3 * np.sin(7 * r) * np.cos(5 * r)
        
        # Chaotic sine-wave interactions between dimensions
        chaotic_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic coupling with non-linear interaction
                coupling = np.sin(x[i] * x[j]) * np.cos(x[i] + x[j]) * np.sin(x[i] - x[j])
                chaotic_interaction += 0.1 * coupling * np.sin(i * 0.7 + j * 0.9)
                
        # Adaptive conditioning based on position
        conditioning = 0.0
        for i in range(self.dim):
            # Dynamic scaling factor based on position
            scale = 1.0 + 0.5 * np.sin(x[i] * 0.5) * np.cos(x[i] * 0.3)
            conditioning += scale * x[i]**2
            
        # Multi-modal structure with asymmetric peaks
        multimodal = 0.0
        for i in range(self.dim):
            # Asymmetric peaks with varying heights and widths
            peak1 = 0.4 * np.exp(-0.5 * (x[i] - 1.5)**2) * np.sin(3 * x[i])
            peak2 = 0.3 * np.exp(-0.5 * (x[i] + 2.0)**2) * np.cos(2 * x[i])
            peak3 = 0.2 * np.exp(-0.5 * (x[i] - 3.0)**2) * np.sin(5 * x[i])
            multimodal += peak1 + peak2 + peak3
            
        # Fractal-like structure with recursive harmonic terms
        fractal = 0.0
        for i in range(self.dim):
            # Nested harmonic terms with decreasing amplitudes
            term = 0.1 * np.sin(11 * x[i]) * np.cos(13 * x[i]) * np.sin(17 * x[i]) * np.cos(19 * x[i])
            fractal += term
            
        # Symmetry breaking with directional bias
        symmetry_break = 0.0
        for i in range(self.dim):
            # Directional bias that varies with dimension
            bias = 0.2 * np.sin(i * 0.8) + 0.1 * np.cos(i * 1.2)
            symmetry_break += bias * x[i]**3
            
        # Combined fitness function
        f = radial + chaotic_interaction + conditioning + multimodal + fractal + symmetry_break
        
        # Add higher-order polynomial terms for additional curvature
        f += 0.1 * np.sum(x**4) + 0.05 * np.sum(x**6)
        
        # Final scaling to ensure proper fitness landscape characteristics
        f *= 1.0 + 0.1 * np.sum(np.abs(x))
        
        return f