import numpy as np

class ChaoticSineBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-wave interaction with logistic map modulation
        chaotic_term = 0.0
        r = 3.9  # Chaos parameter
        for i in range(self.dim):
            if i == 0:
                xi_prev = x[-1] if self.dim > 1 else 0
            else:
                xi_prev = x[i-1]
            chaotic_term += np.sin(r * xi_prev * (1 - xi_prev)) * np.sin(x[i])
        chaotic_term /= self.dim
        
        # Adaptive conditioning with dimension-dependent scaling
        cond_scale = 1.0 + 0.7 * np.std(x)  # Increased scaling factor
        adaptive_term = np.sum((x**2) * np.cos(3.0 * x) * cond_scale) / (self.dim * 2.0)
        
        # Cross-dimensional coupling with exponential interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])  # Modified decay rate
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-modal structure with sinusoidal basin modulation
        modal_term = np.sum(np.sin(2.0 * np.pi * x) * np.cos(0.5 * np.pi * x)) / self.dim
        
        # Dynamic noise injection with time-varying amplitude
        noise_amp = 0.15 + 0.07 * np.mean(np.abs(x))  # Increased noise amplitude
        noise_term = np.sum(noise_amp * np.sin(x * np.pi)) / self.dim
        
        # Polynomial distortion with asymmetric coefficients (modified exponents)
        poly_term = np.sum(0.4 * x**5 - 2.1 * x**4 + 3.0 * x**3 - 1.5 * x**2) / self.dim  # Modified coefficients
        
        # Fractal-like radial component for enhanced multimodality
        radial_term = np.sum(np.sin(0.6 * np.pi * np.sqrt(np.sum(x**2))) * np.cos(0.25 * np.pi * np.sqrt(np.sum(x**2)))) / self.dim  # Modified frequencies
        
        # Combine all terms with carefully tuned weights
        total = 0.19 * chaotic_term + 0.15 * adaptive_term + 0.16 * cross_term + 0.13 * modal_term + 0.14 * noise_term + 0.11 * poly_term + 0.12 * radial_term
        
        return total