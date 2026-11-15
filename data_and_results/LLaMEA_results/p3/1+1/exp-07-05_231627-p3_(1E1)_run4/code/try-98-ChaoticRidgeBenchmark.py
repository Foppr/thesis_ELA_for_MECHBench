import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] for better numerical stability
        x_norm = x / 5.0
        
        # Chaotic sine-wave component with varying frequencies and amplitudes
        chaotic_wave = np.sum(np.sin(10 * np.pi * x_norm) * np.cos(15 * np.pi * x_norm) * 
                              np.exp(-2 * np.abs(x_norm)) + 
                              np.sin(20 * np.pi * x_norm**3) * np.cos(25 * np.pi * x_norm**3) * 
                              np.exp(-3 * np.abs(x_norm)))
        
        # Polynomial ridge structure with varying curvature and multiple peaks
        ridge = np.sum((x_norm**6 - 15 * x_norm**4 + 75 * x_norm**2 - 125)**2)
        
        # Adaptive Gaussian peaks with dynamic widths and heights based on dimensionality
        peaks = 0
        num_peaks = min(20, 2 * self.dim)
        for i in range(num_peaks):
            center = np.full(self.dim, np.sin(i * np.pi / num_peaks) * 0.8)
            width = 0.5 + 0.3 * np.sin(i * np.pi / num_peaks)
            height = 1.5 + 0.5 * np.cos(i * np.pi / num_peaks)
            peaks += height * np.exp(-0.5 * np.sum(((x_norm - center) / width)**2))
        
        # Cross-dimensional interaction terms with chaotic modulation
        cross_terms = 0
        for i in range(self.dim - 1):
            cross_terms += (x_norm[i] - x_norm[i+1])**4 * np.sin(5 * np.pi * (x_norm[i] + x_norm[i+1]))
        
        # Fractional exponential component for ruggedness and non-linearity
        rugged = np.sum(np.abs(x_norm)**1.7 + 0.3 * np.sin(30 * np.pi * x_norm) * np.cos(20 * np.pi * x_norm))
        
        # Multi-scale harmonic component with varying spatial frequencies
        harmonic = np.sum(np.sin(50 * np.pi * x_norm) * np.cos(40 * np.pi * x_norm) + 
                          np.sin(60 * np.pi * x_norm**2) * np.cos(50 * np.pi * x_norm**2))
        
        # Combine all components with dynamic weights based on dimensionality
        weights = [0.25, 0.3, 0.2, 0.1, 0.1, 0.05]
        components = [chaotic_wave, ridge, peaks, cross_terms, rugged, harmonic]
        result = sum(w * c for w, c in zip(weights, components))
        
        # Add dynamic noise with amplitude controlled by function value
        noise_amp = 0.02 * (1 + np.abs(result))
        dynamic_noise = noise_amp * np.random.uniform(-0.5, 0.5)
        
        return result + dynamic_noise