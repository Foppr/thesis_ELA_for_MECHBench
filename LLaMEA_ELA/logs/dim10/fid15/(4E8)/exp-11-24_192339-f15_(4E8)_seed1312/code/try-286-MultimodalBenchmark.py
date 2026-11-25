import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced quantum harmonic oscillator components with chaotic modulation
        quantum_harmonic = 0
        for i in range(self.dim):
            freq = 1.3 + 0.5 * np.sin(0.7 * x[i] + self.dim * 0.3)
            phase = 0.6 * np.cos(0.9 * x[i] + 0.4 * self.dim)
            quantum_harmonic += freq * (x[i]**2) * np.exp(-0.25 * x[i]**2) * np.cos(phase)
        
        # Enhanced radial basis function ensemble with dynamic widths and centers
        rbf_ensemble = 0
        for i in range(self.dim):
            width = 1.6 + 0.4 * np.sin(0.8 * x[i] + self.dim * 0.25)
            center = 3.5 * np.cos(0.6 * x[i] + self.dim * 0.45)
            rbf_ensemble += np.exp(-0.35 * ((x[i] - center) / width)**2)
        
        # Enhanced time-varying spectral filter with chaotic frequency modulation
        spectral_filter = 0
        for i in range(self.dim):
            freq_mod = 1.6 + 0.7 * np.sin(0.5 * x[i] + self.dim * 0.25)
            spectral_filter += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]**2) * np.exp(-0.12 * x[i]**2)
        
        # Enhanced mixed conditioning with dynamic scaling factors
        conditioning = 1.6 + 0.5 * np.sin(self.dim * 0.55) + 0.4 * np.cos(self.dim * 0.65)
        
        # Enhanced cross-dimensional interactions with adaptive coupling
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                poly_term = (x[i]**2 + x[j]**2) * np.exp(-0.2 * (x[i] - x[j])**2)
                cross_coupling += poly_term
        
        # Enhanced asymmetric multimodal structure with combined trigonometric functions
        multimodal_structure = 0
        for i in range(self.dim):
            term1 = np.sin(3.5 * x[i]) * np.cos(4.5 * x[i])
            term2 = np.sin(3.0 * x[i]**2) * np.cos(4.0 * x[i])
            term3 = np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]**2)
            multimodal_structure += term1 + term2 + term3
        
        # Enhanced fractal-based adaptive weights
        fractal_weight = 1.3 + 0.3 * np.sin(self.dim * 0.75)
        
        # Combine all components with optimized weights for better fitness
        return conditioning * fractal_weight * (0.45 * quantum_harmonic + 0.3 * rbf_ensemble + 
                              0.25 * spectral_filter + 0.15 * cross_coupling + 0.05 * multimodal_structure)