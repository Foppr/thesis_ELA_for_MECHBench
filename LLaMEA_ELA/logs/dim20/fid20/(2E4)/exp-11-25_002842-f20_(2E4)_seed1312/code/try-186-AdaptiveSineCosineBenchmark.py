import numpy as np

class AdaptiveSineCosineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize parameters for adaptive frequency modulation
        self.freq_modulators = np.random.uniform(0.3, 2.5, dim)
        self.phase_shifts = np.random.uniform(0, 2*np.pi, dim)
        self.amplitude_factors = np.random.uniform(0.4, 1.6, dim)
        self.cross_coupling_strengths = np.random.uniform(0.1, 1.2, (dim, dim))
        # Additional parameters for enhanced complexity
        self.nonlinear_exponents = np.random.uniform(1.0, 3.5, dim)
        self.damping_factors = np.random.uniform(0.05, 0.6, dim)
        self.resonance_centers = np.random.uniform(-2.5, 2.5, dim)
        self.harmonic_coefficients = np.random.uniform(0.05, 0.6, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base sine-cosine components with adaptive frequencies
        base_terms = 0.0
        for i in range(self.dim):
            freq = self.freq_modulators[i] * (1 + 0.4 * np.sin(x_norm[i]))
            base_terms += (self.amplitude_factors[i] * 
                          np.sin(freq * x_norm[i] + self.phase_shifts[i]) * 
                          np.cos(freq * x_norm[i] + self.phase_shifts[i]))
        
        # Nonlinear transformation with adaptive exponents
        nonlinear_terms = 0.0
        for i in range(self.dim):
            nonlinear_terms += (np.abs(x_norm[i])**self.nonlinear_exponents[i] * 
                              np.sin(x_norm[i]) * np.cos(x_norm[i]))
        
        # Cross-dimensional coupling with adaptive weights
        coupling_terms = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_terms += (self.cross_coupling_strengths[i, j] * 
                                     np.sin(x_norm[i] - x_norm[j]) * 
                                     np.cos(x_norm[i] + x_norm[j]))
        
        # Resonance effects with adaptive centers
        resonance_terms = 0.0
        for i in range(self.dim):
            resonance_terms += (np.exp(-0.5 * ((x_norm[i] - self.resonance_centers[i])**2) / 
                                    (0.4 + 0.2 * np.abs(x_norm[i]))) * 
                              np.sin(3 * x_norm[i]))
        
        # Damping effects
        damping_terms = 0.0
        for i in range(self.dim):
            damping_terms += self.damping_factors[i] * np.exp(-x_norm[i]**2)
        
        # Additional harmonic components
        harmonic_terms = 0.0
        for i in range(self.dim):
            harmonic_terms += self.harmonic_coefficients[i] * np.sin(4 * x_norm[i]) * np.cos(3 * x_norm[i])
        
        # Combine all terms with optimized weights
        return (0.25 * base_terms + 
                0.3 * nonlinear_terms + 
                0.2 * coupling_terms + 
                0.15 * resonance_terms + 
                0.03 * damping_terms + 
                0.07 * harmonic_terms)