import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with varying centers and widths
        rbf = 0
        centers = np.linspace(-1, 1, min(5, self.dim))
        widths = np.logspace(-1, 1, min(5, self.dim))
        for i, (c, w) in enumerate(zip(centers, widths)):
            if i < len(x_norm):
                rbf += np.exp(-0.5 * ((x_norm[i] - c) / w)**2)
        
        # Sinusoidal modulation with varying frequencies and amplitudes
        sin_mod = 0
        freqs = np.linspace(2.0, 8.0, min(6, self.dim))  # Increased frequencies for more sensitivity
        amps = np.logspace(0.5, 2.5, min(6, self.dim))   # Adjusted amplitudes
        for i, (f, a) in enumerate(zip(freqs, amps)):
            if i < len(x_norm):
                sin_mod += a * np.sin(f * np.pi * x_norm[i])
        
        # Cross-dimensional interaction terms with modified polynomial coupling
        cross_terms = 0
        for i in range(self.dim - 1):
            for j in range(i + 1, self.dim):
                # Modified coupling exponents for increased complexity and nonlinearity
                cross_terms += (x_norm[i]**4 + x_norm[j]**4) * np.sin(np.pi * (x_norm[i] - x_norm[j]))
        
        # Asymmetric saddle-point structure with exponential decay
        saddle = 0
        for i in range(self.dim - 1):
            # Changed from quartic to quintic terms for more complex curvature and sharper gradients
            saddle += (x_norm[i]**5 - x_norm[i+1]**5) * np.exp(-0.5 * (x_norm[i] + x_norm[i+1])**2)
        
        # Multi-scale harmonic component with varying phase shifts
        harmonic = 0
        scales = [0.2, 0.8, 1.5]  # Adjusted scales for different harmonic contributions
        for s in scales:
            harmonic += np.sum(np.sin(s * np.pi * x_norm) * np.cos(s * np.pi * x_norm))
        
        # Add a chaotic modulation component to increase landscape complexity
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(13.0 * x_norm[i]) * np.cos(7.0 * x_norm[i])
        
        # Combined function with adaptive scaling and noise
        result = rbf + sin_mod + cross_terms + saddle + harmonic + chaotic
        
        # Add controlled noise for robustness
        noise = 0.015 * np.random.rand() * (1.0 + 0.15 * np.abs(np.mean(x_norm)))
        
        return result + noise