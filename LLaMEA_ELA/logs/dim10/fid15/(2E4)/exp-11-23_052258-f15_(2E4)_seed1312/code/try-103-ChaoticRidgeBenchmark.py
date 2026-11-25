import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient component with logistic map modulation
        chaotic_term = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            xi = x[i]
            # Logistic map for chaotic behavior
            chaos = np.sin(r * xi * (1 - xi)) if i == 0 else np.sin(r * x[i-1] * (1 - x[i-1]))
            chaotic_term += xi**2 * np.exp(-0.1 * xi**2) * chaos
        
        # Adaptive ridge structure with dimension-dependent scaling
        ridge_term = 0.0
        for i in range(self.dim):
            ridge_height = 1.5 + 0.5 * np.sin(0.3 * i)
            ridge_width = 0.8 + 0.2 * np.cos(0.2 * i)
            ridge_term += ridge_height * np.exp(-0.5 * ((x[i] - 0.5 * np.sin(i)) / ridge_width)**2)
        
        # Spectral peak interactions with frequency modulation
        spectral_term = 0.0
        for i in range(self.dim):
            freq = 2.0 + 0.8 * np.sin(0.1 * i)
            amp = 1.2 + 0.3 * np.cos(0.2 * i)
            spectral_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.7)
        
        # Cross-dimensional coupling with dynamic weights
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 0.5 + 0.3 * np.sin(0.2 * (i + j))
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                cross_term += weight * np.exp(-dist**2) * np.sin(0.5 * (x[i] + x[j]))
        
        # Multi-scale harmonic with time-varying amplitudes
        harmonic_term = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.4 * np.sin(0.1 * i)
            freq = 1.5 + 0.6 * np.cos(0.2 * i)
            harmonic_term += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.3)
        
        # Asymmetric multimodal structure with dynamic peak positions
        modal_term = 0.0
        for i in range(self.dim):
            peak_pos = 2.5 * np.sin(0.4 * i) + 0.8 * np.cos(0.3 * i)
            modal_term += np.exp(-0.5 * ((x[i] - peak_pos) / 0.6)**2) * np.sin(2.0 * x[i])
        
        # Combined function with normalization and scaling
        total = (chaotic_term + ridge_term + spectral_term + cross_term + 
                harmonic_term + modal_term)
        
        return total