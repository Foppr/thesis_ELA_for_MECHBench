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
        cond_scale = 1.0 + 0.5 * np.std(x)
        adaptive_term = np.sum((x**2) * np.cos(3.0 * x) * cond_scale) / (self.dim * 2.0)
        
        # Cross-dimensional coupling with exponential interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(x[i] + x[j])
        cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Multi-modal structure with sinusoidal basin modulation
        modal_term = np.sum(np.sin(2.0 * np.pi * x) * np.cos(0.5 * np.pi * x)) / self.dim
        
        # Dynamic noise injection with time-varying amplitude
        noise_amp = 0.1 + 0.05 * np.mean(np.abs(x))
        noise_term = np.sum(noise_amp * np.sin(x * np.pi)) / self.dim
        
        # Polynomial distortion with asymmetric coefficients
        poly_term = np.sum(0.5 * x**4 - 2.0 * x**3 + 1.5 * x**2) / self.dim
        
        # Quantum-inspired interference terms
        quantum_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quantum_term += np.sin(np.pi * (x[i] - x[j]) / (1 + np.abs(x[i] - x[j]))) * np.cos(np.pi * (x[i] + x[j]) / (1 + np.abs(x[i] + x[j])))
        quantum_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Fractal-like self-similarity patterns
        fractal_term = 0.0
        for i in range(self.dim):
            fractal_term += np.sin(2.0 * np.pi * x[i]) * np.cos(4.0 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        fractal_term /= self.dim
        
        # Enhanced cross-dimensional coupling with fractional exponents
        enhanced_cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                enhanced_cross_term += (np.abs(x[i] - x[j])**(1.5)) * np.sin(x[i] + x[j])
        enhanced_cross_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Additional modification: Introduce a new term to increase difficulty
        # This term creates more complex interference patterns and enhances non-separability
        interference_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference_term += np.sin(np.pi * (x[i]**2 - x[j]**2)) * np.cos(np.pi * (x[i] + x[j])**2)
        interference_term /= (self.dim * (self.dim - 1) / 2.0)
        
        # Combine all terms with carefully tuned weights
        total = 0.15 * chaotic_term + 0.14 * adaptive_term + 0.11 * cross_term + 0.13 * modal_term + 0.09 * noise_term + 0.10 * poly_term + 0.07 * quantum_term + 0.06 * fractal_term + 0.05 * enhanced_cross_term + 0.07 * interference_term
        
        return total