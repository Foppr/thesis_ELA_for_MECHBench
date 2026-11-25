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
            freq = 1.2 + 0.4 * np.sin(0.6 * x[i] + self.dim * 0.25)
            phase = 0.5 * np.cos(0.8 * x[i] + 0.3 * self.dim)
            quantum_harmonic += freq * (x[i]**2) * np.exp(-0.2 * x[i]**2) * np.cos(phase)
        
        # Perturbed radial basis function ensemble with dynamic widths and centers
        rbf_ensemble = 0
        for i in range(self.dim):
            width = 1.5 + 0.3 * np.sin(0.7 * x[i] + self.dim * 0.2) + 0.1 * np.sin(3.0 * x[i])
            center = 3.0 * np.cos(0.5 * x[i] + self.dim * 0.4) + 0.2 * np.cos(2.0 * x[i])
            rbf_ensemble += np.exp(-0.3 * ((x[i] - center) / width)**2)
        
        # Enhanced time-varying spectral filter with chaotic frequency modulation
        spectral_filter = 0
        for i in range(self.dim):
            freq_mod = 1.5 + 0.6 * np.sin(0.4 * x[i] + self.dim * 0.2) + 0.3 * np.sin(1.2 * x[i])
            spectral_filter += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i]**2) * np.exp(-0.1 * x[i]**2)
        
        # Enhanced mixed conditioning with dynamic scaling factors
        conditioning = 1.5 + 0.4 * np.sin(self.dim * 0.5) + 0.3 * np.cos(self.dim * 0.6) + 0.2 * np.sin(0.8 * self.dim)
        
        # Enhanced cross-dimensional interactions with adaptive coupling
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                poly_term = (x[i]**2 + x[j]**2) * np.exp(-0.15 * (x[i] - x[j])**2)
                cross_coupling += poly_term
        
        # Enhanced asymmetric multimodal structure with combined trigonometric functions
        multimodal_structure = 0
        for i in range(self.dim):
            term1 = np.sin(3.0 * x[i]) * np.cos(4.0 * x[i])
            term2 = np.sin(2.5 * x[i]**2) * np.cos(3.5 * x[i])
            term3 = np.sin(1.5 * x[i]) * np.cos(2.5 * x[i]**2)
            multimodal_structure += term1 + term2 + term3
        
        # Enhanced fractal-based adaptive weights
        fractal_weight = 1.2 + 0.2 * np.sin(self.dim * 0.7) + 0.1 * np.cos(1.5 * self.dim)
        
        # Add chaotic phase shift modulation to the entire function
        chaos_mod = 1.0 + 0.1 * np.sin(2.0 * np.sum(x)) + 0.05 * np.cos(3.0 * np.sum(x)**2)
        
        # Combine all components with optimized weights for better fitness
        return chaos_mod * conditioning * fractal_weight * (0.4 * quantum_harmonic + 0.25 * rbf_ensemble + 
                              0.2 * spectral_filter + 0.1 * cross_coupling + 0.05 * multimodal_structure)