import numpy as np

class FractalQuantumGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal parameters
        self.hurst = 0.3
        self.fractal_scale = 1.0
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal Brownian motion component with higher dimensional interaction
        fbm_sum = 0.0
        for i in range(self.dim):
            # Enhanced fractal behavior using multiple sine/cosine combinations
            fbm_sum += (np.sin(x[i]) * np.cos(2 * x[i]) + 
                       0.5 * np.sin(3 * x[i]) * np.cos(4 * x[i]) +
                       0.3 * np.sin(5 * x[i]) * np.cos(6 * x[i]) +
                       0.1 * np.sin(7 * x[i]) * np.cos(8 * x[i]))
        
        # Quantum harmonic oscillator component with dynamic frequency and coupling
        quantum_sum = 0.0
        for i in range(self.dim):
            # Harmonic oscillator potential with quantum-like modulation and cross-coupling
            omega = 1.0 + 0.3 * np.sin(x[i]) + 0.2 * np.cos(2 * x[i])
            quantum_sum += 0.5 * omega**2 * x[i]**2 + 0.5 * (1 + 0.4 * np.cos(x[i])) + \
                          0.1 * np.sin(x[i]) * np.sum(np.sin(x[j]) for j in range(min(i+3, self.dim)) if j != i)
        
        # Adaptive gradient field component with non-linear strength modulation
        grad_sum = 0.0
        for i in range(self.dim):
            # Gradient field with adaptive strength based on position and neighborhood
            strength = 1.0 + 0.6 * np.sin(0.5 * x[i]) + 0.3 * np.cos(0.3 * x[i])
            grad_sum += strength * (x[i]**4 - 3*x[i]**3 + 2*x[i]**2 - x[i])
        
        # Multi-scale interference patterns with enhanced coupling
        interference_sum = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended interaction
                freq_i = 1.0 + 0.4 * np.sin(x[i])
                freq_j = 1.0 + 0.4 * np.cos(x[j])
                interference_sum += np.sin(freq_i * x[i]) * np.cos(freq_j * x[j]) * \
                                  np.exp(-0.15 * (x[i] - x[j])**2) * \
                                  (1 + 0.2 * np.sin(0.5 * (x[i] + x[j])))
        
        # Boundary attraction and repulsion with enhanced dynamic behavior
        boundary_sum = 0.0
        for i in range(self.dim):
            # Attract towards center, repel from boundaries with different strengths and phase modulation
            if x[i] < 0:
                boundary_sum += 2.5 * np.exp(-0.25 * (x[i] + 5.0)**2) * (1 + 0.3 * np.sin(4 * x[i]))
            else:
                boundary_sum += 2.0 * np.exp(-0.35 * (x[i] - 5.0)**2) * (1 + 0.2 * np.cos(3 * x[i]))
        
        # Chaotic modulation with logistic map and enhanced sensitivity
        chaotic_sum = 0.0
        r = 3.9  # Increased chaotic parameter for more complexity
        for i in range(self.dim):
            logistic_val = r * (x[i] / 5.0) * (1 - x[i] / 5.0)
            chaotic_sum += 0.5 * logistic_val**2 + 0.2 * np.sin(logistic_val)
        
        # Multi-modal Gaussian components with dynamic centers, widths and correlations
        gaussian_sum = 0.0
        for i in range(self.dim):
            center = 2.0 * np.sin(x[i]) + 0.5 * np.cos(2 * x[i])  # Dynamic center with multiple components
            width = 0.9 + 0.5 * np.cos(x[i])  # Dynamic width
            gaussian_sum += 1.5 * np.exp(-0.5 * ((x[i] - center) / width)**2) + \
                           0.3 * np.sin(3 * x[i]) * np.cos(4 * x[i])
        
        # Additional high-frequency oscillatory component for increased complexity
        high_freq_sum = 0.0
        for i in range(self.dim):
            high_freq_sum += 0.8 * np.sin(10 * x[i]) * np.cos(15 * x[i]) + \
                            0.4 * np.sin(20 * x[i])
        
        # Final combined function with enhanced weighting and non-linear combinations
        result = fbm_sum + quantum_sum + grad_sum + interference_sum + boundary_sum + \
                 chaotic_sum + gaussian_sum + high_freq_sum
        
        return result