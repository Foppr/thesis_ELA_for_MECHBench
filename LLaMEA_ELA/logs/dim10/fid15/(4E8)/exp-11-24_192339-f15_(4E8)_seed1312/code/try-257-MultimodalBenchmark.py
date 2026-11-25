import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-cosine interactions with quaternion-inspired coupling
        chaotic_interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Quaternion-like coupling with chaotic modulation
                q_real = np.sin(x[i]) * np.cos(x[j])
                q_imag = np.cos(0.3 * x[i]) * np.sin(0.7 * x[j])
                q_j = np.sin(0.5 * x[i]) * np.cos(0.4 * x[j])
                q_k = np.cos(0.6 * x[i]) * np.sin(0.8 * x[j])
                coupling = (q_real**2 + q_imag**2 + q_j**2 + q_k**2) * np.exp(-0.1 * (x[i] - x[j])**2)
                chaotic_interaction += coupling
        
        # Fractal-based radial basis functions with dynamic scaling
        fractal_rbf = 0
        for i in range(self.dim):
            # Fractal-like scaling with recursive dimensionality
            scale = 1.0 + 0.3 * np.sin(0.2 * x[i] * (self.dim + 1))
            width = 0.1 + 0.4 * np.cos(0.5 * x[i])
            center = 2.0 * np.sin(0.4 * x[i]) + 1.0 * np.cos(0.6 * x[i])
            fractal_rbf += scale * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Time-varying harmonic couplings with adaptive frequencies
        adaptive_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive frequency modulation based on global dimension
                freq_i = 1.0 + 0.5 * np.sin(0.3 * x[i] + 0.2 * self.dim)
                freq_j = 1.0 + 0.4 * np.cos(0.4 * x[j] - 0.1 * self.dim)
                adaptive_coupling += np.sin(freq_i * x[i] + freq_j * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
        
        # Spherical harmonic interactions with mixed conditioning
        spherical_harmonic = 0
        for i in range(self.dim):
            # Spherical harmonic terms with varying angular dependencies
            amp = 1.0 + 0.2 * np.sin(0.5 * x[i])
            freq = 1.5 + 0.3 * np.cos(0.4 * x[i])
            spherical_harmonic += amp * np.sin(freq * x[i]) * np.exp(-0.01 * x[i]**2)
        
        # Asymmetric exponential landscape with cross-dimensional coupling
        asym_exp = 0
        for i in range(self.dim):
            # Asymmetric exponential terms with dynamic scaling
            asym_factor = 1.0 + 0.4 * np.sin(0.3 * x[i] + 0.1 * self.dim)
            asym_exp += asym_factor * np.exp(-0.3 * x[i]**2) * (1.0 + 0.3 * np.cos(0.5 * x[i]))
        
        # Global conditioning with chaotic dimension scaling
        cond_factor = 1.0 + 0.5 * np.sin(0.4 * self.dim + 0.2 * np.sum(x)) + 0.3 * np.cos(0.6 * self.dim)
        
        # Combine all components with optimized weights
        return cond_factor * (0.3 * chaotic_interaction + 0.25 * fractal_rbf + 
                             0.2 * adaptive_coupling + 0.15 * spherical_harmonic + 0.1 * asym_exp)