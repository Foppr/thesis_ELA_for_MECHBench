import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator components with fractal coupling
        quantum_harmonic = 0
        for i in range(self.dim):
            freq = 1.0 + 0.3 * np.sin(0.5 * x[i] + self.dim * 0.2)
            phase = 0.4 * np.cos(0.7 * x[i])
            quantum_harmonic += freq * (x[i]**2) * np.exp(-0.15 * x[i]**2) * np.cos(phase)
        
        # Radial basis function ensemble with fractal adaptive widths
        rbf_ensemble = 0
        for i in range(self.dim):
            width = 1.0 + 0.4 * np.sin(0.6 * x[i] + self.dim * 0.1)
            center = 2.5 * np.cos(0.4 * x[i] + self.dim * 0.3)
            rbf_ensemble += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Time-varying spectral filter with dynamic frequency modulation and fractal scaling
        spectral_filter = 0
        for i in range(self.dim):
            freq_mod = 1.0 + 0.5 * np.sin(0.3 * x[i] + self.dim * 0.15)
            spectral_filter += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]**2) * np.exp(-0.08 * x[i]**2)
        
        # Mixed conditioning with fractal scaling
        conditioning = 1.0 + 0.3 * np.sin(self.dim * 0.4) + 0.2 * np.cos(self.dim * 0.5)
        
        # Cross-dimensional interactions with fractal coupling
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                poly_term = (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
                cross_coupling += poly_term
        
        # Asymmetric multimodal structure with fractal sine-cosine combinations
        multimodal_structure = 0
        for i in range(self.dim):
            term1 = np.sin(2.5 * x[i]) * np.cos(3.5 * x[i])
            term2 = np.sin(2.0 * x[i]**2) * np.cos(3.0 * x[i])
            multimodal_structure += term1 + term2
        
        # Fractal-based adaptive weights
        fractal_weight = 1.0 + 0.1 * np.sin(self.dim * 0.6)
        
        # Combine all components with optimized weights
        return conditioning * fractal_weight * (0.35 * quantum_harmonic + 0.2 * rbf_ensemble + 
                              0.25 * spectral_filter + 0.15 * cross_coupling + 0.05 * multimodal_structure)